import json
import logging
import os
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from dotenv import load_dotenv
from django.contrib.auth import login, logout
from .models import GoogleUser, Livro
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants

# Initialize logging
log_user = logging.getLogger('user')
views_logger = logging.getLogger('views_logger')

load_dotenv()

GOOGLE_CLIENT_ID = str(os.getenv('GOOGLE_API'))

# Create your views here.

def view_404(request, exception):
    return render(request, '404.html')

@login_required(login_url='/login/')
def home(request):
    if request.user.is_superuser:
        log_user.warning(f'Redirecionado para Login => User {request.user} necessita de um Google ID para prosseguir')
        return redirect('login')
    
    # Get image from user
    if request.user.is_authenticated:
        user = request.user
        try:
            actual = GoogleUser.objects.get(google_id=user.username)  # Assuming `user.username` is the Google ID
            image = actual.imagem_url
        except GoogleUser.DoesNotExist:
            image = None

    log_user.info(f'Acessou Pagina Home => User {request.user}')
    return render(request, 'home.html', {'imagem_url': image})

def login_view(request):
    log_user.info(f'Acessou Pagina Login => User {request.user}')
    return render(request, 'login.html', {'GOOGLE_CLIENT_ID': GOOGLE_CLIENT_ID})

@login_required(login_url='/login/')
def robots(request):
    log_user.info(f'Acessou Robots.txt => User {request.user}')
    return render(request, 'robots.txt')

# Google Login

def verify_google_token(token, client_id):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id, clock_skew_in_seconds=4)
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            return None, 'Invalid issuer'
        return idinfo, None
    except ValueError:
        return None, 'Invalid token'

@csrf_exempt
def google_login(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)

    try:
        body = json.loads(request.body)
        token = body.get('id_token')

        if not token:
            return JsonResponse({'error': 'Token not provided'}, status=400)

        idinfo, error = verify_google_token(token, GOOGLE_CLIENT_ID)

        if error:
            views_logger.error(f'Google login error: {error}')
            return JsonResponse({'error': error}, status=400)

        google_id = idinfo['sub']
        email = idinfo['email']
        nome = idinfo['name']
        imagem_url = idinfo['picture']

        # Check if the user already exists
        user, created = GoogleUser.objects.get_or_create(
            google_id=google_id,
            defaults={
                'nome': nome,
                'email': email,
                'imagem_url': imagem_url,
            }
        )

        user_django, created = User.objects.get_or_create(
            first_name=nome, email=email, username=google_id,
            defaults={'password': User.objects.make_random_password()}  # Ensure the user is created
        )

        if created:
            log_user.info(f'New user created via Google login: {user_django}')
        else:
            log_user.info(f'Existing user logged in via Google: {user_django}')

        login(request, user_django)
        messages.add_message(request, constants.SUCCESS, 'Usuário Logado com Sucesso')
        return JsonResponse({'status': 'ok', 'data': {'google_id': user.google_id, 'nome': user.nome, 'email': user.email}})

    except json.JSONDecodeError:
        views_logger.error('Invalid JSON in Google login request', exc_info=True)
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

def get_or_create_user(idinfo):
    google_id = idinfo['sub']
    email = idinfo['email']
    nome = idinfo['name']
    imagem_url = idinfo['picture']

    # Check if the user already exists
    user, _ = GoogleUser.objects.get_or_create(
        google_id=google_id,
        defaults={
            'nome': nome,
            'email': email,
            'imagem_url': imagem_url,
        }
    )
    return user, None

def user_logout(request):
    log_user.info(f'Logout => User {request.user}')
    logout(request)
    return redirect('login')

def listar_livros(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == "GET":
        livros = Livro.objects.all()
        return render(request, 'listar_livros.html', {'livros': livros})

def cadastrar_livro(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "GET":
        return render(request, 'cadastrar_livro.html', {'categorias': Livro.categoria_choices})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        categoria = request.POST.get('categorias')
        preco = request.POST.get('preco')
        paginas = request.POST.get('paginas')
        sinopse = request.POST.get('sinopse')
        autor = request.POST.get('autor')
        editora = request.POST.get('editora')
        ano = request.POST.get('ano')
        capa = request.FILES.get('capa')

        try:
            livro = Livro(
                nome=nome,
                categoria=categoria,
                preco=preco,
                paginas=paginas,
                sinopse=sinopse,
                autor=autor,
                editora=editora,
                ano=ano,
                capa=capa
            )
            livro.save()
            messages.add_message(request, constants.SUCCESS, 'Livro cadastrado com sucesso')
            return redirect('/cadastrar_livro')
        except Exception as e:
            log_user.error(f'Error saving book: {e}')
            messages.add_message(request, constants.ERROR, 'Algo deu errado')
            return redirect('/cadastrar_livro')

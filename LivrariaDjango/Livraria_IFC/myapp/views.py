import json
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from dotenv import load_dotenv
from django.contrib.auth import login, logout
import os
from .models import GoogleUser
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



load_dotenv()

GOOGLE_CLIENT_ID = str(os.getenv('GOOGLE_API'))

# Create your views here.

@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')

def login_view(request):

    return render(request, 'login.html', {'GOOGLE_CLIENT_ID': GOOGLE_CLIENT_ID})

@login_required(login_url='/login/')
def robots(request):
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

def get_or_create_user(idinfo):
    google_id = idinfo['sub']
    email = idinfo['email']
    nome = idinfo['name']
    imagem_url = idinfo['picture']

    # Check if the user already exists
    user = GoogleUser.objects.filter(google_id=google_id).first()
    if user:
        return user, None

    # If user does not exist, create new user
    user = GoogleUser.objects.create(
        google_id=google_id,
        nome=nome,
        email=email,
        imagem_url=imagem_url
    )
    return user, None

@csrf_exempt
def google_login(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            token = body.get('id_token')

            if not token:
                return JsonResponse({'error': 'Token not provided'}, status=400)

            idinfo, error = verify_google_token(token, GOOGLE_CLIENT_ID)

            if error:
                return JsonResponse({'error': error}, status=400)

            user, error = get_or_create_user(idinfo)

            if error:
                return JsonResponse({'error': error}, status=400)
            
            user_django, created = User.objects.get_or_create(username=user.google_id)
            login(request, user_django)

            return JsonResponse({'status': 'ok', 'data': {'google_id': user.google_id, 'nome': user.nome, 'email': user.email}})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def user_logout(request):
    logout(request)
    return redirect('login')
    
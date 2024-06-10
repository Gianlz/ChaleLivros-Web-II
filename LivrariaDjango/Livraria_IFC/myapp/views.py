import json, time
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
from django.http import JsonResponse
from django.shortcuts import render

from Livraria_IFC.settings import GOOGLE_CLIENT_ID

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def robots(request):
    return render(request, 'robots.txt')


# Google Login

@csrf_exempt
def google_login(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            token = body.get('id_token')

            idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)

            return JsonResponse({'status': 'ok', 'data': idinfo})
        except ValueError:
            return JsonResponse({'error': 'Invalid token'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("robots.txt", views.robots, name="robots"),
    path('google/', views.google_login, name='google_login'),
    path('logout/', views.user_logout, name='logout'),
]


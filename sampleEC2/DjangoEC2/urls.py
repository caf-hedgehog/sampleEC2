"""
Definition of urls for sampleEC2.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

app_name = "app"

urlpatterns = [
    path("", views.login, name="login"),
    path("register", views.register, name="register"),
    path("showlist", views.userList, name="userList"),
]

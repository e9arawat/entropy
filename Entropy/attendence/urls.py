from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('index', views.index, name='index'),
    
]
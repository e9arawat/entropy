
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('manager_login/', views.manager_login, name="manager_login"),
    path('manager_dashboard', views.manager_dashboard, name='manager_dashboard')
]

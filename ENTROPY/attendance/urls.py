from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employee_login/', views.employee_login, name="employee_login"),
    path('manager_login/', views.manager_login, name="manager_login"),
    path('manager_dashboard', views.manager_dashboard, name='manager_dashboard'),
    path('employee_dashboard', views.employee_dashboard, name='employee_dashboard'),
]

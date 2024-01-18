from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, "attendance/home.html")

def employee_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        print("hello************************************************************************************8")
        if user is not None:
            login(request, user)
            return redirect('employee_dashboard')
        else:
            error_message = "Invalid Credentials"
            return render(request, "attendance/employee_login.html", context={'error_message' : error_message})

    return render(request, "attendance/employee_login.html")


def manager_login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('manager_dashboard')
        else:
            error_message = "Invalid Credentials"
            return render(request, "attendance/manager_login.html", context={'error_message' : error_message})
    return render(request, "attendance/manager_login.html")


@user_passes_test(lambda x: x.is_superuser)
def manager_dashboard(request):
    return render(request, 'attendance/manager_dashboard.html')

@login_required
def employee_dashboard(request):
    return render(request, "attendance/employee_dashboard.html")
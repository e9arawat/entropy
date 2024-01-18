from django.shortcuts import render, redirect
from .forms import ManagerLoginForm
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, "attendence/home.html")

def manager_login(request):
    if request.method == "POST":
        form = ManagerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username,password)

            # Authenticating manager

            manager = authenticate(username=username, password=password)

            if manager is not None:
                login(request, manager)
                return redirect('manager_dashboard')
            else:
                error_message = "Invalid Credentials"
                return render(request, 'attendence/manager_login.html', context={'error_message' : error_message})
        else:
            print(form.errors)
    else:
        form = ManagerLoginForm()


    return render(request, "attendence/manager_login.html")


def manager_dashboard(request):
    return render(request, 'attendence/manager_dashboard.html')



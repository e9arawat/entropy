from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .models import UserStatus
from .forms import UserStatusForm
from datetime import datetime

# Create your views here.

def home(request):
    return render(request, "attendance/home.html")

def employee_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
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
            employee_data = User.objects.filter(is_staff=False)
            # redirect('manager_dashboard')
            return render(request, 'attendance/manager_dashboard.html', context={'employee_data' : employee_data})
        else:
            error_message = "Invalid Credentials"
            return render(request, "attendance/manager_login.html", context={'error_message' : error_message})
    return render(request, "attendance/manager_login.html")


@staff_member_required
def manager_dashboard(request):
    
    return render(request, 'attendance/manager_dashboard.html')

@login_required
def employee_dashboard(request):
    return render(request, "attendance/employee_dashboard.html")


@login_required
@staff_member_required
def update_status(request, username, status):
    user_status, created = UserStatus.objects.get_or_create(
        user=request.user,
        name=request.user.get_full_name(),
        date=datetime.date.today(),
        defaults={'status': status}
    )
    if not created:
        user_status.status = status
        user_status.save()
    return redirect('your_redirect_url')

@login_required
@staff_member_required
def submit_status(request):
    if request.method == 'POST':
        form = UserStatusForm(request.POST)
        if form.is_valid():
            user_status = form.save(commit=False)
            user_status.user = request.user
            user_status.name = request.user.get_full_name()
            user_status.date = datetime.date.today()
            user_status.save()
            return redirect('your_redirect_url')
    else:
        form = UserStatusForm()
    return render(request, 'submit_status.html', {'form': form})

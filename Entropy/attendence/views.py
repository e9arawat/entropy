from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import UserAttendance

# Create your views here.

def home(request):
    return render(request, "attendence/home.html")


def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('home')
    return render(request, "attendence/sign_in.html")

@login_required
def index(request):
    data = User.objects.all()
    return render(request, "attendence/index.html", context={'data' : data})




class CustomLoginView(LoginView):
    template_name = 'attendence/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.get_user()
        current_time = timezone.now().time()

        if current_time < timezone.timedelta(hours=10):
            UserAttendance.objects.create(user=user, attendance_status='Present')
        elif current_time < timezone.timedelta(hours=18):
            UserAttendance.objects.create(user=user, attendance_status='Late')
        else:
            UserAttendance.objects.create(user=user, attendance_status='Absent')

        return response
    

@login_required
def attendance_percentage(request):
    user = request.user
    total_days = user.userattendance_set.count()
    present_days = user.userattendance_set.filter(attendance_status='Present').count()
    attendance_percentage = (present_days / total_days) * 100
    context = {
        'total_days': total_days,
        'present_days': present_days,
        'attendance_percentage': attendance_percentage,
    }
    return render(request, 'attendance_percentage.html', context)

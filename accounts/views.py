from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import HomeHealthServiceForm
from django.shortcuts import render, redirect
from .forms import VirtualConsultationForm
from django.shortcuts import render, redirect
from .forms import RemoteMonitoringForm


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Log the user in
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('services')  # Redirect to a home page or dashboard
        else:
            return HttpResponse("Invalid login. Please try again.")
    return render(request, 'accounts/login.html')


def home_view(request):
    return render(request, 'accounts/home.html')


def about_view(request):
    return render(request, 'accounts/about.html')


def teams_view(request):
    return render(request, 'accounts/teams.html')

def services_view(request):
    return render(request, 'accounts/services.html')


def book_consultation(request):
    if request.method == 'POST':
        form = VirtualConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a new URL
    else:
        form = VirtualConsultationForm()
    return render(request, 'accounts/book_consultation.html', {'form': form})


def home_health_service(request):
    if request.method == 'POST':
        form = HomeHealthServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Adjust the redirect as needed
    else:
        form = HomeHealthServiceForm()
    return render(request, 'accounts/home_health_service.html', {'form': form})


def remote_monitoring_view(request):
    if request.method == 'POST':
        form = RemoteMonitoringForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Adjust the redirect as necessary
    else:
        form = RemoteMonitoringForm()
    return render(request, 'accounts/remote_monitoring.html', {'form': form})




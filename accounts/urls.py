from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('teams/', views.teams_view, name='teams'),
    path('services/', views.services_view, name='services'),
    path('book_consultation/', views.book_consultation, name='book_consultation'),
    path('home_health_service/', views.home_health_service, name='home_health_service'),
    path('remote_monitoring/', views.remote_monitoring_view, name='remote_monitoring'),
]

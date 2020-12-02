from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('upprofile/', views.UpdateProfile, name='upprofile'),
    path('adminpanel/', views.checkadmin, name='panel'),
]
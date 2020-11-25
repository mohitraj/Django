from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='att-home'),
    path('about', views.about, name='att-about'),
    path('contact', views.form_test, name='att-contact'),
    path('master', views.master_data, name='att-masterdata'),
    path('dismaster', views.display_master, name='display-master'),
]
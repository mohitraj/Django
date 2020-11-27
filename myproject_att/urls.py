"""myproject_att URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users_app.views import  loginPage, logoutUser


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('login/', auth_views.LoginView.as_view(template_name='users_app/login.html'), name='Login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='users_app/logout.html'), name='Logout'),
    #path('accounts/',include('users_app.urls')),
    path('login/', loginPage, name='Login' ),
    path('logout/', logoutUser, name='Logout' ),
    path('users/',include('users_app.urls')),
    path('att/', include('att_app.urls') )
]

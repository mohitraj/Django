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
from users_app.views import  loginPage, logoutUser, register
from django.conf.urls.static import static 
from django.conf import settings
from rest_framework.routers import DefaultRouter
from att_app import views

router = DefaultRouter()

router.register('studentapi', views.StudentModelViewSet, basename='student123')
router.register('studentread', views.StudentReadOnlyModelViewSet, basename='studentread')


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('login/', auth_views.LoginView.as_view(template_name='users_app/login.html'), name='Login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='users_app/logout.html'), name='Logout'),
    #path('accounts/',include('users_app.urls')),
    path('login/', loginPage, name='Login' ),
    path('logout/', logoutUser, name='Logout' ),
    path('', register, name='register' ),
    path('users/',include('users_app.urls')),
    path('blog/', include('blog.urls')),
    path('att/', include('att_app.urls') ),
    path('api-auth/', include('rest_framework.urls')),
    
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users_app/password_reset.html'), name='password_reset'),
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='users_app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='users_app/password_reset_confirm.html'), name='password_reset_confirm'),
	path('password_reset_complete/', 
    	auth_views.PasswordResetCompleteView.as_view(template_name='users_app/password_reset_complete.html'), 
    	name='password_reset_complete'),
    #path('password_reset_confirm/', auth_views.PasswordResetDoneView.as_view(template_name='users_app/password_reset_done.html'), name='password_reset_done' ),
    path('', include(router.urls)),

]
urlpatterns = urlpatterns+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import render, redirect 

from django.contrib.auth.forms import AuthenticationForm  # from user login 2nd approach 
from django.contrib.auth import authenticate, logout, login #from user login 2nd approach 
from django.contrib import messages
from .forms import SignUP
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm,ProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import User


# Create your views here.
def profile(request):
	return render(request, 'users_app/profile.html')

def loginPage(request):

	next=''
	if request.GET:
		next = request.GET['next']

	if request.method == 'POST':
		form = AuthenticationForm(request= request, data=request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username= username, password=password)
			if user is not None:
				login(request,user)
				if next=='':
					return redirect('profile')
				else :
					return redirect(next)
			else:
				messages.info(request, 'Username or Password is incorrect:)')

	form = AuthenticationForm()
	context = {'form': form, 'legend': 'Login Now'}
	return render(request, 'users_app/login.html', context)

def logoutUser(request):
	logout(request)
	messages.info(request, 'LoggedOut :)')
	return redirect('Login')


def register(request):
	form = SignUP()
	context = {'form': form, 'legend': "Register Now"}
	if request.method  == 'POST':
		form = SignUP(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f"Account created {username}")
			user = User.objects.filter(username=username).first()
			#Profile.objects.create(user=user)

			return redirect('Login')
	return render(request, 'users_app/login.html', context)


def UpdateProfile(request):
	if request.method  == 'POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f"Profile Updated")
			return redirect('profile')


	else :
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

		context = {'u_form' : u_form, 'p_form': p_form, 'legend': "Update Form"}
		return render(request, 'users_app/upprofile.html', context)


def checkadmin(request):
	return render(request, 'users_app/admin.html')
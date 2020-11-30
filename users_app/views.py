from django.shortcuts import render, redirect 

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # from user login 2nd approach 
from django.contrib.auth import authenticate, logout, login #from user login 2nd approach 
from django.contrib import messages



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
	context = {'form': form}
	return render(request, 'users_app/login.html', context)

def logoutUser(request):
	logout(request)
	messages.info(request, 'LoggedOut :)')
	return redirect('Login')


def register(request):
	form = UserCreationForm()
	context = {'form': form}
	if request.method  == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f"Account created {username}")
			return redirect('Login')
	return render(request, 'users_app/login.html', context)
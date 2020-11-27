from django.shortcuts import render, redirect 

from django.contrib.auth.forms import AuthenticationForm  # from user login 2nd approach 
from django.contrib.auth import authenticate, logout, login #from user login 2nd approach 
from django.contrib import messages

# Create your views here.
def profile(request):
	return render(request, 'users_app/profile.html')

def loginPage(request):
	if request.method == 'POST':
		form = AuthenticationForm(request= request, data=request.POST)
		if form.is_valid():
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username= username, password=password)
			if user is not None:
				login(request,user)
				return redirect('profile')
			else:
				messages.info(request, 'Username or Password is incorrect:)')

	form = AuthenticationForm()
	context = {'form': form}
	return render(request, 'users_app/login.html', context)

def logoutUser(request):
	logout(request)
	messages.info(request, 'LoggedOut :)')
	return redirect('Login')


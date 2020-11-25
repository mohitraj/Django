from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, MasterForm
from .models import Masterdata_dummy as md
from django.contrib import messages
# Create your views here.
posts = [
{
	'name' : 'sabiha',
	'roll_number' : 8809,
	'class' : 'CSE'
},
{
	'name' : 'Harpreet',
	'roll_number' : 809,
	'class' : 'CSE'
}]
def home(request):
	#print (request.get_host)
	#return HttpResponse("<h1> Hello Everyone</h1>")
	context = {'data' : posts, 'title': 'Game OVER'  }
	return render (request,'att_app/home.html', context)

def about(request):
	#return HttpResponse("<h1> This is about the Django</h1>")
	return render (request,'att_app/about.html')

def form_test(request):
	form =   ContactForm()
	context = {'form':form }
	return render (request,'att_app/display_form.html', context)

def display_master(request):
	data = md.objects.all()
	context = {'data': data}
	return render (request,'att_app/display_data.html', context)

def master_data(request):
	form = MasterForm()
	context= {'form':form }

	if request.method== 'POST':
		form1 = MasterForm(request.POST)
		if form1.is_valid():
			form1.save()
			messages.success(request, 'Record is added.')
			return redirect('display-master')


	return render (request,'att_app/display_form.html', context)


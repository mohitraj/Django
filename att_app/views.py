from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
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
}


]


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


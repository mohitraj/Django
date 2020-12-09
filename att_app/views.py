from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .forms import ContactForm, MasterForm, AttForm, CheckAttForm
from .models import Masterdata5 as md, Mark_Attendance2 
from django.contrib.auth.decorators import login_required

from users_app.decorators import allowed_users

from django.contrib import messages
import time 
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

@login_required(login_url='Login')
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

def e_h(t1):
	t9 = time.localtime(t1)
	return time.strftime('%d-%m-%Y-%H')

def display_att(request, roll_number):
	context = {  
	'data' : Mark_Attendance2.objects.filter(roll_number=roll_number)
	}
	return render(request, 'att_app/display_att.html', context)


def mark_att(request):
	form1 = AttForm()
	context= {'form':form1 }
	if request.method== 'POST':
		form1 = AttForm(request.POST)
		if form1.is_valid():
			try:
				mark1 = form1.save(commit=False)
				#print (mark1, dir(mark1))
				#print ("typeis ********", type(mark1))
				#print ("****",mark1.roll_number)
				#print ("time is *******",mark1.time1)
				#print (request.META.items())
				mark1.ip_address= request.META.get('REMOTE_ADDR')
				mark1.platform = request.META.get('HTTP_USER_AGENT')
				mark1.time1 = int(time.time())
				mark1.date1 = e_h(mark1.time1)
				mark1.Master = get_object_or_404(md, roll_number=mark1.roll_number)
				form1.save()
				messages.success(request, 'Attendance Marked :)')
				return redirect('display-att', roll_number=mark1.roll_number)
			except Exception as e :
				messages.warning(request, str(e))


	return render (request,'att_app/display_form.html', context)

##############################  Display things ##########################3

@login_required(login_url='Login')
@allowed_users(allowed_roles=['class10'] )
def CheckAttAll(request):
	context = { 'data' : Mark_Attendance2.objects.all()  }
	return render(request, 'att_app/display_att.html', context)

@login_required(login_url='Login')
@allowed_users(allowed_roles=['class10', 'class5'] )
def CheckAtt(request):
	form = CheckAttForm()
	context = {'form': form}
	if request.method == 'POST':
		form = CheckAttForm(request.POST)
		if form.is_valid():
			#print ("*******************",form.cleaned_data)
			d1 = form.cleaned_data['roll_number']
			data = Mark_Attendance2.objects.filter(roll_number=d1)
			context = {'data' : data}
			return render(request, 'att_app/display_att.html', context)


	return render(request, 'att_app/display_form.html', context)


############################################Code of REST #########################
from .serializers import AttSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly


def student_api1(request):
	if request.method == 'GET':
		data = md.objects.all() # Complext data type
		serial = AttSerializer(data, many=True) # 
		json_data = JSONRenderer().render(serial.data)
		return HttpResponse(json_data, content_type='application/json')

'''
@csrf_exempt
def student_api(request):
	if request.method == 'GET':
		json_data = request.body
		print (json_data, "heloooooooooooooooooooo")
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id', None)
		if id is not None:
			print ("id", id)
			stu = md.objects.get(id=id)
			serializer = AttSerializer(stu)
			json_data = JSONRenderer().render(serializer.data)
			return HttpResponse(json_data, content_type='application/json')

'''




'''
from rest_framework.generics import ListAPIView
class StudentList(ListAPIView):
    queryset = md.objects.all()
    serializer_class = AttSerializer

from rest_framework.generics import CreateAPIView
class StudentCreate(CreateAPIView):
    queryset = md.objects.all()
    serializer_class = AttSerializer

from rest_framework.generics import RetrieveAPIView
class StudentRetrieve(RetrieveAPIView):
    queryset = md.objects.all()
    serializer_class = AttSerializer

from rest_framework.generics import UpdateAPIView
class StudentUpdate(UpdateAPIView):
    queryset = md.objects.all()
    serializer_class = AttSerializer

from rest_framework.generics import DestroyAPIView
class StudentDelete(DestroyAPIView):
	queryset = md.objects.all()
	serializer_class = AttSerializer
'''

###################Generics classes#############
'''
from rest_framework.generics import RetrieveUpdateDestroyAPIView
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
	queryset = md.objects.all()
	serializer_class = AttSerializer

from rest_framework.generics import ListCreateAPIView
class StudentListCreate(ListCreateAPIView):
	queryset = md.objects.all()
	serializer_class = AttSerializer
'''

from rest_framework import viewsets
from .permissions import MohitPermission
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = md.objects.all()
    serializer_class = AttSerializer
    authentication=[SessionAuthentication] # Login style 
    #permission_classes=[IsAdminUser]  # authorization or permissions after login
    #permission_classes=[IsAuthenticatedOrReadOnly]
    #permission_classes=[DjangoModelPermissions]
    #permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    permission_classes=[MohitPermission]


















class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = md.objects.all()
    serializer_class = AttSerializer













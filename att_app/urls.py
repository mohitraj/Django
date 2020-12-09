from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='att-home'),
    path('about', views.about, name='att-about'),
    path('contact', views.form_test, name='att-contact'),
    path('master', views.master_data, name='att-masterdata'),
    path('dismaster', views.display_master, name='display-master'),
    path('mark_att', views.mark_att, name='att'),
    path('disatt/<int:roll_number>', views.display_att, name='display-att'),
    path('checkatt', views.CheckAtt, name='check-att'),
    path('checkattall', views.CheckAttAll, name='check-attAll'),
    #path('att_api/', views.StudentListCreate.as_view(), name='api'),
    #path('att_api_new/', views.student_api, name='api1'),
    #path('att_api/<int:pk>/', views.StudentRetrieve.as_view(), name='api_id'),
    #path('att_api/up/<int:pk>/', views.StudentUpdate.as_view(), name='api_up_id'),
    #path('att_api/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view(), name='api_dl_id'),
    



]

  
from django.contrib import admin
from .models import Masterdata5, Mark_Attendance2
# Register your models here.


admin.site.register(Mark_Attendance2)

@admin.register(Masterdata5)
class StudentAdmin(admin.ModelAdmin):
	list_display= ['id', 'name', 'roll_number', 'class_name', 'email']
from django.db import models

class Masterdata_dummy(models.Model):
	roll_number = models.IntegerField(null=False)
	name = models.CharField(max_length=100, null=False)
	email = models.EmailField(null=False)
	class_name = models.CharField(max_length=100, null=False)

	def __str__(self):
		return str(self.roll_number)

class Masterdata5(models.Model):
	class Meta:
		unique_together = (('roll_number', 'class_name'),)
	roll_number = models.IntegerField("Roll Number", null=False)
	name = models.CharField("Name", max_length=100, null=False)
	email = models.EmailField("Email", null=False)
	class_name = models.CharField("Class Name",max_length=100, null=False)

	def __str__(self):
		return str(self.roll_number)

class Mark_Attendance2(models.Model):
	class Meta:
		unique_together = (('roll_number', 'date1'),('date1', 'ip_address'))
	roll_number = models.IntegerField("Roll Number", null=False)
	class_name = models.CharField("Class Name",max_length=100, null=False)
	subject = models.CharField("Subject",max_length=100, null=False)
	time1 = models.IntegerField(null=False)
	ip_address = models.CharField(max_length=100, null=False)
	date1 = models.CharField(max_length=100, null=False)
	platform = models.CharField(max_length=200, null=False)
	Master = models.ForeignKey('Masterdata5', related_name='roll_no', on_delete=models.CASCADE)
	def __str__(self):
		return str(self.roll_number)
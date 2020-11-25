from django.db import models

# Create your models here.
class Masterdata_dummy(models.Model):
	roll_number = models.IntegerField(null=False)
	name = models.CharField(max_length=100, null=False)
	email = models.EmailField(null=False)
	class_name = models.CharField(max_length=100, null=False)

	def __str__(self):
		return str(self.roll_number)
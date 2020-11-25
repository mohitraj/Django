from django import forms
from .models import Masterdata_dummy

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class MasterForm(forms.ModelForm):
	class Meta:
		model = Masterdata_dummy
		fields = ['name', 'roll_number', 'class_name', 'email']


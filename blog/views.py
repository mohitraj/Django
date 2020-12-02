from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

# Create your views here.

class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post 
	fields = ['title', 'content']
	#template_name = blog/post_form.html  # custom name
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)


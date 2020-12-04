from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# Create your views here.

class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post    # Model name 
	fields = ['title', 'content'] 
	#template_name = blog/post_form.html  # custom name
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostDetailView(LoginRequiredMixin, DetailView):
	model = Post 
	#template_name = 'blog/post_detail.html'

class PostListView(LoginRequiredMixin, ListView):
	model =Post 
	template_name = 'blog/display.html'
	login_url = '/login/'
	context_object_name = 'mohit'
	ordering = ['-date1']
	paginate_by = 4

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post 
	fields = ['title', 'content'] 
	#template_name = blog/post_form.html  # custom name
	def form_valid(self,form):
		form.instance.author == self.request.user
		return super().form_valid(form)

	def test_func(self):
		post= self.get_object()
		if self.request.user == post.author:
			return True 
		return False



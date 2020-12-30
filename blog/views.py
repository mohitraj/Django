from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.

class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post    # Model name 
	fields = ['title', 'content'] 
	login_url = '/login/'
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


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post 
	success_url = '/blog/post/view'
	def test_func(self):
		post= self.get_object()
		if self.request.user == post.author:
			return True 
		return False


class UserPostListView(LoginRequiredMixin, ListView):
	model =Post 
	template_name = 'blog/display.html'
	login_url = '/login/'
	context_object_name = 'mohit'
	paginate_by = 4

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by("-date1")


class CommentCreateView(LoginRequiredMixin, CreateView):
	model = Comment
	login_url = '/login/'
	fields = ['content']
	template_name = 'blog/comment_form.html'

	def form_valid(self,form):
		print ("kwargs", self.kwargs)
		form.instance.author = self.request.user

		form.instance.post  = Post.objects.filter(id=self.kwargs.get('pk')).first()
		print ("form*******",form, dir(form))
		return super().form_valid(form)

class PostCommentView(View):
    def get(self, request, *args, **kwargs):
         view = PostDetailView.as_view()
         return view(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs) :
         view = CommentCreateView.as_view()
         return view(request, *args, **kwargs) 



def PostComment(request):
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


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post-sp', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post-sp', pk=post_pk)
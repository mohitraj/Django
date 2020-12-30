
from django.urls import path, include
from . import views

urlpatterns = [
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    #path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-sp'),
    path('post/<int:pk>/', views.PostCommentView.as_view(), name='post-sp'),
    path('post/view', views.PostListView.as_view(), name='post-details'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/comment', views.CommentCreateView.as_view(), name='comment_post'),
    path('post/<int:pk>/approve', views.comment_approve, name='comment_approve'),
    path('post/<int:pk>/remove', views.comment_remove, name='comment_remove'),

    

]
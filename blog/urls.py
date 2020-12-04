
from django.urls import path, include
from . import views

urlpatterns = [
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-sp'),
    path('post/view', views.PostListView.as_view(), name='post-details'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
]
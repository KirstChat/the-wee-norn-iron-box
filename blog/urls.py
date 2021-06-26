from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_posts, name='blog_posts'),
    path('post_detail/<post_id>/', views.post_detail, name='post_detail'),
    path('add_post/', views.add_post, name='add_post'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='home'),
    path('add_review/', views.add_review, name='add_review'),
    path('manage_reviews/', views.manage_reviews, name='manage_reviews'),
    path('delete_review/<int:review_id>/\
        ', views.delete_review, name='delete_review'),
]

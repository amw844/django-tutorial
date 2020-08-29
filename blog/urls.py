from django.urls import path
from . import views

urlpatterns = [
    path('posts', views.post_list, name='post_list'),
    path('', views.index),
    path('posts/<int:id>', views.post_item, name='post_item')
]
from django.urls import path
from . import views

urlpatterns = [
    path('resume', views.new_resume, name='new_resume'),
    path('resume/<int:id>', views.view_resume, name='view_resume')
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_student/', views.add_student, name='add_student'),
    path('all_students/', views.all_students, name='all_students'),
    path('about/', views.about, name='about'),
] 
 
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'navigation/index.html')

def add_student(request):
    return render(request,'navigation/add_student.html')

def all_students(request):
    return render(request, 'navigation/all_students.html')

def about(request):
    return render(request, 'navigation/about.html')

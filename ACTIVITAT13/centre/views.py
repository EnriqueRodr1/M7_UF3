from django.shortcuts import render
from .models import Student, Teacher

def index(request):
    return render(request, 'centre/index.html')

def students(request):
    students = Student.objects.all()
    return render(request, 'centre/students.html', {'students': students})

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'centre/teachers.html', {'teachers': teachers})

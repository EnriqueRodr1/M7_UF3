from django.shortcuts import render, get_object_or_404
from .models import Student, Teacher

def index(request):
    return render(request, 'centre/index.html')

def students(request):
    students = Student.objects.all()
    return render(request, 'centre/students.html', {'students': students})

def students_detalle(request, id):
    student = get_object_or_404(Student, pk=id)
    return render(request, 'centre/students_detalle.html', {'student': student})

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'centre/teachers.html', {'teachers': teachers})

def teachers_detalle(request, id):
    teacher = get_object_or_404(Teacher, pk=id)
    return render(request, 'centre/teachers_detalle.html', {'teacher': teacher})
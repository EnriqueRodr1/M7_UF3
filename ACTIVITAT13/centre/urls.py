from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('students/<int:id>/', views.students_detalle, name='students_detalle'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/<int:id>/', views.teachers_detalle, name='teachers_detalle'),
]

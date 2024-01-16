from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("cursos/", views.cursos, name="cursos"),
    path("estudiantes/", views.estudiantes, name="estudiantes"),
    path("profesores/", views.profesores, name="profesores"),
    path("entregables/", views.entregables, name="entregables"),
]

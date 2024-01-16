from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Entregable, Estudiantes
from AppCoder.forms import (
    formularioCurso,
    formularioEntregable,
    formularioEstudiante,
    formularioProfesor,
)


def inicio(request):
    return render(request, "AppCoder/index.html")


def busqueda(request):
    return render(request, "AppCoder/busqueda.html")


def profesores(request):
    if request.method == "POST":
        miFormulario = formularioProfesor(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Profesor(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                email=informacion["email"],
                profesion=informacion["profesion"],
            )
            profesor.save()
            return render(request, "AppCoder/profesores.html", {"status": "success"})
        else:
            miFormulario = formularioProfesor()
            return render(request, "AppCoder/profesores.html", {"status": "error"})

    return render(request, "AppCoder/profesores.html")


def estudiantes(request):
    if request.method == "POST":
        miFormulario = formularioEstudiante(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante = Estudiantes(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                email=informacion["email"],
            )
            estudiante.save()
            return render(request, "AppCoder/estudiantes.html", {"status": "success"})
        else:
            miFormulario = formularioEstudiante()
            return render(request, "AppCoder/estudiantes.html", {"status": "error"})

    return render(request, "AppCoder/estudiantes.html")


def entregables(request):
    if request.method == "POST":
        form = formularioEntregable(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            fecha_de_entrega = form.cleaned_data["fechaDeEntrega"]
            entregado = form.cleaned_data["entregado"]

            # Create or save the Entregable instance
            entregable = Entregable(
                nombre=nombre, fechaDeEntrega=fecha_de_entrega, entregado=entregado
            )
            entregable.save()

            return render(
                request,
                "AppCoder/entregables.html",
                {"form": form, "status": "success"},
            )
    else:
        form = formularioEntregable()
        return render(
            request, "AppCoder/entregables.html", {"form": form, "status": "error"}
        )

    return render(
        request, "AppCoder/entregables.html", {"form": form, "status": "initial"}
    )


def cursos(request):
    if request.method == "POST":
        miFormulario = formularioCurso(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()
            return render(request, "AppCoder/cursos.html", {"status": "success"})
        else:
            miFormulario = formularioCurso()
            return render(request, "AppCoder/cursos.html", {"status": "error"})

    return render(request, "AppCoder/cursos.html")

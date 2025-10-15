from django.shortcuts import render

from apps.estudiante.models import Estudiante, Curso


def index(request):
    return render(request, 'estudiante/index.html')


def alta_estudiante(request):
    return render(request, 'estudiante/alta_estudiante.html')


def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'estudiante/lista_cursos.html', {'cursos': cursos})
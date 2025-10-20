from django.shortcuts import render


from apps.estudiante.models import Estudiante, Curso
from apps.estudiante.forms import RegistrarAlumnoForm, RegistrarCursoForm



def index(request):
    return render(request,'estudiante/index.html')


def alta_estudiante(request):
    if request.method == 'POST':
        estudianteForm= RegistrarAlumnoForm(request.POST)
        if estudianteForm.is_valid():
            estudianteForm.save()
            return render(request, 'estudiante/alta_estudiante.html', {
                'form': RegistrarAlumnoForm(),
                'mensaje': '¡Estudiante registrado correctamente!'
            })

    else:
        estudianteForm = RegistrarAlumnoForm()
    
    return render(request, 'estudiante/alta_estudiante.html', {
        'form': estudianteForm
    })


def listar_estudiante(request):
    estudiantes = Estudiante.objects.all();

    return render(request, 'estudiante/lista_estudiantes.html', {'estudiantes':estudiantes})





def alta_curso(request):
    if request.method == 'POST':
        cursoForm = RegistrarCursoForm(request.POST)
        if cursoForm.is_valid():
            cursoForm.save()

            return render(request, 'estudiante/alta_curso.html',{
                'form': RegistrarCursoForm(),
                'mensaje': 'Curso registrado Correctamente'
            })
    else:
        cursoForm = RegistrarCursoForm()

    return render(request, 'estudiante/alta_curso.html', {'form': cursoForm})


def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'estudiante/lista_cursos.html', {'cursos': cursos})
from django.urls import path
from apps.estudiante import views

app_name = 'estudiante'

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.alta_estudiante, name='alta_estudiante'),
    path('agregar_curso/', views.alta_curso, name= 'alta_curso'),
    path('listar_cursos/', views.listar_cursos, name='listar_cursos'),
    path('listar_estudiantes/', views.listar_estudiante , name='listar_estudiantes')
]
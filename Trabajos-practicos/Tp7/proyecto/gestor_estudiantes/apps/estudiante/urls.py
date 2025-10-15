from django.urls import path
from apps.estudiante import views

app_name = 'estudiante'

urlpatterns = [
    path('', views.index, name='index'),
    path('alta', views.alta_estudiante, name='alta_estudiante'),
    path('listar_cursos', views.listar_cursos, name='listar_cursos'),
]
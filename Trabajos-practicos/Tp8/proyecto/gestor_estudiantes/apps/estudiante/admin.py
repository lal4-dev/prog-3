from django.contrib import admin
from .models import Estudiante, Curso

# Register your models here.
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre_curso', 'cantidad_horas_curso']
    search_fields = ('nombre_curso',) 

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['nombre_estudiante', 'apellido_estudiante', 'edad_estudiante', 'nota_curso_estudiante']
    search_fields = ('nombre_estudiante',) 

    



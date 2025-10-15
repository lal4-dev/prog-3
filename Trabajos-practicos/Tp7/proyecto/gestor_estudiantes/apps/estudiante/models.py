from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre_curso = models.TextField(max_length=250, unique=True);
    cantidad_horas_curso = models.TextField(unique=True);

    def __str__(self):
        return f'nombre del curso:{self.nombre_curso}, cantidad de horas:{self.cantidad_horas_curso}';

class Estudiante(models.Model):
    nombre_estudiante = models.TextField(max_length=250, unique=True);
    apellido_estudiante = models.TextField(max_length=250, unique=True);
    edad_estudiante = models.IntegerField(unique=True);
    nota_curso_estudiante = models.IntegerField(blank=True, null=True);
    curso_estudiante = models.TextField(max_length=250, blank=True);

    cursos = models.ManyToManyField(Curso, related_name='estudiantes')

    def __str__(self):
        return f'nombre:{self.nombre_estudiante}, apellido:{self.apellido_estudiante}, edad: {self.edad_estudiante}, nota: {self.nota_curso_estudiante}, curso: {self.curso_estudiante}';



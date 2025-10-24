from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=250, unique=True);
    cantidad_horas_curso = models.IntegerField(blank=False, null=False);

    def __str__(self):
        return f'nombre del curso:{self.nombre_curso}, cantidad de horas:{self.cantidad_horas_curso}';

class Estudiante(models.Model):
    nombre_estudiante = models.CharField(max_length=250, blank=False ,null=False);
    apellido_estudiante = models.CharField(max_length=250, blank=False ,null=False);
    edad_estudiante = models.IntegerField(blank=False ,null=False);
    nota_curso_estudiante = models.IntegerField(blank=False ,null=False);

    cursos = models.ManyToManyField(Curso, related_name='estudiantes')

    def __str__(self):
        cursos_nombres = ', '.join([c.nombre_curso for c in self.cursos.all()])
        return f'nombre:{self.nombre_estudiante}, apellido:{self.apellido_estudiante}, edad: {self.edad_estudiante}, nota: {self.nota_curso_estudiante}, curso: {cursos_nombres}';



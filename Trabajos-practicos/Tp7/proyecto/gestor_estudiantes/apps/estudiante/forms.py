from django import forms
from apps.estudiante.models import Estudiante, Curso


class RegistrarAlumnoForm(forms.ModelForm):
    cursos = forms.ModelMultipleChoiceField(
            queryset=Curso.objects.all(),
            widget=forms.SelectMultiple,
            required=False,
            label='Cursos disponibles'
        )

    class Meta:
        model = Estudiante
        fields = ['nombre_estudiante', 'apellido_estudiante', 'edad_estudiante', 'nota_curso_estudiante','cursos']



class RegistrarCursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre_curso', 'cantidad_horas_curso']
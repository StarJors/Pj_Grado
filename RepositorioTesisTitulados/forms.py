from django import forms
from django.contrib import admin
from .models import Estudiante, Tesis

class TesisForm(forms.ModelForm):
    class Meta:
        model = Tesis
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Personalizar queryset para el campo postulante
        self.fields['postulante'].queryset = Estudiante.objects.all()
        self.fields['postulante'].label_from_instance = lambda obj: f"{obj.nombre} {obj.apellido}"

class TesisAdmin(admin.ModelAdmin):
    form = TesisForm
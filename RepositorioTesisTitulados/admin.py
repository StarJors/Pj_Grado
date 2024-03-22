from django.contrib import admin
from .models import Docente, TutorExterno, Modalidad, Materia, Tesis, Estudiante
from .forms import TesisForm

class TesisAdmin(admin.ModelAdmin):
    form = TesisForm
    list_display = ('titulo', 'postulante', 'modalidad', 'fecha', 'numero_acta', 'display_tribunales','pdf_tesis')  
    search_fields = ('titulo', 'postulante__nombre', 'postulante__apellido', 'modalidad__nombre')  
    ordering = ('-fecha',)

    def display_tribunales(self, obj):
        return ", ".join([Docente.nombre +" "+ Docente.apellido for Docente in obj.tribunales.all()])
    display_tribunales.short_description = 'Tribunales'

admin.site.register(Tesis, TesisAdmin)

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')
    search_fields = ('nombre', 'apellido')

@admin.register(TutorExterno)
class TutorExternoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')
    search_fields = ('nombre', 'apellido')

admin.site.register(Modalidad)

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sigla', 'plan')
    search_fields = ('nombre', 'sigla', 'plan')

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('ru','ci','nombre', 'apellido','anio_ingreso','periodo_ingreso','gestion','periodo_salida','nota')
    search_fields = ('ru','ci','nombre', 'apellido')

admin.site.register(Estudiante, EstudianteAdmin)

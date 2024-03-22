from django.db import models

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class TutorExterno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Modalidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Materia(models.Model):
    sigla = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    plan = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Estudiante(models.Model):
    ru = models.CharField(max_length=50)
    ci = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    anio_ingreso = models.PositiveIntegerField()
    periodo_ingreso = models.CharField(max_length=50)
    gestion = models.CharField(max_length=50)
    periodo_salida = models.CharField(max_length=50)
    nota = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Tesis(models.Model):
    titulo = models.CharField(max_length=255)
    postulante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='tesis_postulante')
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE, related_name='tesis_modalidad')
    fecha = models.DateField()
    numero_acta = models.CharField(max_length=50, null=True, blank=True)
    tribunales = models.ManyToManyField(Docente, related_name='tesis_tribunales')
    tutor = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='tesis_tutor', null=True, blank=True)
    tutor_externo = models.ForeignKey(TutorExterno, on_delete=models.CASCADE, related_name='tesis_tutor_externo', null=True, blank=True)
    pdf_tesis = models.FileField(upload_to='tesis/', null=True, blank=True)

    def __str__(self):
        return self.titulo

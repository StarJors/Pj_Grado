from django.shortcuts import render
from django.http import FileResponse, Http404
from .models import Estudiante,Tesis
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os

# Create your views here.

def pdf_view(request, pdf_name):
    # Ruta al directorio donde se almacenan los PDFs
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', pdf_name)

    # Verificar si el archivo existe
    if os.path.exists(pdf_path):
        # Servir el archivo PDF utilizando FileResponse
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    else:
        # Si el archivo no existe, retornar un error 404
        raise Http404("El archivo PDF no existe")

def titulados(request):
    query = request.GET.get('q')
    estudiantes_list = Estudiante.objects.all()

    if query:
        estudiantes_list = estudiantes_list.filter(nombre__icontains=query)

    paginator = Paginator(estudiantes_list, 4)

    page = request.GET.get('page')
    try:
        estudiantes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        estudiantes = paginator.page(1)
    except EmptyPage:

        estudiantes = paginator.page(paginator.num_pages)

    return render(request, 'titulados.html', {'estudiantes': estudiantes, 'query': query})


# Titulado Detalle
def titulado_detalle(request, pk):
    estudiante = Estudiante.objects.get(pk=pk)
    return render(request, 'titulado_detalle.html', {'estudiante': estudiante})


# Tesis
def tesis(request):
    tesis = Tesis.objects.all()
    return render(request,'tesis.html',{'tesis': tesis})
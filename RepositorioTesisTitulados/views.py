from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404
from .models import Estudiante, Tesis
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import os

def pdf_view(request, pdf_name):
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'pdfs', pdf_name)

    if os.path.exists(pdf_path):
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    else:
        raise Http404("El archivo PDF no existe")

def titulados(request):
    query = request.GET.get('q')
    estudiantes_list = Estudiante.objects.all()

    if query:
        estudiantes_list = estudiantes_list.filter(nombre__icontains=query)

    paginator = Paginator(estudiantes_list, 10)
    page = request.GET.get('page')

    try:
        estudiantes = paginator.page(page)
    except PageNotAnInteger:
        estudiantes = paginator.page(1)
    except EmptyPage:
        estudiantes = paginator.page(paginator.num_pages)

    return render(request, 'titulados.html', {'estudiantes': estudiantes, 'query': query})

def titulado_detalle(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'titulado_detalle.html', {'estudiante': estudiante})

def tesis_detalle(request, pk):
    tesis = get_object_or_404(Tesis, pk=pk)
    return render(request, 'tesis_detalle.html', {'tesis': tesis})

def tesis_detalle_p(request, pk):
    tesis = get_object_or_404(Tesis, pk=pk)
    return render(request, 'tesis_detalle_p.html',{'tesis':tesis})

def tesis(request):
    query = request.GET.get('q')
    tesis_list = Tesis.objects.all().order_by('titulo')

    if query:
        tesis_list = tesis_list.filter(
            Q(titulo__icontains=query) | 
            Q(postulante__nombre__icontains=query) | 
            Q(postulante__apellido__icontains=query)| 
            Q(fecha__icontains=query)
        )

    tesis_paginator = Paginator(tesis_list, 15)
    page = request.GET.get('page')

    try:
        tesis = tesis_paginator.page(page)
    except PageNotAnInteger:
        tesis = tesis_paginator.page(1)
    except EmptyPage:
        tesis = tesis_paginator.page(tesis_paginator.num_pages)

    return render(request, 'tesis.html', {'tesis': tesis, 'query': query})

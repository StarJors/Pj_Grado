"""
URL configuration for Proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Usuarios import views
from RepositorioTesisTitulados import views as r
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # APLICACION USUARIO
    path('',views.home, name='home'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registrar/', views.registrar, name='registrar'),
    path('CerrarSesion/',views.CerrarSesion, name='CerrarSesion'),

    #APLICACION REPOSITORIO TESIS TITULADO
    path('pdfs/<str:pdf_tesis>/', r.pdf_view, name='pdf_view'),
    path('titulados/',r.titulados, name='titulados'),
    path('titulados/titulado_detalle/<int:pk>/', r.titulado_detalle, name='titulado_detalle'),
    path('tesis/',r.tesis, name='tesis'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

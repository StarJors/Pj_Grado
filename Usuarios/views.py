from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
#
##
###
# Pagina Principal
def home(request):
    return render(request,'home.html')

# Iniciar Sesion
def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm(request)
    
    return render(request, 'IniciarSesion.html', {'form': form})


def registrar(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar')
        else:
            print(form.errors)  # Agrega esta línea para imprimir los errores en la consola
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'IniciarSesion.html', {'form': form})
#Cerrar Sesion
def CerrarSesion(request):
    logout(request)
    return redirect('registrar')
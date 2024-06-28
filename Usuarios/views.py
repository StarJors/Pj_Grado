from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm

# Página Principal
def home(request):
    return render(request, 'home.html')

# Iniciar Sesión
def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'IniciarSesion.html', {'form': form})

# Registrar Usuario
def registrar(request):
    errors = None
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciar_sesion')
        else:
            errors = form.errors  # Captura los errores
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'IniciarSesion.html', {'form': form, 'errors': errors})

# Cerrar Sesión
def CerrarSesion(request):
    logout(request)
    return redirect('registrar')

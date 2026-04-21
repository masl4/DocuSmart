from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.save()
            login(request, usuario)  # Iniciar sesión automáticamente tras registrarse
            return redirect('inicio')  # Redirigir a la página principal
        else:
            print("Errores en el formulario:", form.errors)  # Para depuración en la terminal
    else:
        form = RegistroForm()

    return render(request, 'usuarios/registro.html', {'form': form})


def login_usuario(request): # Login usuario
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('inicio')  # Redirige a la página principal tras loguearse
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})


def logout_usuario(request):
    logout(request)
    return redirect('login')


@login_required
def abrir_perfil(request):
    return render(request, 'documentos/perfil.html', {'user': request.user})

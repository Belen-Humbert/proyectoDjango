from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def login_view(request):
    # Aquí puedes agregar la lógica de autenticación o simplemente renderizar el formulario de login
    return render(request, 'login_app/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Guardamos el usuario, el hash de la contraseña se maneja automáticamente
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}. ¡Ahora puedes iniciar sesión!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'login_app/registro.html', {'form': form})

def password_reset_view(request):
    # Aquí puedes agregar la lógica de recuperación de contraseña o simplemente renderizar el formulario correspondiente
    return render(request, 'login_app/password_reset.html')

# login_app/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.utils.translation import gettext_lazy as _

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
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not User.objects.filter(email=email).exists():
                messages.error(request, _("Por favor, ingresa el email con el que te registraste."))
                return render(request, 'login_app/password_reset.html', {'form': form})
            # Si el email está registrado, se envía el email de restablecimiento (esto se manejará automáticamente por Django)
            form.save(request=request)
            messages.success(request, _("Te hemos enviado un enlace para restablecer la contraseña."))
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'login_app/password_reset.html', {'form': form})

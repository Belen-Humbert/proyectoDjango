from django.shortcuts import redirect
from django.contrib.auth.models import User


def registrarUsuario(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        # Crear y guardar el user

        User.objects.create(username = username, email = email, password = password)
        return redirect('/')
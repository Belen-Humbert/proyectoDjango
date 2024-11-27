from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def registrarUsuario(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        # Crear y guardar el user

        User.objects.create_user(username = username, email = email, password = password)
        return redirect('/') #(función de Django para manejar usuarios de forma segura).
    

def verificarUser(request):
    if request.method == 'POST':
        nombre = request.POST['username']
        contraseña = request.POST['password']

        # comprueba si las credenciales ingresadas coinciden con las de un usuario en la base de datos.
        user = authenticate(request, username=nombre, password=contraseña)

        if user is not None:  # Si la autenticación fue exitosa
            login(request, user)  # Este método inicia sesión en el sistema y establece una sesión para el usuario, lo que permite que el usuario esté autenticado en futuras peticiones.
            return redirect('/')  # Redirige a la página principal
        else:
            # Si la autenticación falla se muestra mensaje de error
            return render(request, 'login_app/login.html', {
                'error_message': 'Nombre o contraseña incorrecta'
            })
    
     # Si la solicitud no es POST, redirigir o renderizar una página de error o de login
    return render(request, 'login_app/registro.html')

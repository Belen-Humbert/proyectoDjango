from django.contrib import admin  # Importa admin
from django.urls import path, include
from appDjango.login import views  # Importa las vistas de login

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('login/', include('appDjango.login.urls')),  # Incluir las rutas del login
    path('', views.home_view, name='home'),  # Ruta para la página de inicio
]
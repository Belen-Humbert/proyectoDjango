from django.urls import path #define las rutas (URLs) asociadas a las vistas.
from . import views #Importa las vistas definidas en el archivo views.py del mismo directorio.
from django.contrib.auth.views import LogoutView #Define las rutas disponibles en la aplicación.


urlpatterns = [
    path('registrarUser/', views.registrarUsuario, name='registrarUser'),
    path('verificarUsuario/', views.verificarUser, name='verificarUsuario'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
    
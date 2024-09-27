from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('appDjango.login.urls')),  #  rutas del login
]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', include('login_app.urls')),
    path('catalogo/', include('catalogo_app.urls')),
    path('carrito/', include('carrito_app.urls')),
    path('crud/', include('crud_app.urls')),
]

# Servir archivos de medios durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

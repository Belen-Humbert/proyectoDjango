from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_view, name='catalogo'),
    path('categoria/<int:categoria_id>/', views.poductCat, name='productCat'),
]

# Solo en desarrollo, sirve archivos de medios
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

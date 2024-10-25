from django.contrib import admin
from .models import Product, Category

# Register your models here.
# Registrar el modelo Producto
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
        search_fields = ('nombre',)  # Búsqueda por nombre
        list_filter = ('precio', 'stock')  # Filtro por precio y stock
        ordering = ('nombre',)  # Ordenar por nombre    
        list_display = [field.name for field in Product._meta.fields]  # Mostrar todas las columnas

# Registrar el modelo Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)  # Búsqueda por nombre
    list_filter = ('nombre',)  # Filtro por nombre (la categoría no suele tener precio o stock)
    ordering = ('nombre',)  # Ordenar por nombre    
    list_display = [field.name for field in Category._meta.fields]  # Mostrar todas las columnas
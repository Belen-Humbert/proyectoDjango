from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem

# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
        list_display = [field.name for field in Cart._meta.fields]  # Mostrar todas las columnas

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
        list_display = [field.name for field in CartItem._meta.fields]  # Mostrar todas las columnas

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
        list_display = [field.name for field in Order._meta.fields]  # Mostrar todas las columnas

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
        list_display = [field.name for field in OrderItem._meta.fields]  # Mostrar todas las columnas

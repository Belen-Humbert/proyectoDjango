# catalogo_app/management/commands/populate_db.py
from django.core.management.base import BaseCommand
from catalogo_app.models import Product, Category

class Command(BaseCommand):
    help = 'Popula la base de datos con productos de ejemplo'

    def handle(self, *args, **kwargs):
        categoria_electronica = Category.objects.create(
            nombre='Electrónica',
            descripcion='Dispositivos electrónicos'
        )
        categoria_accesorios = Category.objects.create(
            nombre='Accesorios',
            descripcion='Accesorios para dispositivos'
        )

        products = [
            {
                'nombre': 'Smartphone X1',
                'descripcion': 'Un smartphone de última generación con características avanzadas.',
                'precio': 999.99,
                'stock': 50,
                'categoria': categoria_electronica,
            },
            {
                'nombre': 'Laptop Pro',
                'descripcion': 'Una laptop potente para profesionales y gamers.',
                'precio': 1499.99,
                'stock': 30,
                'categoria': categoria_electronica,
            },
            {
                'nombre': 'Auriculares Noise-X',
                'descripcion': 'Auriculares con cancelación de ruido y sonido de alta calidad.',
                'precio': 299.99,
                'stock': 100,
                'categoria': categoria_accesorios,
            },
            {
                'nombre': 'Smartwatch A1',
                'descripcion': 'Un reloj inteligente con múltiples funciones.',
                'precio': 199.99,
                'stock': 75,
                'categoria': categoria_electronica,
            },
            {
                'nombre': 'Tablet Z2',
                'descripcion': 'Una tablet versátil para el entretenimiento y el trabajo.',
                'precio': 499.99,
                'stock': 40,
                'categoria': categoria_electronica,
            },
            {
                'nombre': 'Cargador Rápido',
                'descripcion': 'Cargador rápido para dispositivos móviles.',
                'precio': 29.99,
                'stock': 150,
                'categoria': categoria_accesorios,
            },
            {
                'nombre': 'Televisor 4K',
                'descripcion': 'Televisor de alta definición con tecnología 4K.',
                'precio': 799.99,
                'stock': 20,
                'categoria': categoria_electronica,
            },
            {
                'nombre': 'Altavoces Bluetooth',
                'descripcion': 'Altavoces portátiles con conectividad Bluetooth.',
                'precio': 89.99,
                'stock': 60,
                'categoria': categoria_accesorios,
            },
            {
                'nombre': 'Cámara Digital',
                'descripcion': 'Cámara digital con lente intercambiable.',
                'precio': 599.99,
                'stock': 15,
                'categoria': categoria_electronica,
            },
            {
                'nombre': 'Drone X5',
                'descripcion': 'Drone con cámara HD y control remoto.',
                'precio': 399.99,
                'stock': 25,
                'categoria': categoria_electronica,
            },
            {
                'nombre': 'Teclado Mecánico',
                'descripcion': 'Teclado mecánico para gamers con retroiluminación.',
                'precio': 129.99,
                'stock': 40,
                'categoria': categoria_accesorios,
            },
            {
                'nombre': 'Mouse Gaming',
                'descripcion': 'Mouse ergonómico para juegos con alta precisión.',
                'precio': 59.99,
                'stock': 80,
                'categoria': categoria_accesorios,
            },
            {
                'nombre': 'Monitor 27"',
                'descripcion': 'Monitor de 27 pulgadas con resolución Full HD.',
                'precio': 299.99,
                'stock': 30,
                'categoria': categoria_electronica,
            },
            {
                'nombre': 'Router WiFi',
                'descripcion': 'Router de alta velocidad para conexión a internet.',
                'precio': 69.99,
                'stock': 50,
                'categoria': categoria_accesorios,
            },
            {
                'nombre': 'Batería Externa',
                'descripcion': 'Batería externa de alta capacidad para dispositivos móviles.',
                'precio': 39.99,
                'stock': 100,
                'categoria': categoria_accesorios,
            },
            {
                'nombre': 'Proyector Portátil',
                'descripcion': 'Proyector portátil para presentaciones y entretenimiento.',
                'precio': 499.99,
                'stock': 10,
                'categoria': categoria_electronica,
            },
            {
                'nombre': 'Soporte para Laptop',
                'descripcion': 'Soporte ajustable para laptop con ventilación.',
                'precio': 49.99,
                'stock': 70,
                'categoria': categoria_accesorios,
            },
            {
                'nombre': 'Funda para Smartphone',
                'descripcion': 'Funda protectora para smartphone.',
                'precio': 19.99,
                'stock': 200,
                'categoria': categoria_accesorios,
            },
            {
                'nombre': 'Cámara de Seguridad',
                'descripcion': 'Cámara de seguridad con visión nocturna.',
                'precio': 149.99,
                'stock': 40,
                'categoria': categoria_electronica,
            },
            {
                'nombre': 'Gafas de Realidad Virtual',
                'descripcion': 'Gafas de realidad virtual para una experiencia inmersiva.',
                'precio': 299.99,
                'stock': 20,
                'categoria': categoria_electronica,
            },
        ]

        for product in products:
            Product.objects.create(**product)
            
        self.stdout.write(self.style.SUCCESS('Base de datos populada exitosamente'))
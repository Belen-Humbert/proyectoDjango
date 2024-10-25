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
        ]

        for product in products:
            Product.objects.create(**product)
            
        self.stdout.write(self.style.SUCCESS('Base de datos populada exitosamente'))
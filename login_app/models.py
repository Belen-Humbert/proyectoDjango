from django.db import models

class Category(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Product(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.nombre

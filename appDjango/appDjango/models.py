from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Modelo de Usuario
class Usuario(AbstractBaseUser, PermissionsMixin):
    """
    Este modelo representa a los usuarios de la aplicación.
    """
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    email_verificado_en = models.DateTimeField(null=True, blank=True)
    contrasena = models.CharField(max_length=255)  # Cambiado 'contraseña' por 'contrasena'
    token_recordar = models.CharField(max_length=255, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    # Especificar related_name personalizado para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text="Los grupos a los que pertenece este usuario.",
        verbose_name="grupos"
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text="Los permisos específicos para este usuario.",
        verbose_name="permisos de usuario"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        """
        Retorna el email del usuario.
        """
        return str(self.email)

# Modelo de Rol
class Rol(models.Model):
    """
    Este modelo representa los roles que pueden tener los usuarios.
    """
    nombre = models.CharField(max_length=100)
    nombre_guardia = models.CharField(max_length=50)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Retorna el nombre del rol.
        """
        return str(self.nombre)

# Modelo de Permiso
class Permiso(models.Model):
    """
    Este modelo representa los permisos que pueden tener los usuarios o roles.
    """
    nombre = models.CharField(max_length=100)
    nombre_guardia = models.CharField(max_length=50)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Retorna el nombre del permiso.
        """
        return str(self.nombre)

# Modelo de Token de Acceso Personal
class TokenAccesoPersonal(models.Model):
    """
    Este modelo representa los tokens de acceso personal utilizados para autenticar usuarios.
    """
    tipo_tokenable = models.CharField(max_length=100)
    tokenable_id = models.BigIntegerField()
    nombre = models.CharField(max_length=100)
    habilidades = models.TextField()
    ultimo_uso_en = models.DateTimeField(null=True, blank=True)
    expira_en = models.DateTimeField()

    def __str__(self):
        """
        Retorna el nombre del token de acceso personal.
        """
        return str(self.nombre)

# Modelo de Restablecimiento de Contrasena
class RestablecimientoContrasena(models.Model):  # Cambiado 'RestablecimientoContraseña' por 'RestablecimientoContrasena'
    """
    Este modelo representa los tokens de restablecimiento de contraseña para los usuarios.
    """
    email = models.EmailField()
    token = models.CharField(max_length=255)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Retorna el email asociado al restablecimiento de contraseña.
        """
        return str(self.email)

# Modelo intermedio de relación Permiso-Modelo
class ModeloTienePermiso(models.Model):
    """
    Este modelo representa la relación entre un permiso y un modelo en el sistema.
    """
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)
    tipo_modelo = models.CharField(max_length=100)
    modelo_id = models.BigIntegerField()

    def __str__(self):
        """
        Retorna una representación de la relación permiso-modelo.
        """
        return str(f"{self.tipo_modelo} tiene permiso {self.permiso}")

# Modelo intermedio de relación Rol-Modelo
class ModeloTieneRol(models.Model):
    """
    Este modelo representa la relación entre un rol y un modelo en el sistema.
    """
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    tipo_modelo = models.CharField(max_length=100)
    modelo_id = models.BigIntegerField()

    def __str__(self):
        """
        Retorna una representación de la relación rol-modelo.
        """
        return str(f"{self.tipo_modelo} tiene rol {self.rol}")

# Modelo intermedio de relación Rol-Permiso
class RolTienePermiso(models.Model):
    """
    Este modelo representa la relación entre un rol y un permiso en el sistema.
    """
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retorna una representación de la relación rol-permiso.
        """
        return str(f"Rol {self.rol} tiene permiso {self.permiso}")

# Modelo de Producto
class Producto(models.Model):
    """
    Este modelo representa los productos que se pueden vender en la aplicación.
    """
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.TextField()
    imagen = models.CharField(max_length=255, null=True, blank=True)
    stock = models.IntegerField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Retorna el nombre del producto.
        """
        return str(self.nombre)

# Modelo de Categoría
class Categoria(models.Model):
    """
    Este modelo representa las categorías de los productos.
    """
    nombre = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Retorna el nombre de la categoría.
        """
        return str(self.nombre)

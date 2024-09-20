# Proyecto Django con SQL Server

Este proyecto es una aplicación web creada con Django que permite la gestión de usuarios, productos y compras. Está diseñada para utilizar una base de datos SQL Server mediante el conector `pyodbc`.

## Requerimientos del Sistema

### 1. Requisitos Funcionales

#### 1. Registro de Usuarios
- Los usuarios pueden registrarse con un nombre de usuario, correo electrónico y contraseña.
- La contraseña es almacenada de manera segura utilizando hashing.

#### 2. Autenticación de Usuarios
- Los usuarios pueden iniciar sesión y cerrar sesión.
- El sistema incluye recuperación de contraseñas.

#### 3. Gestión de Productos
- Los administradores pueden crear, editar y eliminar productos.
- Los productos tienen los siguientes campos: ID, nombre, descripción, precio y stock.

#### 4. Catálogo de Productos
- Los usuarios pueden visualizar una lista de productos disponibles.
- Los productos pueden filtrarse por categorías o rangos de precios.

#### 5. Carrito de Compras
- Los usuarios pueden agregar productos a su carrito de compras.
- Los usuarios pueden ver y modificar el contenido del carrito (añadir o eliminar productos).

#### 6. Checkout
- Los usuarios pueden realizar compras de los productos en su carrito.
- Se ha integrado un sistema de pago simulado (sin necesidad de integración real).

#### 7. Panel de Administración
- Un panel exclusivo para administradores donde pueden gestionar usuarios y productos.

### 2. Requerimientos No Funcionales

#### 1. Usabilidad
- Interfaz de usuario intuitiva y fácil de navegar.
- Adaptada para dispositivos móviles.

#### 2. Rendimiento
- Las páginas deben cargarse en menos de 3 segundos.

#### 3. Seguridad
- Protegida contra ataques comunes como XSS, CSRF y SQL Injection.
- Implementación de HTTPS para conexiones seguras.

#### 4. Mantenibilidad
- Código bien documentado, organizado y siguiendo buenas prácticas de programación.

#### 5. Escalabilidad
- Capaz de manejar un crecimiento en el número de usuarios y productos sin comprometer el rendimiento.

### 3. Requisitos Técnicos

#### 1. Lenguaje de Programación
- Python 3.8 o superior.

#### 2. Framework
- Django 4.0 o superior.

#### 3. Base de Datos
- Microsoft SQL Server (local o remoto).
- Conector de base de datos: `pyodbc`.

## Instalación

### Requisitos Previos
- Python 3.8+
- Microsoft SQL Server
- Conector `pyodbc`

### Configuración del Proyecto

1. Clona el repositorio del proyecto:
   ```bash
   git clone https://github.com/tuusuario/proyecto-django-sqlserver.git
   cd proyecto-django-sqlserver

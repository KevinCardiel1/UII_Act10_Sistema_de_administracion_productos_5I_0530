from django.db import models

# Create your models here.
class producto(models.Model):
    CATEGORIAS = [
        (1, 'Peluches y Muñecos'),
        (2, 'Ropa y Vestuario Disney'),
        (3, 'Figuras Coleccionables'),
        (4, 'Juguetes y Juegos'),
        (5, 'Accesorios y Bolsos'),
        (6, 'Hogar Disney'),
        (7, 'Artículos de Parque (Parks)'),
        (8, 'Edición Limitada / Coleccionista'),
    ]


    PROVEEDORES = [
        (1000, 'Disney Store Official'),
        (2000, 'Disney Parks Merch'),
        (3000, 'Marvel Collection Supplier'),
        (4000, 'Pixar Merch Partner'),
        (5000, 'Star Wars Emporium'),
        (6000, 'Disney Licensing Partner'),
        (7000, 'Disney Outlet / Clearance'),
        (8000, 'Tienda Colaboraciones Especiales'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor_id = models.IntegerField(choices=PROVEEDORES, null=True, blank=True)
    categoria_id = models.IntegerField(choices=CATEGORIAS, null=True, blank=True)
    fecha_anadido = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'producto: {self.nombre} - ${self.precio}'

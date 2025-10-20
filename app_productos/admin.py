from django.contrib import admin
from .models import producto

@admin.register(producto)
class ProductoAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'precio', 'proveedor_id', 'categoria_id', 'fecha_anadido')
	search_fields = ('nombre', 'descripcion')
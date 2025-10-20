from django import forms
from .models import producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['nombre', 'descripcion', 'precio', 'proveedor_id', 'categoria_id']
        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'proveedor_id': 'ID del Proveedor',
            'categoria_id': 'ID de la Categoría',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'proveedor_id': forms.Select(attrs={'class': 'form-control'}),
            'categoria_id': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar choices para mostrar 'id - nombre'
        self.fields['proveedor_id'].choices = [
            (id, f"{id} - {label}") for id, label in self._meta.model.PROVEEDORES
        ]
        self.fields['categoria_id'].choices = [
            (id, f"{id} - {label}") for id, label in self._meta.model.CATEGORIAS
        ]
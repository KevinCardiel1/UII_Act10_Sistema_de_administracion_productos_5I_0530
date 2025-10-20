from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import producto
from .forms import ProductoForm

# Create your views here.
def index(request):
    return render(request, 'app_productos/index.html', {
        'productos': producto.objects.all()
        })

def ver_producto(request, id):
    product = producto.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def agregar(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            # Use ModelForm's save to handle new fields (proveedor_id, categoria_id)
            nuevo_producto = form.save()
            return render(request, 'app_productos/agregar.html', {
                'form': ProductoForm(),
                'success': True
            })
    else:
        form = ProductoForm()
    return render(request, 'app_productos/agregar.html', {
        'form': ProductoForm()
    })

def editar(request, id):
    if request.method == 'POST':
        product = producto.objects.get(pk=id)
        form = ProductoForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return render(request, 'app_productos/editar.html', {
                'form': form,
                'success': True
            })
    else:
        product = producto.objects.get(pk=id)
        form = ProductoForm(instance=product)
    return render(request, 'app_productos/editar.html', {
        'form': form,
        'success': False
    })

def eliminar(request, id):
  if request.method == 'POST':
    product = producto.objects.get(pk=id)
    product.delete()
  return HttpResponseRedirect(reverse('index'))
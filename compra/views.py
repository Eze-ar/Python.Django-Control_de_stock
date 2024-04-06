from django.shortcuts import render, redirect
from .models import Producto, Proveedor

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def crear_producto(request):
    proveedores = Proveedor.objects.all()  # Obtener todos los proveedores
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        proveedor_id = request.POST.get('proveedor')  # Obtener el ID del proveedor seleccionado
        stock_actual = request.POST.get('stock_actual')
        precio = request.POST.get('precio')
        proveedor = Proveedor.objects.get(id=proveedor_id)  # Obtener el proveedor por su ID
        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            stock_actual=stock_actual,
            proveedor=proveedor
        )
        return redirect('/')
    return render(request, 'nuevo_producto.html', {'proveedores': proveedores})

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')
        Proveedor.objects.create(
            nombre = nombre,
            apellido = apellido,
            dni = dni,
        )
        return redirect('listar_proveedores')
    return render(request, 'nuevo_proveedor.html')

from django.urls import path
from .views import crear_producto, listar_productos, listar_proveedores, agregar_proveedor

urlpatterns = [
    path('', listar_productos, name="listar_productos"),
    path('proveedores/listado/', listar_proveedores, name="listar_proveedores"),
    path('productos/nuevo/', crear_producto, name="crear_producto"),
    path('proveedores/nuevo/', agregar_proveedor, name="agregar_proveedor"),
]
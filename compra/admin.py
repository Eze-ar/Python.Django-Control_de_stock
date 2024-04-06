from django.contrib import admin
from .models import Producto, Proveedor

admin.site.register(Producto) #registro mi modelo Producto
admin.site.register(Proveedor) #registro mi modelo Proveedor
admin.site.site_header = 'Panel de Administrador'
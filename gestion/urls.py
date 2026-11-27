
from django.urls import path
from . import views

app_name = "gestion"

urlpatterns = [
    # CLIENTES
    path("clientes/", views.clientes, name="clientes"),
    path("clientes/nuevo/", views.cliente_nuevo, name="cliente_nuevo"),
    path(
        "clientes/<int:cliente_id>/editar/",
        views.cliente_editar,
        name="cliente_editar",
    ),
    path(
        "clientes/<int:cliente_id>/eliminar/",
        views.cliente_eliminar,
        name="cliente_eliminar",
    ),

    # PROVEEDORES
    path("proveedores/", views.proveedores, name="proveedores"),
    path("proveedores/nuevo/", views.proveedor_nuevo, name="proveedor_nuevo"),
    path(
        "proveedores/<int:proveedor_id>/editar/",
        views.proveedor_editar,
        name="proveedor_editar",
    ),
    path(
        "proveedores/<int:proveedor_id>/eliminar/",
        views.proveedor_eliminar,
        name="proveedor_eliminar",
    ),
]

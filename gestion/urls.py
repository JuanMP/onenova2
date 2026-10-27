from django.urls import path
from . import views

app_name = "gestion"

urlpatterns = [
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
]
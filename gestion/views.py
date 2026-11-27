
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Cliente, Proveedor


# ============================================================
# FORMULARIOS
# ============================================================

# Formulario para crear y editar clientes.
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "empresa", "email", "telefono"]

        # Aplicamos las clases visuales de Bootstrap.
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "empresa": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
        }


# Formulario para crear y editar proveedores.
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ["nombre", "empresa", "email", "telefono"]

        # Aplicamos las clases visuales de Bootstrap.
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "empresa": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
        }


# ============================================================
# CLIENTES
# ============================================================

# Mostramos todos los clientes registrados.
@login_required
def clientes(request):
    lista_clientes = Cliente.objects.order_by("-creado")

    return render(
        request,
        "gestion/clientes.html",
        {"clientes": lista_clientes},
    )


# Creamos un cliente nuevo.
@login_required
def cliente_nuevo(request):
    if request.method == "POST":
        formulario = ClienteForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("gestion:clientes")
    else:
        formulario = ClienteForm()

    return render(
        request,
        "gestion/cliente_formulario.html",
        {"formulario": formulario, "titulo": "Nuevo cliente"},
    )


# Editamos un cliente existente.
@login_required
def cliente_editar(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    if request.method == "POST":
        formulario = ClienteForm(request.POST, instance=cliente)

        if formulario.is_valid():
            formulario.save()
            return redirect("gestion:clientes")
    else:
        formulario = ClienteForm(instance=cliente)

    return render(
        request,
        "gestion/cliente_formulario.html",
        {"formulario": formulario, "titulo": "Editar cliente"},
    )


# Eliminamos un cliente después de confirmar.
@login_required
def cliente_eliminar(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    if request.method == "POST":
        cliente.delete()
        return redirect("gestion:clientes")

    return render(
        request,
        "gestion/cliente_eliminar.html",
        {"cliente": cliente},
    )


# ============================================================
# PROVEEDORES
# ============================================================

# Mostramos todos los proveedores registrados.
@login_required
def proveedores(request):
    lista_proveedores = Proveedor.objects.order_by("-creado")

    return render(
        request,
        "gestion/proveedores.html",
        {"proveedores": lista_proveedores},
    )


# Creamos un proveedor nuevo.
@login_required
def proveedor_nuevo(request):
    if request.method == "POST":
        formulario = ProveedorForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("gestion:proveedores")
    else:
        formulario = ProveedorForm()

    return render(
        request,
        "gestion/proveedor_formulario.html",
        {"formulario": formulario, "titulo": "Nuevo proveedor"},
    )


# Editamos un proveedor existente.
@login_required
def proveedor_editar(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)

    if request.method == "POST":
        formulario = ProveedorForm(request.POST, instance=proveedor)

        if formulario.is_valid():
            formulario.save()
            return redirect("gestion:proveedores")
    else:
        formulario = ProveedorForm(instance=proveedor)

    return render(
        request,
        "gestion/proveedor_formulario.html",
        {"formulario": formulario, "titulo": "Editar proveedor"},
    )


# Eliminamos un proveedor después de confirmar.
@login_required
def proveedor_eliminar(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, pk=proveedor_id)

    if request.method == "POST":
        proveedor.delete()
        return redirect("gestion:proveedores")

    return render(
        request,
        "gestion/proveedor_eliminar.html",
        {"proveedor": proveedor},
    )

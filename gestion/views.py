from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Cliente


# Formulario para crear y editar clientes.
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "empresa", "email", "telefono"]

    # Aplicamos las clases visuales de Bootstrap a los campos.
    widgets = {
        "nombre": forms.TextInput(attrs={"class": "form-control"}),
        "empresa": forms.TextInput(attrs={"class": "form-control"}),
        "email": forms.EmailInput(attrs={"class": "form-control"}),
        "telefono": forms.TextInput(attrs={"class": "form-control"}),
    }


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


# Eliminamos un cliente después de confirmar la acción.
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
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from gestion.models import Cliente, Proveedor, Producto, Documento

@login_required
def dashboard(request):
    # Los indicadores se calculan con los datos reales guardados en la base de datos.
    context = {
        "clientes_count": Cliente.objects.count(),
        "proveedores_count": Proveedor.objects.count(),
        "productos_count": Producto.objects.count(),
        "documentos_count": Documento.objects.count(),
        "documentos_recientes": Documento.objects.order_by("-creado")[:5],
    }
    return render(request, "core/dashboard.html", context)

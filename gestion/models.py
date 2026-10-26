from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=160)
    empresa = models.CharField(max_length=160, blank=True)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=40, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.empresa or self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=160)
    empresa = models.CharField(max_length=160, blank=True)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=40, blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.empresa or self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=160)
    referencia = models.CharField(max_length=80, blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    stock = models.PositiveIntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Documento(models.Model):
    class Tipo(models.TextChoices):
        FACTURA = "factura", "Factura"
        ALBARAN = "albaran", "Albarán"
        PRESUPUESTO = "presupuesto", "Presupuesto"
        OTRO = "otro", "Otro"

    class Estado(models.TextChoices):
        PENDIENTE = "pendiente", "Pendiente de revisar"
        REVISADO = "revisado", "Revisado"
        ARCHIVADO = "archivado", "Archivado"

    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=Tipo.choices, default=Tipo.OTRO)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)
    archivo = models.FileField(upload_to="documentos/", blank=True)
    notas = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

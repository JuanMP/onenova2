# OneNova

Aplicación web de gestión empresarial con una base preparada para incorporar automatización e IA local.

## Tecnologías
- Python y Django
- SQLite para desarrollo local
- Bootstrap 5 para una interfaz adaptable
- Django Admin para administrar los primeros registros

## Requisitos
- Python 3.10–3.13
- Conexión a Internet solo para instalar Django y cargar Bootstrap desde CDN

## Instalación en Windows (PowerShell)

```powershell
# 1. Entra en la carpeta del proyecto
cd ruta\a\onenova

# 2. Crea un entorno virtual aislado
python -m venv .venv

# 3. Actívalo
.\.venv\Scripts\Activate.ps1

# 4. Instala las dependencias
python -m pip install -r requirements.txt

# 5. Crea las tablas de la base de datos
python manage.py makemigrations gestion
python manage.py migrate

# 6. Crea un usuario administrador
python manage.py createsuperuser

# 7. Arranca la aplicación
python manage.py runserver
```

Abre http://127.0.0.1:8000/ para el panel y http://127.0.0.1:8000/admin/ para la administración.

## Estado actual
Primera base funcional: acceso con usuario, panel con contadores, modelos iniciales de clientes/proveedores/productos/documentos y administración de Django.

## Próximas fases
1. CRUD propio para clientes, proveedores, productos y documentos.
2. Subida y descarga segura de archivos.
3. Búsqueda, filtros y estados de revisión.
4. OCR local con Tesseract.
5. Asistente con modelo local mediante Ollama.
6. Permisos por roles, pruebas y auditoría.

## Seguridad
Esta versión es solo para desarrollo local. Antes de publicar en Internet hay que cambiar `SECRET_KEY`, configurar `DEBUG=False`, `ALLOWED_HOSTS`, HTTPS, permisos y almacenamiento de documentos. No cargues datos reales o sensibles en esta versión inicial.

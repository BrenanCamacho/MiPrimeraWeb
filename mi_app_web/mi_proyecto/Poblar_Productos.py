from mi_app.models import Producto
from django.db import connection

# Eliminar todos los productos
Producto.objects.all().delete()

# Reiniciar el ID autoincremental (solo en SQLite)
with connection.cursor() as cursor:
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='mi_app_producto';")

# Crear nuevos productos
Producto.objects.create(nombre="Arroz", descripcion="Arroz de 1kg", precio=130, disponible=True)
Producto.objects.create(nombre="Aceite", descripcion="Aceite de 900ml", precio=350, disponible=True)
Producto.objects.create(nombre="Mantequilla", descripcion="Mantequilla 250mg", precio=150, disponible=False)

print("Productos reiniciados y agregados.")
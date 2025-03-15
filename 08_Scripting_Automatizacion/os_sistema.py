#---------- Automatización de Archivos ----------
import os

#(Listar Archivos):
print("Archivos en el directorio actual:", os.listdir())

#(Crear Directorio):
directorio = "nuevo_directorio"
if not os.path.exists(directorio):
    os.mkdir(directorio)
    print(f"Directorio '{directorio}' creado.")

#(Crear y Eliminar):
archivo = "archivo_temporal.txt"
with open(archivo, "w") as f:
    f.write("Este es un archivo temporal.")

print(f"Archivo '{archivo}' creado.")

#(Eliminar):
if os.path.exists(archivo):
    os.remove(archivo)
    print(f"Archivo '{archivo}' eliminado.")

#(Sistema):
usuario = os.getenv("USER") or os.getenv("USERNAME")
print(f"Usuario actual: {usuario}")
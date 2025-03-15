#---------- Automatización de Consola ----------
import sys

#(Leer Argumentos):
if len(sys.argv) > 1:
    print(f"Argumentos recibidos: {sys.argv[1:]}")
else:
    print("No se recibieron argumentos.")

#(Forzar Salida):
if len(sys.argv) < 2:
    print("Error: Se necesita al menos un argumento.")
    sys.exit(1)
print("El script continúa ejecutándose...")

#(Cambiar Salida):
sys.stdout = open("salida.txt", "w")  
print("Este texto se guardará en salida.txt")
sys.stdout.close()
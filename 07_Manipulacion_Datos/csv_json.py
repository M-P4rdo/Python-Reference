#---------- CSV ----------
import csv

#(Leer):
with open("datos.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

#(Escribir):
datos = [["Nombre", "Edad"], ["Ana", 25], ["Juan", 30]]
with open("nuevo.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)

#---------- Json  ----------
import json

#(Leer):
with open("datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    print(datos)

#(Escribir):
datos = {"nombre": "Juan", "edad": 30, "activo": True}
json_str = json.dumps(datos)
print("JSON:", json_str)

#(Diccionario en Json):
datos = {"Nombre": "Ana", "Edad": 25}
with open("salida.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=4)
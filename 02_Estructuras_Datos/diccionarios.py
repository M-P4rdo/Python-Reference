#---------- Diccionario ----------
diccionario = { "Nombre": "Miguel", "Apellido": "Pardo", "Edad": 20}

diccionario["Cumpleaños"] = "15 Mayo" #Agregar
diccionario["Nombre"] = "Angel"

print(diccionario["Edad"])
print(diccionario)

print(diccionario.get("Edad"))
print("Claves:", diccionario.keys()) #Claves
print("Valores:", diccionario.values()) #Valores

for clave, valor in diccionario.items(): #Recorrer
    print(f"{clave} : {valor}")

del diccionario["Cumpleaños"] #Eliminar

#(Diccionario Con Listas):
x2 ={"Dia":["Lunes", "Martes", "Miercoles"], "Año" : ["2021", "2022", "2023"]}
print(x2["Año"][1])

#(Diccionario Multidimensional):
informacion = {
    "Clave1" : {"Nombre": "Thomas", "Apellido": "Gil", "Edad": 22},
    "Clave2" : {"Nombre": "Daniel", "Apellido": "Pardo", "Edad": 20},
    "Clave3" : {"Nombre": "Maicol", "Apellido": "Torres", "Edad": 21}
}

informacion["Clave4"] = {"Nombre": "Isabella", "Apellido": "Gallego", "Edad": 19} #Añadir
informacion["Clave3"]["Apellido"] = "Macondo"
print(informacion["Clave2"]["Apellido"])
print(informacion)

for clave, valor in informacion.items(): #Recorrer
    print(clave, end=" ")
    for info in valor.items():
        print(f"{info}", end=" ")
    print()

del informacion["Clave3"] #Eliminar
del informacion["Clave4"]["Nombre"]


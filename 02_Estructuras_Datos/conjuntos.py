# ---------- Conjunto  ----------
conjunto1 = {"Miguel", "Pardo", 20}
conjunto2 = {"Pardo", 30, "15 Mayo"}

conjunto1.add("15 Mayo") #Agregar
print(conjunto1)
for valor in conjunto1: #Recorrer
    print(valor)
conjunto2.discard("15 Mayo") #Eliminar

union_conjuntos = conjunto1.union(conjunto2) #Unir
print("Unión:", union_conjuntos)

interseccion_conjuntos = conjunto1.intersection(conjunto2) #Interseccion
print("Intersección:", interseccion_conjuntos)

diferencia_conjuntos = conjunto1.difference(conjunto2) #Diferencias
print("Diferencia (conjunto1 - conjunto2):", diferencia_conjuntos)
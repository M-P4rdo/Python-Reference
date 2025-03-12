#---------- Tupla  ----------
tupla = ("Miguel", "Pardo", 20)

print(tupla[2])
for i, valor in enumerate(tupla): #Recorrer
    print(f"Índice {i}: {valor}")

nombre, apellido, edad = tupla #Desempaquetado
print(nombre); print(apellido); print(edad)

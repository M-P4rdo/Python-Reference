#---------- Lista ----------
lista = [1, 2, 3, "Python", True]
lista_numerica = list(range(0, 5))

lista.append(6) #Agregar
lista.insert(2, "Si")
lista[3] = "x2" 

print(lista[0:6])
lista_numerica.sort(reverse=True) #Organiza
lista.reverse() #Invierte Orden
print(lista)
for item in lista: #Recorrer
    print(item)

lista.remove("Si") #Eliminar
lista.pop(0) #Eliminar por Posicion
lista_numerica.extend(lista) #Unir Listas
print(lista_numerica)

#(Lista Con Diccionarios):
x1 = [{"Dia": "Lunes", "Mes" : "Abril"},{"Dia": "Jueves", "Mes" : "Junio"}]
print(x1[0]["Dia"])

#(Lista Multidimensional):
contactos = [['Luis', 'luis@mail.com'], ['Thomas', 'thomas@mail.com'],
              ['Miguel', 'miguel@mail.com']]

contactos.append(['Heider', 'heider@mail.com']) #Añadir
contactos[2][0] = 'Angel'
print(f"Nombre: {contactos[1][0]}")
print(f"Correo: {contactos[1][1]}")
print(contactos)

for contacto in contactos: #Recorrer
    for elemento in contacto:
        print(elemento, end=" ")

del contactos[0] #Eliminar
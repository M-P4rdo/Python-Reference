#---------- Tipos de Datos ----------
t0 = 'a'
t1 = "Texto" #Cadena de Texto (string)

t2 = 2 #Entero (int)
t3 = 10/4 #Flotante (float)

t4 = True #Booleano (bool)
t5 = None #Vacio

t6 = 3 +2j #Complejo (complex)
t7 = range(5) #Rango = (0, 1, 2, 3, 4)

t8 = [1, 2, 3, 4, 5] #Lista (list)
t9 = (10.5, 20.3) #Tupla (tuple)
t10 = {"manzana", "pera", "uva"} #Colección (set)
t11 = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"} #Diccionario (dict)

print(type(t6)) #Tipo de dato

#---------- Concatenacion ----------
#(Numeros):
print(t1 + " " + t0 + f" {t3} {t4} {t5}")
print(f"Los Numeros son {t2}, {t3}, {t6}")
print("Los Numeros son {}, {}, {}".format(t2, t3, t6))

#(Texto):
print(t1 + " de prueba")
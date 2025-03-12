#---------- Asignacion de Variables ----------
#(Obtener Datos):
db = input("Ingresa un texto: ")

#(Basicos):
nombre = "Juan"
edad = 25
altura = 1.75
suma = 0; resta = 0; divi = 0; multi = 0; sobrante = 0

#(Multiple):
a, b, c = 1, 2, 3
nombre, edad = "Juan", 25

#(Mismo Valor):
x = y = z = 5

#---------- Conversion de Datos ---------- 
d1 = int("2")
d2 = float("2")
d3 = str([1,2,3])
d4 = bool(0)
d5 = list("Texto")
d6 = tuple([1,2,3])
d7 = set([1,1,2,3,3])
d8 = dict([("nombre", "Juan"), ("edad", 25)])
print(f"{d1}\n{d2}\n{d3}\n{d4}\n{d5}\n{d6}\n{d7}\n{d8}\n")
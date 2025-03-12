#---------- Lambda ----------
#(Suma):
suma = lambda a, b: a + b
print(suma(5, 3))

#(Mayor):
mayor = lambda x, y: x if x > y else y
print(mayor(10, 20))

#(Ordenar):
pares = [(1, 3), (4, 2), (6, 5)]
pares.sort(key=lambda x: x[1])
print(pares)
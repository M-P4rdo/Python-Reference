#---------- Filtrado de Datos ----------
#(Map):
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda x: (x * 9/5) + 32, celsius))
print(fahrenheit)

#(Filter):
palabras = ["python", "es", "genial", "para", "todos"]
cortas = list(filter(lambda palabra: len(palabra) <= 3, palabras))
print(cortas)

#(Reduce):
from functools import reduce

numeros = [1, 2, 3, 4, 5]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)

#---------- Estructuras Avanzadas ----------
#(Doble Cola):
from collections import deque

mi_deque = deque([1, 2, 3])
mi_deque.appendleft(0)  #Inserta Inicio
mi_deque.append(4)
print(mi_deque)

mi_deque.pop()  #Elimina del Final

#(Diccionario Predeterminado):
from collections import defaultdict

mi_defaultdict = defaultdict(int)  #Valores por Defecto
mi_defaultdict["a"] += 1  
print(mi_defaultdict["a"])  

#(Contador):
from collections import Counter

contador = Counter("banana")
print(contador)  #{'b': 1, 'a': 3, 'n': 2}

#---------- List Comprehension ----------
cuadrados = [x**2 for x in range(5)]
print(cuadrados)

palabras = ["hola", "mundo", "python"]
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)

#(Doble For):
combinaciones = [(x, y) for x in range(3) for y in range(2)]
print(combinaciones)
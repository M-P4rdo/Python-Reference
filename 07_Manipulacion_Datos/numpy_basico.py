#---------- Numpy ----------
#pip install numpy
import numpy as np

#(Crear Array):
arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)

#(Matriz):
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)

#(Datos Aleatorios):
aleatorios = np.random.randint(0, 100, (3, 3))
print(aleatorios)
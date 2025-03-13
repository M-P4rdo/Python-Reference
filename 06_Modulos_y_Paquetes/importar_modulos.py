#---------- Importar Módulo ----------
import modulos

#(Funciones del Módulo):
print(f"Suma: {modulos.suma(10, 5)}")
print(f"Resta: {modulos.resta(10, 5)}")
print(f"Multiplicación: {modulos.multiplicacion(10, 5)}")
print(f"División: {modulos.division(10, 5)}")

#(Variable del Módulo):
print(f"Valor de PI: {modulos.PI}")

#(Funciones Especificas):
from modulos import suma, division

print(suma(20, 10))
print(division(10, 2))

#(Alias):
import modulos as op

print(op.suma(5, 3))  # 8
print(op.PI)

#---------- Importar Paquete ----------
import crear_paquetes as cp

print(cp.sumar(10, 5))  # 15
print(cp.potencia(2, 3))
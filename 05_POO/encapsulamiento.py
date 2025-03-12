#---------- Encampsulamiento ----------
#(Atributo Privado):
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad

    def obtener_nombre(self):
        return self.__nombre  # Accediendo a un atributo privado

p = Persona("Juan", 25)
print(p.obtener_nombre())

#(Getter y Setter):
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo

c = CuentaBancaria(1000)
c.set_saldo(2000)
print(c.get_saldo())

#(Protegido):
class Vehiculo:
    def __init__(self, marca):
        self._marca = marca

v = Vehiculo("Toyota")
print(v._marca)
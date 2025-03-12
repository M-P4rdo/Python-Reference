#---------- Clase Abstracta ----------
#(Método Obligatorio):
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

p = Perro()
g = Gato()
print(p.hacer_sonido()) 
print(g.hacer_sonido())

#(Método Implementado):
class Figura(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    def descripcion(self):
        return f"Esta figura es de color {self.color}"

class Circulo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2

c = Circulo(5, "rojo")
print(c.area())  
print(c.descripcion())

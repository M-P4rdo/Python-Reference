#---------- Herencia ----------
#(Clase Padre):
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"

p = Perro("Rex")
print(p.nombre)
print(p.hacer_sonido())

#(Reutilizar Constructor):
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color

g = Gato("Whiskers", "Blanco")
print(g.nombre, g.color)

#(Herencia Múltiple):
class Animal:
    def __init__(self, patas, raza):
        self.patas = patas
        self.raza = raza

    def comer(self):
        print(f"El {self.raza} esta Comiendo...")

class Habitad:
    def __init__(self, zona, estacion):
        self.zona = zona
        self.estacion = estacion

    def cambiar_estacion(self, nueva_estacion):
        self.estacion = nueva_estacion.lower()
        print(f"El Clima ahora es {nueva_estacion}")

class AnimalenHabitad(Animal, Habitad):
    def __init__(self, patas, raza, zona, estacion, nombre, edad):
        Animal.__init__(self, patas, raza)
        Habitad.__init__(self, zona, estacion)
        self.nombre = nombre
        self.edad  = edad

    def hibernar(self):
        if self.estacion == "invierno":
            print("Hibernando")
        else:
            print("No esta en estacion de Hibernar")

    def cazar(self):
        print("Cazando..")
        print(super().comer())

animal = AnimalenHabitad(4, 'Tigre', 'Sabana', 'Verano', 'Trinitty', 15)
animal.hibernar()
animal.cambiar_estacion('invierno')
animal.hibernar()
animal.cazar()
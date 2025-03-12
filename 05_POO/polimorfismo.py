#---------- Polimosfirmo ----------
#(Diferentes Clases):
class Perro:
    def sonido(self):
        return "Guau!"

class Gato:
    def sonido(self):
        return "Miau!"

animales = [Perro(), Gato()]

for animal in animales:
    print(animal.sonido())

#(Con Herencia):
class Ave:
    def volar(self):
        return "Vuelo bajo"

class Aguila(Ave):
    def volar(self):
        return "Vuelo alto"

aves = [Ave(), Aguila()]
for ave in aves:
    print(ave.volar())

#(Con Funciones):
def hacer_sonido(animal):
    return animal.sonido()

print(hacer_sonido(Perro()))  # Guau!
print(hacer_sonido(Gato()))
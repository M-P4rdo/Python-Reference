#---------- Metodos Especiales ----------
#(__str__):
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona({self.nombre}, {self.edad} años)"

p = Persona("Juan", 30)
print(p)

#(__len__):
class Grupo:
    def __init__(self, miembros):
        self.miembros = miembros

    def __len__(self):
        return len(self.miembros)

g = Grupo(["Ana", "Luis", "Pedro"])
print(len(g))

#(__eq__):
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.edad == otro.edad

p1 = Persona("Juan", 25)
p2 = Persona("Juan", 25)
print(p1 == p2)
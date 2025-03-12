#---------- Clases ----------
#(Definir):
class Persona:
    trabajo = "Obrero" #Atributo de Clase
    def __init__(self, nombre, edad):
        self.nombre = nombre #Atributo de instancia
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

#(Instanciación):
p1 = Persona("Juan", 25)
print(p1.saludar())
print(p1.trabajo)

#(Atributos):
p1.edad = 30
print(p1.edad)

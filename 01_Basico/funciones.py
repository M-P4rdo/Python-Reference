#---------- Funciónes ----------
#(Simples):
def saludar_s():
    print("¡Hola, bienvenido!")

#(Con Parámetros):
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

#(Con Retorno):
def suma(a, b):
    return a + b

#(Valores Predeterminados):
def presentar(nombre="Desconocido"):
    print(f"Hola, soy {nombre}.")

#(Con *Args (Argumentos Variables Posicionales)):
def sumar_todo(*numeros):
    return sum(numeros)

#(Con **Kwargs (Argumentos Variables con Nombre)):
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

#(Anidados):
def exterior():
    def interior():
        print("Soy la función interior")
    interior()

#(Retorna Multiples Valores):
def calcular(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

#(Devuelve Otras Funciones):
def operacion(tipo):
    if tipo == "suma":
        return lambda a, b: a + b
    elif tipo == "multiplicacion":
        return lambda a, b: a * b

#---------- Llamar las Funciónes ----------
saludar_s() #Simples
saludar("Carlos") #Parametro
print(suma(5, 3)) #Retorno
presentar() #Valor Predeterminado
presentar("Ana") #Valor Predeterminado
print(sumar_todo(1, 2, 3, 4, 5)) #*Args
mostrar_info(nombre="Luis", edad=30) #*Kwargs
exterior() #Anidado
suma_1, resta_1 = calcular(5, 3) #Devuelve Multiples Valores
print(suma_1, resta_1)
sumar = operacion("suma") #Devuelve Otra Funcion 
print(sumar(5, 3))

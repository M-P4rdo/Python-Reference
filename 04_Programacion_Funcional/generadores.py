#---------- Generador ----------
#(Números Impares)
def impares(n):
    for i in range(n):
        if i % 2 != 0:
            yield i

gen = impares(10)
print(list(gen))

#(Infinito de Fibonacci):
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for _ in range(5):
    print(next(gen))

#(Archivo Línea por Línea):
def leer_lineas(archivo):
    with open(archivo, 'r') as f:
        for linea in f:
            yield linea.strip()

# for linea in leer_lineas("archivo.txt"):
#     print(linea)
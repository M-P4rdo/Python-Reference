#---------- Decorador ----------
#(Imprimir Antes):
def decorador(func):
    def wrapper():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")
    return wrapper

@decorador
def saludo():
    print("Hola, mundo!")

#(Verificar Permiso):
def verificar_permiso(func):
    def wrapper(usuario):
        if usuario == "admin":
            return func()
        else:
            print("Acceso denegado")
    return wrapper

@verificar_permiso
def panel_admin():
    print("Bienvenido al panel de administración")

#(Con Argumentos):
def repetir(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorador

@repetir(3)
def hola():
    print("Hola!")

#---------- Llamar las Funciónes ----------
saludo()
panel_admin("admin")
panel_admin("user")
hola()
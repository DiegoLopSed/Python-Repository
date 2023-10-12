class MiClase:
    def __init__(self):
        self.atributo1 = None
        self.atributo2 = None
        self.atributo3 = None
        self.atributo4 = None

    def insertar_valores_desde_teclado(self):
        self.atributo1 = input("Ingrese el valor para atributo1: ")
        self.atributo2 = input("Ingrese el valor para atributo2: ")
        self.atributo3 = input("Ingrese el valor para atributo3: ")
        self.atributo4 = input("Ingrese el valor para atributo4: ")

# Crear un objeto de la clase MiClase
objeto = MiClase()

# Insertar valores desde el teclado
objeto.insertar_valores_desde_teclado()

# Acceder a los atributos
print("Atributo 1:", objeto.atributo1)
print("Atributo 2:", objeto.atributo2)
print("Atributo 3:", objeto.atributo3)
print("Atributo 4:", objeto.atributo4)

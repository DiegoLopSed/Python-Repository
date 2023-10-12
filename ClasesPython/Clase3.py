class MiClase:
    def __init__(self, atributo1, atributo2, atributo3, atributo4):
        self.atributo1 = atributo1
        self.atributo2 = atributo2
        self.atributo3 = atributo3
        self.atributo4 = atributo4

    @classmethod
    def crear_objeto_desde_teclado(cls):
        atributo1 = input("Ingrese el valor para atributo1: ")
        atributo2 = input("Ingrese el valor para atributo2: ")
        atributo3 = input("Ingrese el valor para atributo3: ")
        atributo4 = input("Ingrese el valor para atributo4: ")
        return cls(atributo1, atributo2, atributo3, atributo4)

# Solicitar al usuario la cantidad de objetos a crear
num_objetos = int(input("Ingrese la cantidad de objetos a crear: "))

# Crear y registrar los atributos de los objetos
objetos = []
for _ in range(num_objetos):
    objeto = MiClase.crear_objeto_desde_teclado()
    objetos.append(objeto)

# Mostrar los atributos de los objetos
for i, objeto in enumerate(objetos, 1):
    print(f"Objeto {i}:")
    print("Atributo 1:", objeto.atributo1)
    print("Atributo 2:", objeto.atributo2)
    print("Atributo 3:", objeto.atributo3)
    print("Atributo 4:", objeto.atributo4)

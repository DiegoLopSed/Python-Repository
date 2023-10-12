class MiClase:
    def __init__(self, atributo1, atributo2, atributo3, atributo4):
        self.atributo1 = atributo1
        self.atributo2 = atributo2
        self.atributo3 = atributo3
        self.atributo4 = atributo4

# Crear tres objetos de la clase MiClase
objeto1 = MiClase("Valor1", 42, True, 3.14)
objeto2 = MiClase("OtroValor", 123, False, 2.71)
objeto3 = MiClase("Ejemplo", 999, True, 1.618)

# Acceder a los atributos de los objetos
print("Objeto 1:")
print(objeto1.atributo1)
print(objeto1.atributo2)
print(objeto1.atributo3)
print(objeto1.atributo4)

print("Objeto 2:")
print(objeto2.atributo1)
print(objeto2.atributo2)
print(objeto2.atributo3)
print(objeto2.atributo4)

print("Objeto 3:")
print(objeto3.atributo1)
print(objeto3.atributo2)
print(objeto3.atributo3)
print(objeto3.atributo4)

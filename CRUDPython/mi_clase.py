objetos = []

class MiClase:
    def __init__(self, numero_de_parte, clasificacion, marca, categoria, subcategoria,
                 compatibilidad, posicion, nombre_producto, costo_fabrica, precio_venta, descripcion, origen):
        self.numero_de_parte = numero_de_parte
        self.clasificacion = clasificacion
        self.marca = marca
        self.categoria = categoria
        self.subcategoria = subcategoria
        self.compatibilidad = compatibilidad
        self.posicion = posicion
        self.nombre_producto = nombre_producto
        self.costo_fabrica = costo_fabrica
        self.precio_venta = precio_venta
        self.descripcion = descripcion
        self.origen = origen

    @classmethod
    def crear_objeto_desde_teclado(cls):
        numero_de_parte = input("Ingrese el número de parte: ")
        clasificacion = input("Ingrese la clasificación: ")
        marca = input("Ingrese la marca: ")
        categoria = input("Ingrese la categoría: ")
        subcategoria = input("Ingrese la subcategoría: ")
        compatibilidad = input("Ingrese la compatibilidad: ")
        posicion = input("Ingrese la posición: ")
        nombre_producto = input("Ingrese el nombre del producto: ")
        costo_fabrica = input("Ingrese el costo de fábrica: ")
        precio_venta = input("Ingrese el precio de venta: ")
        descripcion = input("Ingrese la descripción: ")
        origen = input("Ingrese el origen: ")

        return cls(numero_de_parte, clasificacion, marca, categoria, subcategoria,
                   compatibilidad, posicion, nombre_producto, costo_fabrica, precio_venta, descripcion, origen)
    

objeto1 = MiClase(
    numero_de_parte="12345",
    clasificacion="Clase A",
    marca="Marca X",
    categoria="Categoría 1",
    subcategoria="Subcategoría 1",
    compatibilidad="Compatibilidad 1",
    posicion="Posición 1",
    nombre_producto="Producto 1",
    costo_fabrica="100.00",
    precio_venta="150.00",
    descripcion="Descripción 1",
    origen="Origen 1"
)

objeto2 = MiClase(
    numero_de_parte="67890",
    clasificacion="Clase B",
    marca="Marca Y",
    categoria="Categoría 2",
    subcategoria="Subcategoría 2",
    compatibilidad="Compatibilidad 2",
    posicion="Posición 2",
    nombre_producto="Producto 2",
    costo_fabrica="80.00",
    precio_venta="120.00",
    descripcion="Descripción 2",
    origen="Origen 2"
)

objetos = [objeto1, objeto2]
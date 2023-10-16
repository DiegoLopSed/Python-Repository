class Partes:
    def __init__(self, num_parte, clasificacion, marca, categoria, subcategoria, compatibilidad, posicion, nombre_producto, costo_fabrica, precio_venta, descripcion, origen):
        self.num_parte = num_parte
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

        
# Crear objeto 1
producto1 = Partes(
    num_parte="001",
    clasificacion="Electrónica",
    marca="Sony",
    categoria="Televisores",
    subcategoria="LED",
    compatibilidad="1080p",
    posicion="Sala de estar",
    nombre_producto="Televisor LED de 55 pulgadas",
    costo_fabrica=500,
    precio_venta=799.99,
    descripcion="Televisor LED de alta definición de 55 pulgadas.",
    origen="China"
)

# Crear objeto 2
producto2 = Partes(
    num_parte="002",
    clasificacion="Electrodomésticos",
    marca="Samsung",
    categoria="Lavadoras",
    subcategoria="Carga frontal",
    compatibilidad="7 kg",
    posicion="Cocina",
    nombre_producto="Lavadora de carga frontal",
    costo_fabrica=400,
    precio_venta=599.99,
    descripcion="Lavadora de carga frontal de 7 kg de capacidad.",
    origen="Corea del Sur"
)

# Crear objeto 3
producto3 = Partes(
    num_parte="003",
    clasificacion="Electrónica",
    marca="Apple",
    categoria="Smartphones",
    subcategoria="iOS",
    compatibilidad="iPhone 13",
    posicion="Bolsillo",
    nombre_producto="iPhone 13 Pro",
    costo_fabrica=800,
    precio_venta=1199.99,
    descripcion="Último modelo de iPhone con características avanzadas.",
    origen="Estados Unidos"
)

productos = [producto1, producto2, producto3]

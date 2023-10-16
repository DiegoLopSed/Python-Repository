from mi_clase import Partes,productos
class GestorDeObjetos:

    @staticmethod
    def mostrar_productos(productos):
        for producto in productos:
            print("Número de parte:", producto.num_parte)
            print("Clasificación:", producto.clasificacion)
            print("Marca:", producto.marca)
            print("Categoría:", producto.categoria)
            print("Subcategoría:", producto.subcategoria)
            print("Compatibilidad:", producto.compatibilidad)
            print("Posición:", producto.posicion)
            print("Nombre del producto:", producto.nombre_producto)
            print("Costo de fábrica:", producto.costo_fabrica)
            print("Precio de venta:", producto.precio_venta)
            print("Descripción:", producto.descripcion)
            print("Origen:", producto.origen)
            print("\n")

    def insertar_producto(self):
        num_parte = input("Número de parte: ")
        clasificacion = input("Clasificación: ")
        marca = input("Marca: ")
        categoria = input("Categoría: ")
        subcategoria = input("Subcategoría: ")
        compatibilidad = input("Compatibilidad: ")
        posicion = input("Posición: ")
        nombre_producto = input("Nombre del producto: ")
        costo_fabrica = float(input("Costo de fábrica: "))
        precio_venta = float(input("Precio de venta: "))
        descripcion = input("Descripción: ")
        origen = input("Origen: ")

        producto = Partes(num_parte, clasificacion, marca, categoria, subcategoria, compatibilidad, posicion, nombre_producto, costo_fabrica, precio_venta, descripcion, origen)
        productos.append(producto)

    def buscar_producto(self, num_parte):
        for producto in productos:
            if producto.num_parte == num_parte:
                return producto
        return None
    
    
    def eliminar_producto(self, num_parte):
        for producto in productos:
            if producto.num_parte == num_parte:
                productos.remove(producto)
                return

    def actualizar_producto(self, num_parte):
        producto = self.buscar_producto(num_parte)
        if producto:
            print("Producto encontrado. Ingrese los nuevos datos:")
            producto.num_parte = input("Nuevo número de parte: ")
            producto.clasificacion = input("Nueva clasificación: ")
            producto.marca = input("Nueva marca: ")
            producto.categoria = input("Nueva categoría: ")
            producto.subcategoria = input("Nueva subcategoría: ")
            producto.compatibilidad = input("Nueva compatibilidad: ")
            producto.posicion = input("Nueva posición: ")
            producto.nombre_producto = input("Nuevo nombre del producto: ")
            producto.costo_fabrica = float(input("Nuevo costo de fábrica: "))
            producto.precio_venta = float(input("Nuevo precio de venta: "))
            producto.descripcion = input("Nueva descripción: ")
            producto.origen = input("Nuevo origen: ")
            print("Producto actualizado con éxito.")
        else:
            print("Producto no encontrado. No se puede actualizar.")
import os
from mi_clase import Partes, productos
from clase_gestor import GestorDeObjetos

# Ejemplo de uso
manager = GestorDeObjetos()

while True:
    print("Opciones:")
    print("1. Insertar un producto")
    print("2. Buscar producto por número de parte")
    print("3. Mostrar todos los productos")
    print("4. Actualizar producto por número de parte")
    print("5. Eliminar producto por número de parte")
    print("6. Limpiar pantalla")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        manager.insertar_producto()

    elif opcion == "2":
        num_parte = input("Ingrese el número de parte a buscar: ")
        producto_buscado = manager.buscar_producto(num_parte)
        if producto_buscado:
            print("Producto encontrado:")
            print("Número de parte:", producto_buscado.num_parte)
            # Mostrar otros atributos aquí
        else:
            print("Producto no encontrado.")

    elif opcion == "3":
        manager.mostrar_productos(productos)

    elif opcion == "4":

        num_parte_a_eliminar = input("Ingrese el número de parte a eliminar: ")
        producto_eliminado = manager.eliminar_producto(num_parte_a_eliminar)
        if producto_eliminado:
            print("Producto eliminado con éxito.")
        else:
            print("No se encontró el producto para eliminar.")
    elif opcion == "5":
        num_parte_a_eliminar = input("Ingrese el número de parte a eliminar: ")
        manager.eliminar_producto(num_parte_a_eliminar)

    elif opcion == "6":
        os.system('cls')
        
    elif opcion == "7":
        break
    else:
        print("Opción no válida. Intente de nuevo.")
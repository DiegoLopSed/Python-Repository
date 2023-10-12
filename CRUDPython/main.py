import os
from mi_clase import MiClase, objetos
from metodos_mi_clase import buscar_objeto_por_numero_de_parte, eliminar_objeto_por_numero_de_parte


while True:

    
    # Mostrar un menú de selección
    print("\nMenú de selección:")
    print("1. Agregar objeto")
    print("2. Mostrar objetos")
    print("3. Buscar objeto por número de parte")
    print("4. Eliminar objeto por número de parte")
    print("5. Limpiar consola")
    print("6. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5/6): ")
    

    if opcion == "1":
        # Agregar objeto
        objeto = MiClase.crear_objeto_desde_teclado()
        objetos.append(objeto)
        print("Objeto agregado.")

    elif opcion == "2":
        # Mostrar los atributos de los objetos
        for i, objeto in enumerate(objetos, 1):
            print(f"Objeto {i}:")
            print("Número de parte:", objeto.numero_de_parte)
            print("Clasificación:", objeto.clasificacion)
            print("Marca:", objeto.marca)

    elif opcion == "3":
        # Buscar objeto por número de parte
        numero_buscar = input("Ingrese el número de parte a buscar: ")
        objeto_encontrado = buscar_objeto_por_numero_de_parte(objetos, numero_buscar)
        if objeto_encontrado:
            print("Objeto encontrado:")
            print("Número de parte:", objeto_encontrado.numero_de_parte)
            print("Descripción:", objeto_encontrado.descripcion)
        else:
            print("Objeto no encontrado.")

    elif opcion == "4":
        # Eliminar objeto por número de parte
        numero_eliminar = input("Ingrese el número de parte a eliminar: ")
        eliminar_objeto_por_numero_de_parte(objetos, numero_eliminar)
        print(f"Objeto {numero_eliminar} eliminado.")

    elif opcion == "5":
        os.system('cls')

    elif opcion == "6":
        break

    else:
        print("Opción no válida. Intente de nuevo.")

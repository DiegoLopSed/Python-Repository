
from mi_clase import MiClase


def buscar_objeto_por_numero_de_parte(objetos, numero_de_parte):
    for objeto in objetos:
        if objeto.numero_de_parte == numero_de_parte:
            return objeto
    return None

def eliminar_objeto_por_numero_de_parte(objetos, numero_de_parte):
    objeto = buscar_objeto_por_numero_de_parte(objetos, numero_de_parte)
    if objeto is not None:
        objetos.remove(objeto)

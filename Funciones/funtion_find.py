'''
Conoceremos la función .find() dentro de python 
la cual nos permite buscar dentro de una cadena de texto
información especifica o solicitada.
'''

#? Palabra a buscar
searching = "videojuegos"
searching2 = "gaming"
#? Texto de donde buscar
text1 = "EL mundo de los videojuegos esta más desarollado gracias al crecimiento de la comunidad gamer"

#!Asignamos la busqueda a una variable y si el resultado existe nos arrojara como valor el espacio de caracter donde inicia
found = text1.find(searching)
print(found)
#!Asignamos la busqueda a una variable y si el resultado no existe nos arrojara como valor -1
found = text1.find(searching2)
print(found)


# Comentario de una línea
# Estos comentarios se utilizan para agregar explicaciones en el código

"""
Comentario de varias líneas
Puedes usar comillas triples para comentarios de varias líneas.
Estos son útiles para documentar funciones y clases.
"""

# Variables y tipos de datos básicos
numero = 42             # Entero
decimal = 3.14          # Punto flotante (número decimal)
texto = "Hola, mundo"   # Cadena de texto
booleano = True         # Valor booleano (True o False)

print("Numero: ",numero) #Concatenar los valores asignados
print("Decimal: ",decimal) #Concatenar los valores asignados
print("Texto: ",texto) #Concatenar los valores asignados
print("Booleano: ",booleano) #Concatenar los valores asignados

# Operaciones aritméticas
suma = 2 + 3
resta = 5 - 1
multiplicacion = 4 * 6
division = 8 / 2
modulo = 10 % 3  # Devuelve el resto de la división (2)

#Mostrar operaciones aritméticas
print("Suma: ",suma) 
print("Resta: ",resta) 
print("Multiplicación: ",multiplicacion) 
print("División: ",division) 
print("Modulo: ",modulo) 

# Listas
mi_lista = [1, 2, 3, 4, 5]
elemento = mi_lista[0]  # Acceder al primer elemento de la lista
mi_lista.append(6)      # Agregar un elemento al final de la lista
mi_lista.remove(3)     # Eliminar un elemento de la lista

print(mi_lista) #Mostrar mi lista asignada

# Condicionales
if booleano:
    print("La variable booleano es verdadera")
else:
    print("La variable booleano es falsa")

# Bucles
print("Bucle del 0 al 4")
for i in range(5):

    print(i)  # Imprime los números del 0 al 4

print("Bucle condicional de la variable numero, Numero=",numero)
while numero > 0:
    print(numero)
    numero -= 1

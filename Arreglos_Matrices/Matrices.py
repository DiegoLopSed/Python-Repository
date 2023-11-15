matriz=[]#! Crea una lista/arreglo que sera nuestra matriz

for i in range(3):#? Almacena en todos los elementos de la matriz 0
    fila =[0 for i in range(3)]
    matriz.append(fila)

for f in matriz: #* Muestra los elementos de la matriz
    print(f)

for i in range (3): #? Cambia los elementos de la matriz por datos ingresados por el usuario
    for j in range (3):
        print("Posición:",i,",",j)
        matriz[i][j]=int(input("Numero:")) #! Lee numeros a almacenar

for f in matriz: #* Muestra los elementos de la matriz
    print(f)



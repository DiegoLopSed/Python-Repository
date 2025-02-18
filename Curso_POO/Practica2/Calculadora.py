class OperacionMatematica:#TODO Creamos la clase 'Padre' OperacionMatematica
    def __init__(self,name, num1, num2=0):  #! Valor predeterminado para num2
        self.num1 = num1
        self.num2 = num2
        self.name = name #* atributo para el nombre de la operación

    def mostrar_numeros(self):#* Metodo para mostrar valores
        print(f"Los numeros son: {self.num1} y {self.num2}")

    def calcular(self):
         pass

class Suma(OperacionMatematica):#* Clase 'Hija' Suma, hereda de Clase 'Padre'

  def calcular(self):#* Metodo para sumar
    return self.num1 + self.num2

class Resta(OperacionMatematica):#* Clase 'Hija' Resta, hereda de Clase 'Padre'

  def calcular(self):#* Metodo para restar
    return self.num1 - self.num2

class Multiplicacion(OperacionMatematica):#* Clase 'Hija' Multiplicacion, hereda de Clase 'Padre'

  def calcular(self):#* Metodo para multiplicar
    return self.num1 * self.num2

class Division(OperacionMatematica):#* Clase 'Hija' Division, hereda de Clase 'Padre'

  def calcular(self):
    return round((self.num1 / self.num2),3)#* Metodo para dividir

class Potencia(OperacionMatematica):#* Clase 'Hija' Potencia, hereda de Clase 'Padre'

  def calcular(self):
    return self.num1 ** self.num2#* Metodo para elevar

class Raiz(OperacionMatematica):#* Clase 'Hija' Raiz, hereda de Clase 'Padre'

    def __init__(self, name,num1):
        super().__init__(name,num1)  #* Solo se pasa num1, num2 toma el valor predeterminado

    def calcular(self):
        if self.num1 >= 0:
            return(self.num1 ** (1 / 2))
        else:#! lanza una excepción para el mensaje de no raiz cuadrada negativa
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")

def realizar_op(num1,num2,op):
    #? segun el signo y los numeros realizar la operación
    #? e instancian los objetos para dichas operaciones
    if op == '+':
        Suma1 = Suma('Suma',num1,num2)
        print(f"El resultado de la {Suma1.name} es: ", Suma1.calcular())
    elif op == '-':
        Resta1 = Resta('Resta',num1,num2)
        print(f"El resultado de la {Resta1.name} es: ",Resta1.calcular())
    elif  op == '*':
        Multi = Multiplicacion('Multiplicación',num1,num2)
        print(f"El resultado de la {Multi.name} es: ", Multi.calcular())
    elif op == '/':
        Div = Division('División',num1,num2)
        print(f"El resultado de la {Div.name} es: ",Div.calcular())
    elif op == '**':
        Pow = Potencia('Potencia',num1,num2)
        print(f"El resultado de la {Pow.name} es: ",Pow.calcular())
    elif op == '*/':
        raiz = Raiz('Raiz cuadrada',num1)
        print(f"El resultado de la {raiz.name} es: ",raiz.calcular())
    else:
        raise ValueError('Elige una operación valida')


def ingresar_numeros(op):

    #* Solicita los numeros para operar 'Solo 1 en caso para la raiz'
    if op == '*/':
        num1 = int(input("Ingresa el número1: "))
        num2 = 0

    else:
        num1 = int(input("Ingresa el número 1: "))
        num2 = int(input("Ingresa el número 2: "))

    realizar_op(num1,num2,op)

def Menu():
    #? Despliega un menu de opciones
    print("Elige una operación...")

    print("Suma '+' ")
    print("Resta '-' ")
    print("Multiplicación '*' ")
    print("División '/' ")
    print("Potencia '**' ")
    print("Raiz '*/' ")

    op = input("Operación: ")
    return op

while True:#! Repite la opción de realizar operaciones
    try:
        ingresar_numeros(Menu())#? Función para poder realizar todas las operaciones
        break
    except NameError as e:
        print(f"NameError: {e}")
    except Exception as e:  #? Captura cualquier otra excepción
        print(f"Error: {e}")



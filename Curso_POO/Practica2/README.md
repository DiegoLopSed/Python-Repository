# Operaciones Matemáticas en Python

Este proyecto es una implementación en Python que realiza varias operaciones matemáticas (suma, resta, multiplicación, división, potencia, y raíz cuadrada) utilizando el concepto de herencia y clases.

## Descripción

El programa tiene una clase base llamada `OperacionMatematica` que define los atributos y métodos comunes para todas las operaciones matemáticas. Luego, se definen clases específicas para cada operación matemática como `Suma`, `Resta`, `Multiplicacion`, `Division`, `Potencia` y `Raiz`. 

El programa también incluye una interfaz interactiva en la consola que permite al usuario elegir una operación, ingresar los números necesarios, y ver el resultado.

## Estructura del Código

1. **Clase `OperacionMatematica`**: Clase base con atributos comunes (`num1`, `num2` y `name`) y un método `mostrar_numeros` para mostrar los números involucrados en la operación.
2. **Clases derivadas**: 
   - `Suma`: Realiza la suma de `num1` y `num2`.
   - `Resta`: Realiza la resta de `num1` y `num2`.
   - `Multiplicacion`: Realiza la multiplicación de `num1` y `num2`.
   - `Division`: Realiza la división de `num1` y `num2` (redondeada a 3 decimales).
   - `Potencia`: Eleva `num1` a la potencia de `num2`.
   - `Raiz`: Calcula la raíz cuadrada de `num1`, si `num1` es no negativo.
   
3. **Función `realizar_op`**: Según la operación seleccionada por el usuario, instanciará la clase correspondiente y mostrará el resultado.
4. **Función `ingresar_numeros`**: Solicita los números del usuario según la operación seleccionada y luego llama a `realizar_op` para procesar la operación.
5. **Función `Menu`**: Muestra el menú interactivo de operaciones disponibles y recibe la entrada del usuario.

## Uso

1. Al ejecutar el script, el programa presentará un menú interactivo en la consola donde podrás elegir una operación matemática.
2. Según la operación seleccionada, el programa pedirá que ingreses los números necesarios.
3. Después de ingresar los números, el programa calculará y mostrará el resultado de la operación seleccionada.
4. Puedes realizar múltiples operaciones en una misma ejecución del programa.

### Ejemplo de ejecución

```bash
Elige una operación...
Suma '+' 
Resta '-' 
Multiplicación '*' 
División '/' 
Potencia '**' 
Raiz '*/' 
Operación: +
Ingresa el número 1: 5
Ingresa el número 2: 3
El resultado de la Suma es:  8


## Requisitos

- Python 3.x o superior.
- **Recomendación**: Para mejorar la legibilidad del código, te sugerimos instalar la extensión **Better Comments** en Visual Studio Code. Esta extensión ayuda a resaltar comentarios de manera más eficiente, lo que facilita la comprensión del código. Puedes encontrarla e instalarla desde el marketplace de Visual Studio Code.

### Instalación de Better Comments en Visual Studio Code

1. Abre Visual Studio Code.
2. Dirígete a la vista de extensiones (Ctrl+Shift+X o Cmd+Shift+X en macOS).
3. Busca "Better Comments" en la barra de búsqueda.
4. Instala la extensión y reinicia VS Code si es necesario.
5. Ahora podrás disfrutar de un formato de comentarios más fácil de leer, con colores que indican la importancia del comentario.

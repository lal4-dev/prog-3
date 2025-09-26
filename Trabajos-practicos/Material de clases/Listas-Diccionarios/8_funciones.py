# Crear un pequeño programa que realice una función aritmética que permita al usuario ingresar datos por la terminal
# acorde a distintas opciones.  Para ellos debemos definir una función que reciba parámetros: Combinar funciones
# nativas y funciones definidas, condicionales, y bucles. Si el usuario ingresa el nro 1, realiza la acción A. Si el
# usuario ingresa el nro 2, realiza la acción B.

def calcular_operacion(opcion, numero1, numero2):
    if opcion == 1:
        # Acción A
        resultado = numero1 + numero2
    elif opcion == 2:
        # Acción B
        resultado = numero1 * numero2
    else:
        resultado = None
    return resultado


# Programa principal
opcion = int(input("Ingrese una opción (1- SUMA o 2- MULTIPLICACION): "))

# Validar que la opción ingresada sea 1 o 2
while opcion not in [1, 2]:
    print('Ingrese una opción válida (1- SUMA o 2- MULTIPLICACION).')
    opcion = int(input("Ingrese una opción (1- SUMA o 2- MULTIPLICACION): "))

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Llamada a la función
resultado = calcular_operacion(opcion, numero1, numero2)

# Imprimir resultado si la opción es válida
if resultado is not None:
    if opcion == 1:
        print("El resultado de la suma es:", resultado)
    elif opcion == 2:
        print("El resultado de multiplicar los dos números es:", resultado)
else:
    print("Opción inválida")

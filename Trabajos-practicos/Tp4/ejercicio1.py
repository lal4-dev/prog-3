#Ejercicio Nro 1: Validación de entrada y búsqueda en una Lista.
#Implementar un programa que valide la entrada de un número entero y verifique su presencia enuna lista.
#Requisitos:
#1. Solicitar al usuario que ingrese un número entero del 0 al 9. Listo
#2. Mientras el número ingresado no esté en el rango especificado, repetir la solicitud. Listo
#3. Verificar si el número se encuentra en una lista predefinida de números.
#4. Notificar al usuario si el número está o no en la lista.

#Concepto útil: Utilizar la sintaxis [valor] in [lista] para comprobar la presencia de un valor en unalista

lista = [1,3,5,7,9];

numero = int(input("Ingrese un numero entero entre un rango de 0 a 9: "));
print();

while numero<0 or numero>9: 
    print("numero fuera de rango, proba de nuevo");
    numero = int(input("Ingrese un numero entero entre un rango de 0 a 9: "));
    print();

if(numero in lista):
    print(f"El numero {numero},esta en la lista");
else:
    print(f"El numero {numero},no esta en la lista");

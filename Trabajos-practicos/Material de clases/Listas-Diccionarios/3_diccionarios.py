# Un diccionario en Python es una estructura de datos que permite almacenar pares clave-valor. A diferencia de las
# listas y las tuplas, que son secuencias ordenadas de elementos, los diccionarios no están ordenados Cada clave
# dentro de un diccionario es única y se utiliza para acceder al valor asociado. Los diccionarios se definen
# utilizando llaves {}, y los pares clave-valor están separados por dos puntos :

edades = {"Laura": 22, "Beto": 27}
edades["Carla"] = 30
edades["Laura"] += 1

print(edades)

# # keys(): Devuelve todas las keys de un diccionario
# print(edades.keys())

# # values(): Devuelve todos los values de un diccionario.
# print(edades.values())

# # items(): Devuelve todos los pares de key/values de un diccionario
# print(edades.items())

# # pop() Elimina un elemento del diccionario a partir de su key
# valor_eliminado = edades.pop('Beto')
#
# # Mostrar el valor eliminado y el diccionario actualizado
# print("Valor eliminado:", valor_eliminado)
# print("Diccionario actualizado:", edades)

# # clear(): Elimina todos los elementos del diccionario.
# edades.clear()
#
# # Mostrar el diccionario después de limpiar
# print("Diccionario después de clear:", edades)
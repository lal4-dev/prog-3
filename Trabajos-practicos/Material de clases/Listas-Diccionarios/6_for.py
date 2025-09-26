# Recorriendo una lista de nombres
# La lista nombres contiene tres nombres: "Laura", "Paula" y "Charly".
# El bucle for itera sobre cada elemento de la lista y la variable del bucle nombre toma
# cada nombre de la lista. La print(nombre)declaración imprime cada nombre en una línea separada.

nombres = ["Laura", "Paula", "Charly"]
for nombre in nombres:
    print(nombre)

# Recorriendo un diccionario
#El diccionario autocontiene información sobre un automóvil, incluida su marca, modelo y año.
# El forbucle itera sobre cada par clave-valor del diccionario utilizando el items()método.
# Las variables de bucle clave y valor representan la clave y el valor de cada par, respectivamente.
# La print()declaración utiliza formato de cadena f para mostrar la clave y el valor de cada par.


auto = {"marca": "Ford", "modelo": "Mustang", "año": 1964}

for clave, valor in auto.items():
    print(f"Clave: {clave} - Valor: {valor}")

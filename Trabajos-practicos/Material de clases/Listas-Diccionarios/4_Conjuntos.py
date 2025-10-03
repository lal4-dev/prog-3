# Los conjuntos en Python son objetos mutables, lo que significa que puedes agregar, eliminar y actualizar
# elementos una vez que se han creado. Los conjuntos también admiten operaciones matemáticas comunes
# como la unión, la intersección y la diferencia.

# Creación de un conjunto vacío
conjunto_vacio = set()
print(conjunto_vacio)  # output: set()

# # Creación de un conjunto con elementos
# conjunto = {1, 2, 5}
# print(conjunto)  # output: {1, 2, 5}
#
# # Añadir un elementos a un conjunto
# conjunto.add(4)
# print(conjunto)  # output: {1, 2, 4, 5}
#
#
# # Eliminar elementos de un conjunto
# # Puedes agregar elementos a un conjunto utilizando el método add() y eliminar elementos utilizando
# # el método remove() o discard(). La diferencia entre remove() y discard() es que remove() generará un error
# # si el elemento no está presente en el conjunto, mientras que discard() no generará ningún error.
#
# conjunto.remove(2)
# print(conjunto)  # output: {1, 3, 4}
#
# conjunto.discard(6)  # No genera ningún error
# print(conjunto)  # output: {1, 3, 4}
#

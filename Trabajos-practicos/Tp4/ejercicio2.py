#Ejercicio Nro 2: Gestión de Conjuntos de Usuarios y Administradores

#Requisitos:
#1. Crear un conjunto llamado usuarios con los nombres: Marcela, David, Elvira, Juan, y Marcos.
#2. Crear un conjunto llamado administradores con los nombres: Juan y Marcela.
#3. Eliminar a Juan del conjunto de administradores.
#4. Añadir a Marcos como administrador, pero mantenerlo en el conjunto de usuarios.
#5. Mostrar todos los usuarios, indicando si cada uno es administrador o no.
#Sugerencia: Utilizar el método .discard(elemento) para eliminar un elemento de un conjunto.

usuarios = {"Marcela", "David", "Elvira", "Juan", "Marcos"};

administradores = {"Juan", "Marcela"};

administradores.discard("Juan");

administradores.add("Marcos");

for usuarios in usuarios:
    if(usuarios in administradores):
        print(f"{usuarios}: es administrador");
    else:
        print(f"{usuarios}: no es administrador");
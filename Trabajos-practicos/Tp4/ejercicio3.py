#Ejercicio Nro 3: Registro de Información en un Diccionario.

#Requisitos:
#1. Solicitar al usuario que ingrese los siguientes datos: nombre, edad, dirección y teléfono.
#2. Almacenar los datos en un diccionario llamado usuario_info.
#3. Permitir el ingreso de información para varios usuarios.
#4. Mostrar la información ingresada para cada usuario en formato clave-

usuarios_infos = {};

while True:
    nombre = input("Ingrese el nombre del usuario(o 'salir' para terminar): ");
    if nombre.lower() == "salir":
        break;
    
    edad = input("Ingrese la edad: ");
    direccion = input("Ingrese la direccion: ");
    telefono = input("Ingrese el telefono: ");

    usuario_info = {
        "edad": edad,
        "direccion": direccion,
        "telefono": telefono
    }

    usuarios_infos[nombre] = usuario_info;

print("\n-- Informacion de usuarios --");

for nombre, info in usuarios_infos.items():
    print(f"\nUsuario:{nombre}");
    for clave, valor in info.items():
        print(f"{clave}: {valor}");
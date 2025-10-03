#Ejercicio Nro 4: Gestión de Inventario de Instrumentos Musicales
#La fábrica tiene una lista de sucursales, cada una con su nombre y una lista de instrumentos a la venta. De cada instrumento se conoce el ID alfanumérico, precio y tipo (Percusión, Viento o Cuerda).

#Requisitos:
#1. Método listarInstrumentos(): Mostrar todos los datos de cada instrumento en la consola.
#2. Método instrumentosPorTipo(tipo): Devolver una lista de instrumentos cuyo tipo coincida con el parámetro tipo.
#3. Método borrarInstrumento(id): Recibir un ID y eliminar el instrumento asociado de la sucursal correspondiente.
#4. Método porcInstrumentosPorTipo(sucursal): Recibir el nombre de una sucursal y retornar los porcentajes de instrumentos por tipo.

class Instrumento:
    def __init__(self,id_instrumento,precio,tipo):
        self.id = id_instrumento;
        self.precio = precio;
        self.tipo = tipo;

    def __str__(self):
        return (f"ID: {self.id}, Precio: {self.precio}, Tipo: {self.tipo} ");

class Sucursal:
    def __init__(self,nombre):
        self.nombre = nombre;
        self.instrumentos = [];

    def listarInstrumentos(self):
        print(f"\n Surcursal: {self.nombre}");
        for instrumento in self.instrumentos:
            print(instrumento);
    
    def instrumentoPorTipo(self,tipo):
        listaInstrumentos = [];
        
        for lista in self.instrumentos:
            if lista.tipo.lower() == tipo.lower():
                listaInstrumentos.append(lista);

        return listaInstrumentos ;

    def borrarInstrumento(self,id_instrumento):
        for instrumentoBorrar in self.instrumentos:
            if instrumentoBorrar.id == id_instrumento:
                self.instrumentos.remove(instrumentoBorrar);
                return True;
        return False;

    def porcInstrumentosPorTipo(self):
        total = len(self.instrumentos);
        if total == 0:
            return {}

        percusion = 0;
        viento = 0;
        cuerda = 0;

        for instrumentoContar in self.instrumentos:
            if instrumentoContar.tipo.lower() == "percusion":
                percusion += 1;
            elif instrumentoContar.tipo.lower() == "viento":
                viento += 1;
            elif instrumentoContar.tipo.lower() == "cuerda":
                cuerda += 1;

        porcentajes = {
            "Percusion": (percusion / total) * 100,
            "Viento": (viento / total) * 100,
            "Cuerda": (cuerda / total) * 100
        }

        return porcentajes


# ------------------------
# Código de prueba por si la duda uno tiene que probar 
# ------------------------

# Crear sucursal al no especificar el punto el como las instanciamos si nosotros o por entrada lo hago asi de manera manual por la rapides
sucursal1 = Sucursal("Sucursal Centro");

# Crear instrumentos
i1 = Instrumento("G001", 1500, "Cuerda");
i2 = Instrumento("G002", 2000, "Cuerda");
i3 = Instrumento("D001", 3000, "Percusion");
i4 = Instrumento("S001", 2500, "Viento");
i5 = Instrumento("B001", 1800, "Cuerda");

# Agregar instrumentos a la sucursal
sucursal1.instrumentos.append(i1);
sucursal1.instrumentos.append(i2);
sucursal1.instrumentos.append(i3);
sucursal1.instrumentos.append(i4);
sucursal1.instrumentos.append(i5);

# 1. Listar todos los instrumentos
print("\n--- Listar instrumentos ---");
sucursal1.listarInstrumentos();

# 2. Buscar instrumentos por tipo
print("\n--- Instrumentos de cuerda ---");
cuerda = sucursal1.instrumentoPorTipo("Cuerda");

for instrumentosPrueba in cuerda:
    print(instrumentosPrueba);

# 3. Borrar un instrumento
print("\n--- Borrar instrumento con ID G002 ---");
if sucursal1.borrarInstrumento("G002"):
    print("Instrumento borrado con exito");
else:
    print("No se encontro el instrumento");

print("\nLista despues de borrar:");
sucursal1.listarInstrumentos();

# 4. Porcentaje de instrumentos por tipo
print("\n--- Porcentajes por tipo ---");

porcentajes = sucursal1.porcInstrumentosPorTipo();
for tipo, porc in porcentajes.items():
    print(f"{tipo}: {porc:.2f}%");

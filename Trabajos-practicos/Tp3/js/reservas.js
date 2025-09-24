
//aca hice el constructor
function reserva(origen,destino,fecha,hora,clase,ubicacion,numeroSilla,nombre,dni,nacimiento,sexo){
    this.origen = origen;
    this.destino = destino;
    this.fecha = fecha;
    this.hora = hora;
    this.clase = clase;
    this.ubicacion = ubicacion;
    this.numeroSilla=numeroSilla;
    this.nombre = nombre;
    this.dni = dni;
    this.nacimiento = nacimiento;
    this.sexo = sexo;
}

//aca inicializo el array e inserto los elementos o retorno el array
class SistemaReservas{
    constructor(){
        this.reservas=[];
    }

    agregarReservas(reserva){
        this.reservas.push(reserva)
    }

    obtenerReservas(){
        return this.reservas
    }
}

//aca inserto de manera manual una prueba
const SistemaPrueba = new SistemaReservas();
SistemaPrueba.agregarReservas(new reserva("Cordoba","Tucuman","2025-10-20","10:00","Ejecutiva","Ventanilla","A1","Alejo Maidana","44943481","2003-08-29","M"));
SistemaPrueba.agregarReservas(new reserva("Cordoba","Tucuman","2025-10-25","17:00","Economica","Pasillo","C7","Leonel Saidana","41841910","2003-06-16","M"));
SistemaPrueba.agregarReservas(new reserva("Mendoza","Cordoba","2025-10-14","11:00","Ejecutiva","Ventanilla","B2","Valentina Diaz","46221091","2004-10-14","F"));





//aca muesto todo en la tabla
const tabla = document.getElementById("tablaReservas");

SistemaPrueba.obtenerReservas().forEach(reservaSistema => {
    const fila  = document.createElement("tr");

    const celdaOrigen = document.createElement("td");
    celdaOrigen.textContent = reservaSistema.origen;
    fila.appendChild(celdaOrigen);

    const celdaDestino = document.createElement("td");
    celdaDestino.textContent = reservaSistema.destino;
    fila.appendChild(celdaDestino);

    const celdaFecha = document.createElement("td");
    celdaFecha.textContent = reservaSistema.fecha;
    fila.appendChild(celdaFecha)

    const celdaHora = document.createElement("td");
    celdaHora.textContent = reservaSistema.hora;
    fila.appendChild(celdaHora);

    const celdaClase = document.createElement("td");
    celdaClase.textContent = reservaSistema.clase;
    fila.appendChild(celdaClase);

    const celdaUbicacion = document.createElement("td");
    celdaUbicacion.textContent = reservaSistema.ubicacion;
    fila.appendChild(celdaUbicacion);

    const celdaAsiento = document.createElement("td");
    celdaAsiento.textContent = reservaSistema.numeroSilla;
    fila.appendChild(celdaAsiento);
    
    const celdaNombre = document.createElement("td");
    celdaNombre.textContent = reservaSistema.nombre;
    fila.appendChild(celdaNombre)

    const celdaDNI = document.createElement("td");
    celdaDNI.textContent = reservaSistema.dni;
    fila.appendChild(celdaDNI);

    const celdaNacimiento = document.createElement("td");
    celdaNacimiento.textContent = reservaSistema.nacimiento;
    fila.appendChild(celdaNacimiento);

    const celdaSexo = document.createElement("td");
    celdaSexo.textContent = reservaSistema.sexo;
    fila.appendChild(celdaSexo);

    tabla.appendChild(fila);
})
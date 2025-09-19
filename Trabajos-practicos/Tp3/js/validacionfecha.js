function validarfecha(fechaingresada){
    const hoy = new Date();

    const fechaVuelo = new Date(fechaingresada);

    if (fechaVuelo < hoy){
        return "Fecha de vuelo debe ser mayor a la fecha actual"
    }
    return true
}

document.getElementById("form-vuelo").addEventListener("submit",(enviodatos)=>{

    const fechaingresada = document.getElementById("fecha-vuelo").value;
    const resultado = validarfecha(fechaingresada);

    const mensaje = document.getElementById("mensajeFecha");

    if(resultado === true){
        mensaje.style.display = "block";
        mensaje.textContent = "Fecha valida";
        mensaje.style.color = "green";
    }
    else{
        mensaje.style.display = "block";
        enviodatos.preventDefault();
        mensaje.textContent = resultado;
        mensaje.style.color = "red";
    }
})



//origen y destino no iguales------------------------------------------------------------------

const origenVuelo =document.getElementById("origen");
const destinoVuelo =document.getElementById("destino");

origenVuelo.addEventListener('change',()=> {
    
    const valorOrigen = origenVuelo.value;

    Array.from(destinoVuelo.options).forEach(opciones =>{
        if(opciones.value === valorOrigen){
            opciones.disabled = true;
            opciones.style.color ="red";

        }
        else{
            opciones.disabled = false;
            opciones.style.color="green";
        }
    })
    
})
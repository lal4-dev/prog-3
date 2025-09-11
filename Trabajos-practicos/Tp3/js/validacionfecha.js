function validarfecha(fechaingresada){
    const hoy = new Date();

    const fechaVuelo = new Date(fechaingresada);

    if (fechaVuelo < hoy){
        return "Fecha de vuelo debe ser mayor a la fecha actual"
    }
    return true
}

document.getElementById("form-vuelo").addEventListener("submit",function(enviodatos){

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

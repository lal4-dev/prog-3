const cantidadInput = document.getElementById("cantidad-pasaje");
const claseSelect = document.getElementById("clase");
const bloqueOriginal = document.getElementById("bloqueRepetitivo");

// Contenedor donde vamos a poner los bloques clonados
const contenedorBloques = document.createElement("div");
bloqueOriginal.parentNode.insertBefore(contenedorBloques, bloqueOriginal.nextSibling);

bloqueOriginal.style.display = "none";

cantidadInput.addEventListener("change", actualizarBloques);
claseSelect.addEventListener("change", actualizarBloques);

function actualizarBloques() {
    contenedorBloques.innerHTML = "";

    const cantidad = parseInt(cantidadInput.value) || 0;
    const clase = claseSelect.value; // 1=Ejecutiva, 2=Economica

    for (let i = 0; i < cantidad; i++) {
        const clon = bloqueOriginal.cloneNode(true);
        clon.style.display = "block"; // Habilitamos su visualización

        // Ajustamos el input del número de silla según la clase
        const numeroSillaInput = clon.querySelector("#numero-silla");
        if (clase === "1") { // Ejecutiva
            numeroSillaInput.min = 1;
            numeroSillaInput.max = 8;
        } else { // Económica
            numeroSillaInput.min = 9;
            numeroSillaInput.max = 50;
        }

        // Agregamos al contenedor
        contenedorBloques.appendChild(clon);
    }
}

/*(() => {
    BOTON.addEventListener("click", obtener);
    botones.addEventListener("click", delegacion);
})();*/

/*function obtener() {
    let Cedula = localStorage.getItem("Cedula");
    let Apellidos = localStorage.getItem("Apellidos");
    let Nombres = localStorage.getItem("Nombres");
    let Nacionalidad = localStorage.getItem("Nacionalidad");
    let Lnacimiento = localStorage.getItem("Lnacimiento");
    let Nacimiento = localStorage.getItem("Nacimiento");
    let Edad = localStorage.getItem("Edad");
    let Direccion = localStorage.getItem("Direccion");
    let eCivil = localStorage.getItem("eCivil");
    let Email = localStorage.getItem("Email");
    let tel = localStorage.getItem("cel");

     if () {
         let nombre = localStorage.getItem("nombre");
         let persona = JSON.parse(localStorage.getItem("persona"));
         console.log(nombre);
         console.log(persona);
     } else {
         console.log("no hay entradas en el localstroage");
     }  
}
*/
var guardar = function() {
    /*var Cedula =document.querySelector("#Cedula") ;
    var Apellidos = document.querySelector("#Apellidos");
    var Nombres = document.querySelector("#Nombres");
    var Nacionalidad = document.querySelector("#Nacionalidad");
    var Lnacimiento = document.querySelector("#Lnacimiento");
    var Nacimiento = document.querySelector("#Nacimiento");
    var Edad = document.querySelector("#Edad");
    var Direccion = document.querySelector("#Direccion");
    var eCivil = document.querySelector("#eCivil");
    var Email = document.querySelector("#Email");
    var nombre = tel.querySelector("#tel");
    var apellido = cel.querySelector("#cel");
*/
    localStorage.setItem("Cedula", document.querySelector("#Cedula").value);
    localStorage.setItem(" Apellidos", document.querySelector("#Apellidos").value);
    localStorage.setItem(" Nombres", document.querySelector("#Nombres").value);
    localStorage.setItem(" Nacionalidad", document.querySelector("#Nacionalidad").value);
    localStorage.setItem(" Lnacimiento", document.querySelector("#Lnacimiento").value);
    localStorage.setItem(" Nacimiento", document.querySelector("#Nacimiento").value);
    localStorage.setItem(" Edad ", document.querySelector("#Edad").value);
    localStorage.setItem(" Direccion", document.querySelector("#Direccion").value);
    localStorage.setItem(" eCivil", document.querySelector("#eCivil").value);
    localStorage.setItem(" Email", document.querySelector("#Email").value);
    localStorage.setItem(" tel", document.querySelector("#tel").value);
    localStorage.setItem(" cel", document.querySelector("#cel").value);


}

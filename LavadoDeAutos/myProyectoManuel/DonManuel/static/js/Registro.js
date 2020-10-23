function validarNombre(dato){
    var a = dato.trim().length;

    if (a == null || (a < 3 || a > 80)) {
        alert("El nombre y el apellido deben contener entre 3 y 80 caracteres");
        return false;
    }  
    return true;
}

function validarUser(dato){
    var u = dato.trim().length;

    if( u == null || u < 8 ){
        alert("El usuario y la contraseña deben tener mínimo 8 caracteres");
        return false;
    }
    return true;
}

function validarContra(pas1, pas2){
    if (pas1 != pas2) {
        alert("Las contraseñas deben coincidir");
        return false;
    }
    return true;
}

function validar(){
    var res;

    var nom = document.getElementById("txtNombre").value;
    res = validarNombre(nom);
    if (res == false) {
        return false;
    }

    var nom = document.getElementById("txtApellidos").value;
    res = validarNombre(nom);
    if (res == false) {
        return false;
    }

    var usu = document.getElementById("txtUser").value;
    res = validarUser(usu);
    if (res == false) {
        return false;
    }
    
    var usu = document.getElementById("txtPass").value;
    res = validarUser(usu);
    if (res == false) {
        return false;
    } 

    var pas1 = document.getElementById("txtPass").value;
    var pas2 = document.getElementById("txtPass2").value;
    res = validarContra(pas1, pas2)
    if (res == false) {
        return false;
    } 

}
function validarRut(){
    var rut = document.getElementById("txtRut").value;

    if (rut.trim().length != 10) {
        alert("Rut no tiene el largo necesario de 10 (12345678-9)");
        return false;
    }
    var num = 3; // secuencia
    var suma = 0;

    for (let index = 0; index < 8; index++) {
        var carac = rut.slice(index, index + 1);
        suma = suma + (carac * num);
        num = num - 1;
        if (num == 1) {
            num = 7;
        }
    }

    var resto = suma % 11;
    var dv = 11 - resto;
    
    if (dv > 9) {
        if (dv == 10) {
            dv = "K";
        }
        else{
            dv = 0;
        }
    }

    var dv_usuario = rut.slice(-1).toUpperCase();
    if (dv != dv_usuario) {
        alert("Rut incorrecto");
        return false;
    }

    return true;
}

function validarFecha(){
    var fechaFrom = document.getElementById("txtFechaN").value;
    var fechaSist = new Date();

    var ano = fechaFrom.slice(0,4);
    var mes = fechaFrom.slice(5,7);
    var dia = fechaFrom.slice(8,10);

    var fechaMia = new Date(ano, (mes - 1),  dia);

    if (fechaMia > fechaSist) {
        alert("Fecha de nacimiento incorrecta");
        return false;
    }
    return true;
}



/*PROBANDO UNA FORMA DE VALIDAR LOS ESPACIOES EN BLANCO*/ 

/**/ 


function validarNombre(dato){
        if (dato.trim() == null || (dato.trim().length < 3 || dato.trim().length > 80)) {
        alert("El nombre y el apellido deben contener entre 3 y 80 caracteres");
        return false;
    }  
    return true;
}

function validarUser(){
    var user= document.getElementById("txtUser").value;
    if( user.trim()==null || user.trim().length < 8 ){
        alert("El usuario debe tener mínimo 8 caracteres");
        return false;
    }
    return true;
}



function validarPass(){
    var pass = document.getElementById("txtPass").value;
    if( pass.trim() == null || pass.trim().length < 8 ){
        alert("La contraseña debe tener mínimo 8 caracteres");
        return false;
    }
    return true;
}


function espacios(){
    var espacio_blanco = /[a-z]/i;  //Expresión regular
    var nombre = document.getElementById("txtNombre").value; 
    var ap = document.getElementById("txtApellidos").value;
    var user=document.getElementById("txtUser").value;
    var pass=document.getElementById("txtPass").value;

    if(!espacio_blanco.test(nombre) )
    {
        alert("Solo de admiten letras en el nombre");
        document.getElementById("txtNombre").focus();
        return false;
    }
    else if(!espacio_blanco.test(ap)){
        alert("Solo de admiten letras en el apellido.");
        document.getElementById("txtApellidos").focus();
        return false;
    }
    else if(!espacio_blanco.test(user)){
        alert("Solo de admiten letras en el usuario");
        document.getElementById("txtUser").focus();
        return false;
    }
    else if(!espacio_blanco.test(pass)){
        alert("Solo de admiten letras en el contraseña");
        document.getElementById("txtPass").focus();
        return false;
    }

    return true;
}

function contrasenias(pass1, pass2){
    if (pass1 != pass2) {
        alert("Las contraseñas deben coincidir");
        document.getElementById("txtPass").focus();
        return false;
    }
}

function validarTodo(){
    var resp;
    
    resp = validarRut();
    if (resp == false) {
        return false;
    }

    resp = validarFecha();
    if (resp == false) {
        return false;
    }

    var nombre = document.getElementById("txtNombre").value;
    resp = validarNombre(nombre);
    if (resp == false) {
        return false;
    }

    var nombre = document.getElementById("txtApellidos").value;
    resp = validarNombre(nombre);
    if (resp == false) {
        return false;
    }

    var p1 = document.getElementById("txtPass").value;
    var p2 = document.getElementById("txtPass2").value;
    resp = contrasenias(p1,p2);
    if (resp == false) {
        return false;
    }

    resp=validarUser();
    if (resp == false) {
        return false;
    }

    resp=validarPass();
    if (resp == false) {
        return false;
    }

    resp=espacios();
    if (resp == false) {
        return false;
    }
    return true;
}
function validarNombre(){
    var nom=document.getElementById("txtNombre").value;
    if(nom.trim().length < 3 || nom.trim().length > 120){
        alert("El nombre debe tener entre 3 y 120 carcateres");
        return false;
    }
    return true;
}

function validarPrecio(){
    var valor = document.getElementById("txtvalor").value;

    if (valor < 1){
        alert("El precio mínimo de un artículo debe ser $1");
        return false;
    }
    return true;
}

function validarStock(){
    var valor = document.getElementById("txtstock").value;
    
    if (valor < 0){
        alert("El stock mínimo de un artículo debe ser 0");
        return false;
    }
    return true;
}

function validarTodo(){
    var r;
    r = validarNombre();
    if(r == false){
        return false;
    }

    r = validarPrecio();
    if(r == false){
        return false;
    }

    r = validarStock();
    if(r == false){
        return false;
    }

    return true;
}

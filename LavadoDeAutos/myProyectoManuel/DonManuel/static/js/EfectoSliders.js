const lista = document.querySelector('.slider_lista');
const imaga = Array.from(lista.children); // almacena las imagenes en un arreglo

const siguiente = document.querySelector('.slider_boton--der');
const anterior = document.querySelector('.slider_boton--izq');

const indicador = document.querySelector('.slider_puntos');
const puntos = Array.from(indicador.children);

const tamanioimg = imaga[0].getBoundingClientRect().width;

// Imagenes junta a otra
const setPosicion = (imaga, index) => { // funcion
    imaga.style.left = tamanioimg * index + 'px';
};
imaga.forEach(setPosicion);

const moviIMG = (lista, imgactual, imgselect) => { // funcion mueve la imagen
    lista.style.transform = 'translateX(-' + imgselect.style.left + ')'; // movimiento
    imgactual.classList.remove('indicador-activo'); // quita el nombre
    imgselect.classList.add('indicador-activo'); // agrega el nombre
}

const moviPUN = (puntoactu, puntopres) => { // funcion cambia el boton
    puntoactu.classList.remove('indicador-activo');
    puntopres.classList.add('indicador-activo');
}

const flechas = (imaga, anterior, siguiente, puntoindi) =>{ // Funcion para las flechas
    if(puntoindi == 0){
        anterior.classList.add('oculto');
        siguiente.classList.remove('oculto');
    }
    else if (puntoindi == imaga.length -1){
        anterior.classList.remove('oculto');
        siguiente.classList.add('oculto');
    }
    else{
        anterior.classList.remove('oculto');
        siguiente.classList.remove('oculto');
    }
}

// boton derecho
siguiente.addEventListener('click', e => {
    const imgactual = lista.querySelector('.indicador-activo');
    const imgsiguie = imgactual.nextElementSibling; // imagen siguiente
    const puntoactu = indicador.querySelector('.indicador-activo');
    const puntosigi = puntoactu.nextElementSibling;
    const siguiindi = imaga.findIndex(im => im === imgsiguie);

    moviIMG(lista, imgactual, imgsiguie);
    moviPUN(puntoactu, puntosigi);
    flechas(imaga, anterior, siguiente, siguiindi);
});

// boton izquierdo
anterior.addEventListener('click', e => {
    const imgactual = lista.querySelector('.indicador-activo');
    const imganteri = imgactual.previousElementSibling; // imagen anterior
    const puntoactu = indicador.querySelector('.indicador-activo');
    const puntoante = puntoactu.previousElementSibling;
    const anterindi = imaga.findIndex(im => im === imganteri);

    moviIMG(lista, imgactual, imganteri);
    moviPUN(puntoactu, puntoante);
    flechas(imaga, anterior, siguiente, anterindi);
});

// puntos
indicador.addEventListener('click', e => {
    const puntopres = e.target.closest('button'); // punto presionado

    if (!puntopres) return; // si apreciona algo distinto a boton sale de la funcion

    const imgactual = lista.querySelector('.indicador-activo');
    const puntoactu = indicador.querySelector('.indicador-activo');
    const puntoindi = puntos.findIndex(punto => punto === puntopres); //  toma el indice del punto presionado
    const imgindi = imaga[puntoindi]; // toma la imagen del indice, dependiendo del boton presionado
        
    moviIMG(lista, imgactual, imgindi);
    moviPUN(puntoactu, puntopres);
    flechas(imaga, anterior, siguiente, puntoindi);
});



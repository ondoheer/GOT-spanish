//designa genero de hijos y hermanos
function designarGenero() {
    var chance = Math.floor((Math.random() * 10) + 1);
    var genero;
    if (chance % 2 == 0) {
        genero = 'mujer';
    } else {
        genero = 'hombre';
    }
    return genero
}

//imprime hermanos
function imprimirHermano(etiqueta, propiedadObjeto, containerToAppendTo) {
    if (typeof(propiedadObjeto) == 'string') {
        var genero = designarGenero();
        containerToAppendTo.append('<div class="toRemove"><span class="nombreRasgo">' + etiqueta + '(' + genero + '): </span><span>' + propiedadObjeto + '</span></div>');
    }
}

/******************
DATOS QUE SE ENVIAN: No es necesario generarlos todos porque solo envío los que python necesita y recibo otros
******************/
var npcCharacter = {
    "edad": null,
    "genero": null,

}
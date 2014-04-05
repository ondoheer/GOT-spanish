$(document).ready(function() {

    // Función que ata la funcion de click con los elementos aún no creados.
    //para lograrlo llamamos el .on a un elemento ya existente, pero lo atamos a uno
    //que aparecerá después
    $('.dataContainer').on('click', '.removeElement', function() {

        $(this).parent('.toRemove').remove();
    });
    $('.boton').on('click', function() {


        /*********
        BORRAMOS TODO EL CONTENIDO DEL GENERADO ANTERIOR
        *********/
        $('.rasgosContainer').empty();
        $('.eventosContainer').empty();
        $('.religionContainer').empty();
        $('.parejaContainer').empty();
        $('.hijosContainer').empty();
        $('.hermanosContainer').empty();
        $('.lejanosContainer').empty();

        npcCharacter.edad = $('#edad').val();
        if ($('#hombre').is(':checked')) {
            npcCharacter.genero = 'hombre'
        } else if ($('#mujer').is(':checked')) {
            npcCharacter.genero = 'mujer'
        } else {
            alert('No seleccionaste género');
        }

        if ($('#edad').val() < 13) {
            alert('La edad mínima es 13 años');
        }

        // solo si se han cumplido los requicitos envía la data.
        if (npcCharacter.genero != null && $('#edad').val() > 12) {


            /********
             Enviamos el objeto generado en functions.js
            ********/
            $.getJSON('/NPCgenerator', npcCharacter, function(npcRecibido) {
                console.log(npcRecibido.familia);


                /***************
                AGREGAMOS DATOS A LA WEB
                ***************/
                var religion = npcRecibido.religion
                var eventos = npcRecibido.eventos
                var rasgos = npcRecibido.rasgos
                var familia = npcRecibido.familia


                // Religion
                if (religion.creencia != false) {
                    $('.religionContainer').append('<div class="toRemove"><span class="nombreRasgo"> Creencia: </span><span>' + religion.creencia + '</span></div>');
                }
                if (religion.nivel != false) {
                    $('.religionContainer').append('<div class="toRemove"><span class="nombreRasgo"> Compromiso: </span><span>' + religion.nivel + '</span></div>');
                }

                // Rasgos
                if (rasgos.especiales != false) {
                    $('.rasgosContainer').append('<div class="toRemove"><span class="nombreRasgo"> Especiales: </span><span>' + rasgos.especiales + '</span></div>');
                }
                if (rasgos.psicologicos != false) {
                    $('.rasgosContainer').append('<div class="toRemove"><span class="nombreRasgo"> Psicológicos: </span><span>' + rasgos.psicologicos + '</span></div>');
                }
                if (rasgos.fisicos != false) {
                    $('.rasgosContainer').append('<div class="toRemove"><span class="nombreRasgo"> Físicos: </span><span>' + rasgos.fisicos + '</span></div>');
                }
                if (rasgos.motivacionales != false) {
                    $('.rasgosContainer').append('<div class="toRemove"><span class="nombreRasgo"> Motivacionales: </span><span>' + rasgos.motivacionales + '</span></div>');
                }

                // Eventos
                if (eventos.personal != false) {
                    $('.eventosContainer').append('<div class="toRemove"><span class="nombreRasgo"> Personal: </span><span>' + eventos.personal + '</span></div>');
                }
                if (eventos.familiar != false) {
                    $('.eventosContainer').append('<div class="toRemove"><span class="nombreRasgo"> Familiar: </span><span>' + eventos.familiar + '</span></div>');
                }
                if (eventos.social != false) {
                    $('.eventosContainer').append('<div class="toRemove"><span class="nombreRasgo"> Social: </span><span>' + eventos.social + '</span></div>');
                }
                if (eventos.guerra != false) {
                    $('.eventosContainer').append('<div class="toRemove"><span class="nombreRasgo"> En la guerra: </span><span>' + eventos.guerra + '</span></div>');
                }
                if (eventos.dinero != false) {
                    $('.eventosContainer').append('<div class="toRemove"><span class="nombreRasgo"> Dinero: </span><span>' + eventos.dinero + '</span></div>');
                }
                if (eventos.fisicos != false) {
                    $('.eventosContainer').append('<div class="toRemove"><span class="nombreRasgo"> Físicos: </span><span>' + eventos.fisicos + '</span></div>');
                }

                // Familia
                // Hermanos
                if (familia.hermanos != false || familia.hermanos != 0) {
                    $('.hermanosContainer').append('<div class="toRemove"><span class="nombreRasgo"> Hermanos: </span><span>' + familia.hermanos + '</span></div>');
                    imprimirHermano('hermano 1 ', familia.hermano1, $('.hermanosContainer'));
                    imprimirHermano('hermano 2 ', familia.hermano2, $('.hermanosContainer'));
                    imprimirHermano('hermano 3 ', familia.hermano3, $('.hermanosContainer'));
                    imprimirHermano('hermano 4 ', familia.hermano4, $('.hermanosContainer'));
                    imprimirHermano('hermano 5 ', familia.hermano5, $('.hermanosContainer'));
                    imprimirHermano('hermano 6 ', familia.hermano6, $('.hermanosContainer'));
                    imprimirHermano('hermano 7 ', familia.hermano7, $('.hermanosContainer'));
                    imprimirHermano('hermano 8 ', familia.hermano8, $('.hermanosContainer'));
                    imprimirHermano('hermano 9 ', familia.hermano9, $('.hermanosContainer'));
                    imprimirHermano('hermano 10 ', familia.hermano10, $('.hermanosContainer'));

                }
                // Pareja
                if (familia.pareja != false) {
                    $('.parejaContainer').append('<div class="toRemove"><span class="nombreRasgo"> Pareja: </span><span>' + familia.pareja + '</span></div>');
                }
                if (familia.pareja2 != false) {
                    $('.parejaContainer').append('<div class="toRemove"><span class="nombreRasgo"> Pareja 2: </span><span>' + familia.pareja2 + '</span></div>');
                }
                if (familia.pareja3 != false) {
                    $('.parejaContainer').append('<div class="toRemove"><span class="nombreRasgo"> Pareja 3: </span><span>' + familia.pareja3 + '</span></div>');
                }
                if (familia.pareja4 != false) {
                    $('.parejaContainer').append('<div class="toRemove"><span class="nombreRasgo"> Pareja 4: </span><span>' + familia.pareja4 + '</span></div>');
                }
                if (familia.pareja5 != false) {
                    $('.parejaContainer').append('<div class="toRemove"><span class="nombreRasgo"> Pareja 5: </span><span>' + familia.pareja5 + '</span></div>');
                }
                if (familia.pareja6 != false) {
                    $('.parejaContainer').append('<div class="toRemove"><span class="nombreRasgo"> Pareja 6: </span><span>' + familia.pareja6 + '</span></div>');
                }
                // Amante
                if (familia.amante != false) {
                    $('.parejaContainer').append('<div class="toRemove"><span class="nombreRasgo"> Amante: </span><span>' + familia.amante + '</span></div>');
                }


                // Hijos
                if (familia.hijos != false || familia.hijos != 0) {
                    $('.hijosContainer').append('<div class="toRemove"><span class="nombreRasgo"> Hijos: </span><span>' + familia.hijos + '</span></div>');
                    imprimirHermano('hijo 1 ', familia.hijo1, $('.hijosContainer'));
                    imprimirHermano('hijo 2 ', familia.hijo2, $('.hijosContainer'));
                    imprimirHermano('hijo 3 ', familia.hijo3, $('.hijosContainer'));
                    imprimirHermano('hijo 4 ', familia.hijo4, $('.hijosContainer'));
                    imprimirHermano('hijo 5 ', familia.hijo5, $('.hijosContainer'));
                    imprimirHermano('hijo 6 ', familia.hijo6, $('.hijosContainer'));
                    imprimirHermano('hijo 7 ', familia.hijo7, $('.hijosContainer'));
                    imprimirHermano('hijo 8 ', familia.hijo8, $('.hijosContainer'));
                    imprimirHermano('hijo 9 ', familia.hijo9, $('.hijosContainer'));
                    imprimirHermano('hijo 10 ', familia.hijo10, $('.hijosContainer'));
                }

                // Parientes Lejanos
                if (familia.lejanos != false) {
                    $('.lejanosContainer').append('<div class="toRemove"><span class="nombreRasgo"> Relacion: </span><span>' + familia.lejanos + '</span></div>');
                }

                $('.nombreRasgo + span').each(function() {
                    $(this).after('<button class="removeElement">Eliminar</button>');

                });


            });
        }

    });




});
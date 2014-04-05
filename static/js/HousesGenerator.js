$(document).ready(function() {



    $('#submitHouses').on('click', function() {
        var selectedRealm = $('#selectRealm').val();
        var houseName = $('#houseName').val();
        var houseSize = $('#houseSize').val();
        var houseFoundation = $('#houseFoundation').val();

        /****
       	BORRAMOS EL CONTENIDO PREVIO
       	****/
        /*
        $('#houseStats').empty();
        $('#houseEvents').empty();
        $('#defenseHoldings').empty();
        */
        $('.houseDataSection').each(function() {
            $(this).empty();
        });


        houseData = {
            'name': houseName,
            'realm': selectedRealm,
            'size': houseSize,
            'foundation': houseFoundation
        }
        console.log('envio');
        console.log(houseData);

        /****************
        FUNCION QUE SOLICITA E IMPRIME LA DATA
        ****************/
        $.getJSON('/houseGenerator', houseData, function(dataRecibida) {
            console.log('recibí:');
            console.log(dataRecibida);

            $('#houseStats').append('<span class="houseStat houseDefense"> Defense: ' + dataRecibida.defense + '</span><span class="">Puntos sobrantes:' + dataRecibida.remainingDefense + '</span>');
            $('#houseStats').append('<span class="houseStat houseDefense"> Influence: ' + dataRecibida.influence + '</span><span class="">Puntos sobrantes:' + dataRecibida.remainingInfluence + '</span>');
            $('#houseStats').append('<span class="houseStat houseDefense"> Lands: ' + dataRecibida.lands + '</span>');
            $('#houseStats').append('<span class="houseStat houseDefense"> Law: ' + dataRecibida.law + '</span>');
            $('#houseStats').append('<span class="houseStat houseDefense"> Population: ' + dataRecibida.population + '</span>');
            $('#houseStats').append('<span class="houseStat houseDefense"> Power: ' + dataRecibida.power + '</span>');
            $('#houseStats').append('<span class="houseStat houseDefense"> Wealth: ' + dataRecibida.wealth + '</span>');


            for (var i = 0; i < dataRecibida.events.length; i++) {
                $('#houseEvents').append('<span class="houseStat houseEvent"> Evento: ' + dataRecibida.events[i] + '</span>');
            }

            for (var j = 0; j < dataRecibida.defenseHoldings.length; j++) {
                $('#defenseHoldings').append('<span class="defenseHoldings">' + dataRecibida.defenseHoldings[j] + '</span>');
            }
            $('#influenceHoldings').append('<span>Max Head of the House Status: ' + dataRecibida.maxStatus + '</span>');
            for (var i = 0; i < dataRecibida.influenceHoldings.length; i++) {
                $('#influenceHoldings').append('<span class="influenceHoldings">' + dataRecibida.influenceHoldings[i] + '</span>');
            }





        });
    });

});
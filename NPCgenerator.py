# -*- coding: utf-8 -*-
from random import randint

eventosGenerales = {"personales": [
    "exiliado/a de su hogar",
    "estuvo un tiempo perdido/a vagando",
    "fue secuestrado/a y se escapó",
    "fue secuestrado/a y pagaron el rescate",
    "fue secuestrado/a y se unió a los secuestradores luego de un tiempo",
    "es amado/a por alguien importante",
    "es amado/a por alguien que el desconoce",
    "fue amado/a por alguien importante",
    "tiene un secreto que le podría valer la muerte",
    "tiene un secreto que le traería muchos problemas",
    "viajó mucho tiempo",
    "viajó por toda la región",
    "viaja constantemente",
],
    "familiares": (
        "hubo una importante muerte en la familia",
        "hubo un importante matrimonio en la familia",
        "recibió una herencia",
        "el estatus familiar vivió un aumento",
        "el estatus familiar sufrió un descenso",
        "es bastardo/a",
        "es bastardo/a reconocido",
        "existe un importante cisma familiar",
        "existe una familia rival"
    ),
    "sociales": [
        "participó en una revuelta",
        "es infame",
        "es famoso/a",
        "es un/a lider en su grupo humano",
        "tiene un título reconocible",
    ],
    "guerra": [
        "mató por primera vez en una guerra y lo/a marcó",
        "sufrió una herida en la guerra",
        "obtuvo reconocimiento por algún acto durante la guerra",
        "organizó a un grupo importante durante la guerra",
        "hizo negocios durante la guerra",
        "ayudó a resolver un conflicto durante la guerra",
        "fue un saqueador/a durante la guerra",
        "se avergüenza de los actos que realizó durante la guerra",
        "fué violado/a durante la guerra"
    ],
    "dinero": (
        "perdió algo",
        "perdió mucho",
        "ganó algo",
        "ganó mucho",
        "es comerciante",
        "tiene un rentable negocio",
        "heredó una fortuna"
    ),
    "fisicos": (
        "sufrió una lesión grave que lo/a incapacita",
        "sufrió una lesión media que es muy notoria",
        "sufrió una lesión leve que puede ocultar",
        "fue mutilado/a"
    )
}

eventosHombre = {
    "personales": (
        "ha estudiado formalmente",
        "ha aprendido un oficio"
    ),
    "sociales": (
        "es caballero o su equivalente",
    ),
    "guerra": (
        "luchó en una guerra",
        "desertó en una guerra",
        "tiene un grupo de hermanos de armas que data de esos tiempos\
        le protegen"
    )
}
eventosMujer = {
    "personales": (
        "ha aprendido alguna habilidad manual que le permite trabajar",
        "es o ha sido prostituta",
        "ha sido o ha asistido a una partera"
    ),
    "sociales": (
        "es considerada una bruja",
    ),
    "guerra": (
        "quedó embarazada durante la guerra, no sabe quien es el padre",
        "quedó embarazada durante la guerra, el padre era del bando enemigo",
        "quedó embarazada durante la guerra, el padre er de su bando"
    )
}

religion = {
    "creencia": (
        "Los Siete: La Madre",
        "Los Siete: El Padre",
        "Los Siete: El Herrero",
        "Los Siete: La Anciana",
        "Los Siete: La Doncella",
        "Los Siete: El Guerrero",
        "Los Siete: El Extraño",
        "Dios regional (dioses antiguos, Dios ahogado, espiritus oscuros,\
        etc)",
        "r\'hllor",
        "many faces",
        "otra",
        "no se sabe",
        "ateo"
    ),
    "nivel": (
        "practica su fé con fervor",
        "es procelitista",
        "creció creyendo en su fé, no la cuestiona",
        "su fé es muy importante para el/ella",
        "aunque dice ser creyente no es algo que tenga presente",
        "no se cuestiona su fé",
        "realmente no cree en su fé",
        "mas que creyente o practicante es superticioso/a",
        "vive su fé como una carga que no le permite ser libre",
        "su fé es una tradición familiar"
    )


}

familia = {
    "hermanos": (
        "mayor",
        "menor",
        "gemelo",
        "mellizo",
        "bastardo"
    ),
    "pareja": (
        "algo mayor que el/ella",
        "algo menor que el/ella",
        "mucho mayor que el/ella",
        "mucho menor que el/ella",
        "murió",
        "escapó por maltrato",
        "escapó con amante",
        "desapareció",
        "le es infiel y el/ella lo sabe",
        "le es infiel y el/ella no lo sabe"
    ),
    "amante": (
        "tiene pareja homosexual",
        "desde hace años",
        "tiene mutiples parejas",
        "es de status y lo/a mantiene",
        "le paga todo a su amante",
        "es un secreto a voces",
        "es sabido por todos",
        "es una relación reconocida"
    ),
    "hijos": (
        "vivo",
        "muerto",
        "enfermo",
        "lesionado",
        "digno",
        "indigno",
        "bastardo no reconocido",
        "bastardo reconocido",
        "adoptivo",
        "no lo sabe",
        "viviendo en otro lugar",
        "aprendiendo un oficio",
        "aprendiendo de él",
        "en alguna organización religiosa",
        "en alguna organización militar",
        "en alguna organización específica"
    ),
    "lejanos": (
        "mantienen una mala relación",
        "mantienen una buena relación",
        "a los que ha conocido recientemente",
        "no mantienen relación",
        "grandiosos y o famosos",
        "despreciables"
    )
}

rasgos = {
    "especiales": (
        "le gustá algún juego en particular (cyvasse, dominó, etc)",
        "colecciona algun tipo de objeto como hobbie",
        "practica algún deporte con pasión",
        "es muy habil en algo",
        "tiene un defecto que prefiere ocultar",
        "tiene un amigo importante",
        "greensight",
        "warg",
        "Los animales lo/a respetan",
        "siempre sabe que camino seguir para mantenerse con vida",
        "sabe leer el futuro de alguna manera",
        "es un/a gran cantante",
        "es un/a gran músico",
        "tiene memoria fotográfica",
        "habla muchas lenguas",
        "es clarividente",
    ),
    "psicologicos": (
        "obsesivo/a",
        "nervioso/a",
        "habla sin parar",
        "callado/a",
        "inseguro/a",
        "tiene una fobia",
        "loco/a",
        "agresivo/a",
        "paranoico/a",
        "amigable",
        "confiado/a",
        "inculto/a",
        "inocente",
        "honorable",
        "mentiroso/a",
        "maquinador/a",
        "aprovechado/a",
        "distraído/a",
        "mordaz",
        "astuto/a",
        "cauto/a",
        "piadoso/a",
        "traicionero/a",
        "incorruptible",
        "buen/a negociante",
        "pésimo/a negociante",
        "temperamental",
        "pasional",
        "adicto/a a alguna sustancia (alcohol, hojaroja, etc)",
        "cobarde",
        "olvidadizo/a",
        "supersticioso/a",
        "ha jurado abstinencia sexual",
        "tiene fobia a los genitales del sexo opuesto"

    ),
    "fisicos": (
        "grande",
        "obeso/a"
        "fuerte",
        "voz hipnotizadora",
        "hermoso/a",
        "enano/a",
        "enclenque",
        "delgado/a",
        "paralítico/a",
        "cojo/a",
        "ágil",
        "rápido/a",
        "manco/a",
        "ojos raros",
        "tiene una notable cicatriz",
        "color llamativo de pelo o piel",
        "enfermo/a de algo visible (greyscale, lepra, etc)",
        "enfermo/a de algo no visible (tuberculosis, sífilis, etc)"
        "albino/a",
        "eunuco",
        "esteril",
        "sordo/a",
        "ciego/a",
        "tuerto/a",

    ),
    "motivacionales": (
        "amor",
        "dinero",
        "honor",
        "gloria",
        "provecho",
        "estatus",
        "religión",
        "causa",
        "familia",
        "juramento",
        "hedonismo"
    )
}

dataNPC = {
    "edad": None,
    "genero": None,
    "eventos": {
        "personal": False,
        "familiar": False,
        "social": False,
        "guerra": False,
        "dinero": False,
        "fisicos": False
    },
    "religion": {
        "creencia": False,
        "nivel": False
    },
    "rasgos": {
        "especiales": False,
        "psicologicos": False,
        "fisicos": False,
        "motivacionales": False
    },
    "familia": {
        "hermanos": False,
        "pareja": False,
        "amante": False,
        "hijos": False,
        "lejanos": False,
        "pareja2": False,
        "pareja3": False,
        "pareja4": False,
        "pareja5": False,
        "pareja6": False,
    }
}


class generateNPC(object):

    """se le pasa el diccionario data
    con todos los datos del NPC y estos se rellenan,
    en los casos de familia se buscara generar familiares
    en numero aleatorios"""
    @staticmethod
    def resetearNPC(NPC):
        """Toma como input un objeto JSON especcifico NPC para procesar
        Resetea el objeto para no enviar la misma data"""
        NPC["religion"]["creencia"] = False
        NPC["religion"]["nivel"] = False
        NPC["familia"]["hermanos"] = False
        NPC["familia"]["hijos"] = False
        for evento in NPC["eventos"]:
            NPC["eventos"][evento] = False
        for rasgo in NPC["rasgos"]:
            NPC["rasgos"][rasgo] = False
        for familiar in NPC["familia"]:
            if "hijo" in familiar:
                NPC["familia"][familiar] = False
            if "hermano" in familiar:
                NPC["familia"][familiar] = False
            if familiar == "pareja":
                NPC["familia"]["pareja"] = False
            if familiar == "lejanos":
                NPC["familia"]["lejanos"] = False

    @staticmethod
    def unirDicts(dictToAdd, targetList):
        """ (dict, list) -> list
        agrega los elementos de un dict dentro de los de una lista,
        sirve para generar listas de sucesos segun genero"""
        for key in dictToAdd:
            if key == 'personales':
                for value in dictToAdd[key]:
                    targetList[key].append(value)
            if key == "sociales":
                for value in dictToAdd[key]:
                    targetList[key].append(value)
            if key == "guerra":
                for value in dictToAdd[key]:
                    targetList[key].append(value)

    @staticmethod
    def darGeneroStr(strToMod, genero):
        """ (str, str) -> str
        genero solo acepta como valores validos 'hombre' o 'mujer'
        Reemplaza en todos los textos bi-enero como 'o/a' por 'o' u 'a' ..."""
        if genero == 'mujer':
            if 'o/a' in strToMod:
                string = strToMod.replace('o/a', 'a')
            elif 'el/ella' in strToMod:
                string = strToMod.replace('el/ella', 'ella')
            elif 'un/a' in strToMod:
                string = strToMod.replace('un/a', 'una')
            elif 'r/a' in strToMod:
                string = strToMod.replace('r/a', 'ra')
            elif 'eunuco' in strToMod:
                string = strToMod.replace('eunuco', 'esteril por agresión')
            else:
                return strToMod
            return string
        elif genero == 'hombre':
            if 'o/a' in strToMod:
                string = strToMod.replace('o/a', 'o')
            elif 'el/ella' in strToMod:
                string = strToMod.replace('el/ella', 'él')
            elif 'un/a' in strToMod:
                string = strToMod.replace('un/a', 'un')
            elif 'r/a' in strToMod:
                string = strToMod.replace('r/a', 'r')
            else:
                return strToMod
            return string

    @classmethod
    def generarNPC(_class, genero, edad):
        """ (str, int) -> JSON
        genero solo acepta como valores validos 'hombre' o 'mujer'
        Rellena el Objeto JSON que se enviará con el AJAX.Get request,
         ejecuta todos los comandos de creacion en orden"""
        if genero == 'mujer':
            _class.unirDicts(eventosMujer, eventosGenerales)
        elif genero == 'hombre':
            _class.unirDicts(eventosHombre, eventosGenerales)
        _class.resetearNPC(dataNPC)
        _class.religion(religion, dataNPC, genero)
        _class.rasgos(rasgos, dataNPC, genero)
        _class.eventosGenerales(eventosGenerales, dataNPC, genero)
        _class.familia(familia, dataNPC, genero, edad)
        return dataNPC

    @classmethod
    def singleTupleSelector(_class, tupleToSelect, genero):
        """ (tuple, str) -> str
        selecciona un elemento de un tuple
        para retornarlo como string"""
        num = len(tupleToSelect)
        selected = randint(0, num - 1)
        itemToWrite = tupleToSelect[selected]
        return _class.darGeneroStr(itemToWrite, genero)

    @classmethod
    def religion(_class, religionDict, NPC, genero):
        """ (dict, JSON, str) -> JSON.str
        rellena los datos del JSON de religion
        con la información del dict"""
        for key, value in religionDict.items():
            if key == "creencia":
                NPC["religion"][
                    "creencia"] = _class.singleTupleSelector(value, genero)
            if key == 'nivel':
                NPC["religion"]["nivel"] = _class.singleTupleSelector(
                    value, genero)

    @classmethod
    def rasgos(_class, rasgosDict, NPC, genero):
        """ (dict, JSON, str) -> JSON.str
        elige rasgos con cierta probabilidad y los
        asigna al JSON"""
        for key, value in rasgosDict.items():
            if key == "especiales":
                if randint(1, 100) < 30:
                    NPC["rasgos"][
                        "especiales"] = _class.singleTupleSelector(value, genero)
            if key == "psicologicos":
                if randint(1, 100) < 70:
                    NPC["rasgos"][
                        "psicologicos"] = _class.singleTupleSelector(value, genero)
            if key == "fisicos":
                if randint(1, 100) < 30:
                    NPC["rasgos"][
                        "fisicos"] = _class.singleTupleSelector(value, genero)
            if key == "motivacionales":
                if randint(1, 100) < 80:
                    NPC["rasgos"][
                        "motivacionales"] = _class.singleTupleSelector(value, genero)

    @classmethod
    def eventosGenerales(_class, eventosDict, NPC, genero):
        """(dict, JSON, str) -> JSON.str
        elige aleatoriamente eventos y los asigna al JSON"""
        for key, value in eventosDict.items():
            if key == "personales":
                if randint(1, 100) < 80:
                    NPC["eventos"][
                        "personal"] = _class.singleTupleSelector(value, genero)
            if key == "familiar":
                if randint(1, 100) < 80:
                    NPC["eventos"][
                        "familiar"] = _class.singleTupleSelector(value, genero)
            if key == "social":
                if randint(1, 100) < 80:
                    NPC["eventos"][
                        "social"] = _class.singleTupleSelector(value, genero)
            if key == "guerra":
                if randint(1, 100) < 80:
                    NPC["eventos"][
                        "guerra"] = _class.singleTupleSelector(value, genero)
            if key == "dinero":
                if randint(1, 100) < 80:
                    NPC["eventos"][
                        "dinero"] = _class.singleTupleSelector(value, genero)
            if key == "fisicos":
                if randint(1, 100) < 80:
                    NPC["eventos"][
                        "fisicos"] = _class.singleTupleSelector(value, genero)

    @classmethod
    def familia(_class, familiaDict, NPC, genero, edad=30):
        """(dict, JSON, str, int) -> JSON.str
        Ejecuta al final las funciones internas
        fueron desmembradas para poder pulirlas luego si fuese
        necesario"""

        def hermanos(familiaDict, NPC, edad):
            """(dict, JSON, int) -> JSON.str
            Genera hermanos """
            chanceHermanos = randint(1, 100)
            if chanceHermanos <= 5:
                NPC["familia"]["hermanos"] = randint(6, 10)
            elif 5 < chanceHermanos <= 15:
                NPC["familia"]["hermanos"] = randint(4, 7)
            elif 15 < chanceHermanos <= 40:
                NPC["familia"]["hermanos"] = randint(2, 5)
            elif 40 < chanceHermanos <= 80:
                NPC["familia"]["hermanos"] = randint(1, 3)
            elif 80 < chanceHermanos <= 100:
                NPC["familia"]["hermanos"] = 0
            # ahora rellena para cada hermano generado
            if NPC["familia"]["hermanos"] > 0:
                for hermano in range(NPC["familia"]["hermanos"]):
                    chanceCualidadHermano = randint(1, 100)
                    if chanceCualidadHermano <= 3:
                        NPC["familia"]["hermano" +
                                       str(hermano + 1)] = 'gemelos'
                    elif chanceCualidadHermano <= 7:
                        NPC["familia"]["hermano" +
                                       str(hermano + 1)] = 'mellizos'
                    elif chanceCualidadHermano <= 20:
                        NPC["familia"]["hermano" +
                                       str(hermano + 1)] = 'bastardo (Mayor)'
                    elif chanceCualidadHermano <= 35:
                        NPC["familia"]["hermano" +
                                       str(hermano + 1)] = 'bastardo (Menor)'
                    elif chanceCualidadHermano <= 67:
                        NPC["familia"]["hermano" +
                                       str(hermano + 1)] = 'natural Mayor'
                    elif chanceCualidadHermano <= 100:
                        NPC["familia"]["hermano" +
                                       str(hermano + 1)] = 'natural Menor'

        def pareja(familiaDict, NPC, genero, edad):
            """(dict, JSON, str) -> JSON.str
            determina si se tiene relación marital y además
            extra marital, tmb si se ha vuelto a casar
            """
            chancePareja = randint(1, 100)
            chanceAmante = randint(1, 100)
            if genero == 'mujer' and edad > 12:
                if chancePareja <= 70:
                    NPC["familia"]["pareja"] = _class.singleTupleSelector(
                        familiaDict['pareja'], genero)
                if NPC["familia"]["pareja"] is 'murió' and chancePareja <= 40:
                    NPC["familia"]["pareja2"] = _class.singleTupleSelector(
                        familiaDict['pareja'], genero)
                if NPC["familia"]["pareja2"] is 'murió' and chancePareja <= 10:
                    NPC["familia"]["pareja3"] = _class.singleTupleSelector(
                        familiaDict['pareja'], genero)
                if NPC["familia"]["pareja3"] is 'murió' and chancePareja <= 5:
                    NPC["familia"]["pareja4"] = _class.singleTupleSelector(
                        familiaDict['pareja'], genero)
                if chanceAmante <= 10:
                    NPC["familia"]["amante"] = _class.singleTupleSelector(
                        familiaDict['amante'], genero)

            if genero == 'hombre' and edad > 16:
                if chancePareja <= 70:
                    NPC["familia"]["pareja"] = _class.singleTupleSelector(
                        familiaDict['pareja'], genero)
                if NPC["familia"]["pareja"] is 'murió' and chancePareja <= 60:
                    NPC["familia"]["pareja2"] = _class.singleTupleSelector(
                        familiaDict['pareja'], genero)
                if NPC["familia"]["pareja2"] is 'murió' and chancePareja <= 40:
                    NPC["familia"]["pareja3"] = _class.singleTupleSelector(
                        familiaDict['pareja'], genero)
                if NPC["familia"]["pareja3"] is 'murió' and chancePareja <= 20:
                    NPC["familia"]["pareja4"] = _class.singleTupleSelector(
                        familiaDict['pareja'], genero)
                if NPC["familia"]["pareja4"] is 'murió' and chancePareja <= 10:
                    NPC["familia"]["pareja5"] = _class.singleTupleSelector(
                        familiaDict['pareja'], genero)
                if NPC["familia"]["pareja5"] is 'murió' and chancePareja <= 5:
                    NPC["familia"]["pareja6"] = _class.singleTupleSelector(
                        familiaDict['pareja'], genero)
                if chanceAmante <= 25:
                    NPC["familia"]["amante"] = _class.singleTupleSelector(
                        familiaDict['amante'], genero)

        def hijos(familiaDict, NPC, genero):
            """(dict, JSON, str) -> JSON.str
            genera hijos y los agrega al JSON
            """
            chanceHijos = randint(1, 100)
            if chanceHijos <= 5:
                NPC["familia"]["hijos"] = randint(8, 10)
            elif 5 < chanceHijos <= 15:
                NPC["familia"]["hijos"] = randint(5, 7)
            elif 15 < chanceHijos <= 55:
                NPC["familia"]["hijos"] = randint(2, 5)
            elif 55 < chanceHijos <= 80:
                NPC["familia"]["hijos"] = randint(1, 2)
            elif 80 < chanceHijos <= 100:
                NPC["familia"]["hijos"] = 0
            # rol de los hijos
            if NPC["familia"]["hijos"] > 0:
                for hijo in range(NPC["familia"]["hijos"]):
                    NPC["familia"]["hijo" +
                                   str(hijo + 1)] = _class.singleTupleSelector(familiaDict['hijos'], genero)

        def lejanos(familiaDict, NPC, genero):
            """(dict, JSON, str) -> JSON.str
            agrega elementos del diccionario al json"""
            if randint(1, 4) < 10:
                NPC["familia"][
                    "lejanos"] = _class.singleTupleSelector(familiaDict['lejanos'], genero)

        """Ejecucion de las subfunciones"""
        hermanos(familiaDict, NPC, edad)
        pareja(familiaDict, NPC, genero, edad)
        hijos(familiaDict, NPC, genero)
        lejanos(familiaDict, NPC, genero)

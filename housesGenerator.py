from random import randint
from libraries import rollDices, randomStats


realms = {
    'kingslanding': {
        'defense': 5,
        'influence': -5,
        'lands': -5,
        'law': 20,
        'population': 5,
        'power': -5,
        'wealth': -5
    },
    'dragonstone': {
        'defense': 20,
        'influence': -5,
        'lands': -5,
        'law': 5,
        'population': 0,
        'power': 0,
        'wealth': -5
    },
    'theNorth': {
        'defense': 5,
        'influence': 10,
        'lands': 20,
        'law': -10,
        'population': -5,
        'power': -5,
        'wealth': -5
    },
    'theIronIslands': {
        'defense': 10,
        'influence': -5,
        'lands': -5,
        'law': 0,
        'population': 0,
        'power': 10,
        'wealth': 0
    },
    'theRiverlands': {
        'defense': -5,
        'influence': -5,
        'lands': 5,
        'law': 0,
        'population': 10,
        'power': 0,
        'wealth': 5
    },
    'mountainsOfTheMoon': {
        'defense': 20,
        'influence': 10,
        'lands': -5,
        'law': -10,
        'population': -5,
        'power': 0,
        'wealth': 0
    },
    'theWesternlands': {
        'defense': -5,
        'influence': 10,
        'lands': -5,
        'law': -5,
        'population': -5,
        'power': 0,
        'wealth': 20
    },
    'theReach': {
        'defense': -5,
        'influence': 10,
        'lands': 0,
        'law': -5,
        'population': 5,
        'power': 0,
        'wealth': 5
    },
    'theStormlands': {
        'defense': 5,
        'influence': 0,
        'lands': -5,
        'law': 10,
        'population': -5,
        'power': 5,
        'wealth': 0
    },
    'dorne': {
        'defense': 0,
        'influence': -5,
        'lands': 10,
        'law': -5,
        'population': 0,
        'power': 10,
        'wealth': 0
    }
}

eventsData = {
    3: {
        'name': 'Doom',
        'defense': rollDices(6, 2) * -1,
        'influence': rollDices(6, 2) * -1,
        'lands': rollDices(6, 2) * -1,
        'law': rollDices(6, 2) * -1,
        'population': rollDices(6, 2) * -1,
        'power': rollDices(6, 2) * -1,
        'wealth': rollDices(6, 2) * -1
    },
    4: {
        'name': 'Defeat',
        'defense': rollDices(6, 1) * -1,
        'influence': rollDices(6, 1) * -1,
        'lands': rollDices(6, 1) * -1,
        'law': 0,
        'population': rollDices(6, 1) * -1,
        'power': rollDices(6, 1) * -1,
        'wealth': rollDices(6, 1) * -1
    },
    5: {
        'name': 'Catastrophe',
        'defense': 0,
        'influence': 0,
        'lands': 0,
        'law': rollDices(6, 1) * -1,
        'population': rollDices(6, 1) * -1,
        'power': rollDices(6, 1) * -1,
        'wealth': rollDices(6, 1) * -1
    },
    6: {
        'name': 'Madness',
        'defense': (rollDices(6, 2) * -1) + 6,
        'influence': (rollDices(6, 2) * -1) + 6,
        'lands': (rollDices(6, 2) * -1) + 6,
        'law': (rollDices(6, 2) * -1) + 6,
        'population': (rollDices(6, 2) * -1) + 6,
        'power': (rollDices(6, 2) * -1) + 6,
        'wealth': (rollDices(6, 2) * -1) + 6
    },
    7: {
        'name': 'Invasion/Revolt',
        'defense': 0,
        'influence': 0,
        'lands': 0,
        'law': rollDices(6, 2) * -1,
        'population': rollDices(6, 1) * -1,
        'power': rollDices(6, 1) * -1,
        'wealth': rollDices(6, 1) * -1
    },
    8: {
        'name': 'Scandal',
        'defense': 0,
        'influence': rollDices(6, 1) * -1,
        'lands': rollDices(6, 1) * -1,
        'law': 0,
        'population': 0,
        'power': rollDices(6, 1) * -1,
        'wealth': 0
    },
    9: {
        'name': 'Treachery',
        'defense': 0,
        'influence': rollDices(6, 1) * -1,
        'lands': 0,
        'law': rollDices(6, 1) * -1,
        'population': 0,
        'power': rollDices(6, 1) * -1,
        'wealth': 0
    },
    10: {
        'name': 'Decline',
        'defense': 0,
        'influence': rollDices(6, 1) * -1,
        'lands': rollDices(6, 1) * -1,
        'law': 0,
        'population': 0,
        'power': rollDices(6, 1) * -1,
        'wealth': rollDices(6, 1) * -1
    },
    11: {
        'name': 'Infrastructure',
        'defense': 0,
        'influence': 0,
        'lands': 0,
        'law': 0,
        'population': 0,
        'power': 0,
        'wealth': 0
    },
    12: {
        'name': 'Ascent',
        'defense': 0,
        'influence': rollDices(6, 1),
        'lands': rollDices(6, 1),
        'law': 0,
        'population': 0,
        'power': rollDices(6, 1),
        'wealth': rollDices(6, 1)
    },
    13: {
        'name': 'Favor',
        'defense': 0,
        'influence': rollDices(6, 1),
        'lands': rollDices(6, 1),
        'law': rollDices(6, 1),
        'population': 0,
        'power': rollDices(6, 1),
        'wealth': 0
    },
    14: {
        'name': 'Victory',
        'defense': rollDices(6, 1),
        'influence': rollDices(6, 1),
        'lands': 0,
        'law': 0,
        'population': 0,
        'power': rollDices(6, 1),
        'wealth': 0
    },
    15: {
        'name': 'Villain',
        'defense': 0,
        'influence': rollDices(6, 1),
        'lands': 0,
        'law': rollDices(6, 1) * -1,
        'population': rollDices(6, 1) * -1,
        'power': rollDices(6, 1),
        'wealth': 0
    },
    16: {
        'name': 'Glory',
        'defense': rollDices(6, 1),
        'influence': rollDices(6, 1),
        'lands': 0,
        'law': rollDices(6, 1),
        'population': 0,
        'power': rollDices(6, 1),
        'wealth': 0
    },
    17: {
        'name': 'Conquest',
        'defense': rollDices(6, 1) * -1,
        'influence': rollDices(6, 1),
        'lands': rollDices(6, 1),
        'law': rollDices(6, 1) * -1,
        'population': rollDices(6, 1),
        'power': 0,
        'wealth': rollDices(6, 1)
    },
    18: {
        'name': 'Widnfall',
        'defense': rollDices(6, 1),
        'influence': rollDices(6, 2),
        'lands': rollDices(6, 1),
        'law': rollDices(6, 1),
        'population': rollDices(6, 1),
        'power': rollDices(6, 2),
        'wealth': rollDices(6, 2)
    }
}

foundationList = ('ancient', 'veryOld', 'old', 'established', 'recent', 'new')
houseData = {}


class House(object):

    # Hay que pasarlelos parametros para generarlo
    def __init__(self, realm=None, size=None, foundation=None, name=None):
        self.name = name
        self.realm = realm
        self.size = size
        self.foundation = foundation

    @staticmethod
    def startingResources(realm,
                          size,
                          foundation,
                          name,
                          houseDict=houseData
                          ):
        '''(str, str) -> Object properties
        generates the initial values for the house'''

        # Size of the house, int = number of 1D6 dices to roll
        if size == 'small':
            numOfDices = 7
        elif size == 'medium':
            numOfDices = 9
        elif size == 'large':
            numOfDices = 12
        elif size == 'famous':
            numOfDices = 16
        elif size == 'warden':
            numOfDices = 25

        # modify stats according to realm
        for key, modifier in realms.items():
            if key == realm:
                houseDict['defense'] = rollDices(
                    6, numOfDices) + realms[key]['defense']
                houseDict['influence'] = rollDices(
                    6, numOfDices) + realms[key]['influence']
                houseDict['lands'] = rollDices(
                    6, numOfDices) + realms[key]['lands']
                houseDict['law'] = rollDices(
                    6, numOfDices) + realms[key]['law']
                houseDict['population'] = rollDices(
                    6, numOfDices) + realms[key]['population']
                houseDict['power'] = rollDices(
                    6, numOfDices) + realms[key]['power']
                houseDict['wealth'] = rollDices(
                    6, numOfDices) + realms[key]['wealth']

        # Ancientness of the house
        if foundation == 'random':
            foundation = foundationList[randint(0, len(foundationList) - 1)]
        if foundation == 'ancient':
            historicalEvents = abs(rollDices(6, 1) + 3)
        elif foundation == 'veryOld':
            historicalEvents = abs(rollDices(6, 1) + 2)
        elif foundation == 'old':
            historicalEvents = abs(rollDices(6, 1) + 1)
        elif foundation == 'established':
            historicalEvents = abs(rollDices(6, 1))
        elif foundation == 'recent':
            historicalEvents = abs(rollDices(6, 1) - 1)
        elif foundation == 'new':
            historicalEvents = abs(rollDices(6, 1) - 2)

        # modify stats according to events
        houseDict['events'] = []
        for event in range(historicalEvents):
            rolledEvent = rollDices(6, 3)
            houseDict['events'].append(eventsData[rolledEvent]['name'])
            if rolledEvent == 11:
                # generar funcion de seleccion de dos items aleatorios
                randomStats(2, houseDict)

            else:
                houseDict['defense'] += eventsData[rolledEvent]['defense']
                houseDict['influence'] += eventsData[rolledEvent]['influence']
                houseDict['lands'] += eventsData[rolledEvent]['lands']
                houseDict['law'] += eventsData[rolledEvent]['law']
                houseDict[
                    'population'] += eventsData[rolledEvent]['population']
                houseDict['power'] += eventsData[rolledEvent]['power']
                houseDict['wealth'] += eventsData[rolledEvent]['wealth']

        # this works because a str() always returns False when checking
        # if it's smaller than an int() and True otherwise
        for key, value in houseDict.iteritems():
            if value < 0:
                houseDict[key] = 0

        return houseDict

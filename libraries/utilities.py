from random import randint


def rollDices(diceType, numOfDices):
    '''(int, int) -> int
    Takes a a diceType (max value for a roll) and a number
    of dices to roll
    returns the sum of the rolled dices and applies it to a stat'''
    result = 0
    for dice in range(numOfDices):
        result += randint(1, diceType)
    return result


def randomStats(numStats, statsDict):
    '''(int, dict)->dict.value
    from a num of stats in a dict, increases such a number'''
    for stat in range(numStats):
        key = statsDict.items()[stat][0]  # += rollDices(6, 1)
        statsDict[key] += rollDices(6, 1)
        
    

'''
_dict = {
    'defense': 20,
    'influence': -5,
    'lands': -5,
    'law': 5,
    'population': 0,
    'power': 0,
    'wealth': -5
}

randomStats(2, _dict)
'''
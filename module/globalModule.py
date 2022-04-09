# GLOBAL MODULE

import module.globalModule as Global


def convertGameId(number):
    if (number // 10 == 0):
        return str("GAME00" + str(number))
    elif (1 <= number // 10 <= 9):
        return str("GAME0" + str(number))
    elif (10 <= number // 10):
        return str("GAME" + str(number))


def displayGameCharacters(string, length):
    finalString = ""
    if (Global.length(string) > length):
        for i in range(length - 4):
            finalString += string[i]
        finalString += " ..."
    else:
        nSpace = length - Global.length(string)
        finalString = string
        for i in range(nSpace):
            finalString += " "
    return finalString


def length(object):
    count = 0
    for i in object:
        count += 1
    return count

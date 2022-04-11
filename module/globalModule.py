# GLOBAL MODULE

import module.globalModule as Global


def convertGameId(number):
    if (number // 10 == 0):
        return str("GAME00" + str(number))
    elif (1 <= number // 10 <= 9):
        return str("GAME0" + str(number))
    elif (10 <= number // 10):
        return str("GAME" + str(number))


def convertGameIdReverse(id):
    number = id[4] + id[5] + id[6]
    return str(int(number))


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


# len()
def length(object):
    count = 0
    for i in object:
        count += 1
    return count


# split()
def seperate(string, word):
    elements = 1
    for i in range(len(string)):
        if (string[i] == word):
            elements += 1

    list = ["" for i in range(elements)]
    listIndex = 0
    for i in range(len(string)):
        if (string[i] == word):
            listIndex += 1
        else:
            list[listIndex] += string[i]
    return list


# replace()
def Replace(string, initialCharacter, finalCharacter):
    listedString = ["" for i in range(len(string))]
    for i in range(len(string)):
        listedString[i] = string[i]

    for i in range(len(listedString)):
        if (listedString[i] == initialCharacter):
            listedString[i] = finalCharacter

    string = ""
    for i in range(len(listedString)):
        string += listedString[i]

    return string

# append()


def Append(list, newElement):
    temp = ["" for i in range(length(list) + 1)]
    for i in range(length(list)):
        temp[i] = list[i]
    temp[length(list)] = newElement
    return temp

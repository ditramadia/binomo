# GLOBAL MODULE

def convertGameId(number):
    if (number // 10 == 0):
        return f"GAME00{number}"
    elif (1 <= number // 10 <= 9):
        return f"GAME0{number}"
    elif (10 <= number // 10):
        return f"GAME{number}"


def displayGameCharacters(string, length):
    finalString = ""
    if (len(string) > length):
        for i in range(length - 4):
            finalString += string[i]
        finalString += " ..."
    else:
        nSpace = length - len(string)
        finalString = string
        for i in range(nSpace):
            finalString += " "
    return finalString

# SEARCH GAME TOKO MODULE

import module.globalModule as Global


def SearchGameToko(gameData):
    idInput = str(input("Masukkan ID Game: "))
    nameInput = str(input("Masukkan Nama Game: "))
    priceInput = str(input("Masukkan Harga Game: "))
    categoryInput = str(input("Masukkan Kategori Game: "))
    releaseInput = str(input("Masukkan Tahun Rilis Game: "))

    matchList = ["" for i in range(Global.length(gameData) - 1)]
    for i in range(Global.length(gameData) - 1):
        matchList[i] = gameData[i + 1][0]

    matchList = filterId(gameData, matchList, idInput)
    matchList = filterName(gameData, matchList, nameInput)
    matchList = filterPrice(gameData, matchList, priceInput)
    matchList = filterCategory(gameData, matchList, categoryInput)
    matchList = filterRelease(gameData, matchList, releaseInput)

    print("Daftar game pada toko yang memenuhi kriteria:")
    for i in range(Global.length(matchList)):
        print(f'{i + 1}. {matchList[i]} | {Global.displayGameCharacters(gameData[int(Global.convertGameIdReverse(matchList[i]))][1], 25)} | {Global.displayGameCharacters(gameData[int(Global.convertGameIdReverse(matchList[i]))][4], 7)} | {Global.displayGameCharacters(gameData[int(Global.convertGameIdReverse(matchList[i]))][2], 20)} | {gameData[int(Global.convertGameIdReverse(matchList[i]))][3]} | {gameData[int(Global.convertGameIdReverse(matchList[i]))][5]}')


def filterId(gameData, matchList, idInput):
    if (Global.length(idInput) == 0):
        return matchList
    else:
        return [gameData[int(Global.convertGameIdReverse(idInput))][0]]


def filterName(gameData, matchList, nameInput):
    if (Global.length(nameInput) == 0):
        return matchList
    else:
        for i in range(Global.length(matchList)):
            if (nameInput not in gameData[int(Global.convertGameIdReverse(matchList[i]))][1]):
                matchList[i] = "x"
            else:
                pass

        i = 0
        while "x" in matchList:
            if (matchList[i] == "x"):
                matchList.pop(i)
            else:
                i += 1

        return matchList


def filterPrice(gameData, matchList, priceInput):
    if (Global.length(priceInput) == 0):
        return matchList
    else:
        for i in range(Global.length(matchList)):
            if (priceInput != gameData[int(Global.convertGameIdReverse(matchList[i]))][4]):
                matchList[i] = "x"
            else:
                pass

        i = 0
        while "x" in matchList:
            if (matchList[i] == "x"):
                matchList.pop(i)
            else:
                i += 1

        return matchList


def filterCategory(gameData, matchList, categoryInput):
    if (Global.length(categoryInput) == 0):
        return matchList
    else:
        for i in range(Global.length(matchList)):
            if (categoryInput not in gameData[int(Global.convertGameIdReverse(matchList[i]))][2]):
                matchList[i] = "x"
            else:
                pass

        i = 0
        while "x" in matchList:
            if (matchList[i] == "x"):
                matchList.pop(i)
            else:
                i += 1

        return matchList


def filterRelease(gameData, matchList, releaseInput):
    if (Global.length(releaseInput) == 0):
        return matchList
    else:
        for i in range(Global.length(matchList)):
            if (releaseInput != gameData[int(Global.convertGameIdReverse(matchList[i]))][3]):
                matchList[i] = "x"
            else:
                pass

        i = 0
        while "x" in matchList:
            if (matchList[i] == "x"):
                matchList.pop(i)
            else:
                i += 1

        return matchList

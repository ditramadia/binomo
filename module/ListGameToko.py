# LIST GAME TOKO MODULE

import module.globalModule as Global


def ListGameToko(gameData):
    sorting = str(input("Skema sorting: "))
    while not isSortingValid(sorting):
        print("Skema sorting tidak valid!")
        sorting = str(input("Skema sorting: "))

    if (sorting == "harga+"):
        ListGameHargaAscending(gameData)
    elif (sorting == "harga-"):
        ListGameHargaDescending(gameData)
    elif (sorting == "tahun+"):
        ListGameTahunAscending(gameData)
    elif (sorting == "tahun-"):
        ListGameTahunDescending(gameData)


def isSortingValid(sorting):
    if (sorting == "tahun-" or sorting == "tahun+" or sorting == "harga-" or sorting == "harga+"):
        return True
    else:
        False


def ListGameHargaAscending(gameData):
    gameDataTemp = ["" for i in range(Global.length(gameData) - 1)]
    for i in range(Global.length(gameData) - 1):
        gameDataTemp[i] = gameData[i + 1][0]

    listNumber = 0
    while Global.length(gameDataTemp) > 0:
        lowestPriceGame = updateTempGame(gameDataTemp[0], gameData)
        for i in range(Global.length(gameDataTemp) - 1):
            if (int(lowestPriceGame[4]) > int(gameData[int(Global.convertGameIdReverse(gameDataTemp[i + 1]))][4])):
                lowestPriceGame = updateTempGame(
                    gameDataTemp[i + 1], gameData)

        gameId = lowestPriceGame[0]
        gameName = lowestPriceGame[1]
        gamePrice = lowestPriceGame[4]
        gameCategory = lowestPriceGame[2]
        gameRelease = lowestPriceGame[3]
        gameStock = lowestPriceGame[5]

        print(
            f"{listNumber + 1}. {gameId} | {Global.displayGameCharacters(gameName, 25)} | {Global.displayGameCharacters(gamePrice, 7)} | {Global.displayGameCharacters(gameCategory, 20)} | {gameRelease} | {gameStock} ")

        gameDataTemp.remove(gameId)
        listNumber += 1


def ListGameHargaDescending(gameData):
    gameDataTemp = ["" for i in range(Global.length(gameData) - 1)]
    for i in range(Global.length(gameData) - 1):
        gameDataTemp[i] = gameData[i + 1][0]

    listNumber = 0
    while Global.length(gameDataTemp) > 0:
        highestPriceGame = updateTempGame(gameDataTemp[0], gameData)
        for i in range(Global.length(gameDataTemp) - 1):
            if (int(highestPriceGame[4]) < int(gameData[int(Global.convertGameIdReverse(gameDataTemp[i + 1]))][4])):
                highestPriceGame = updateTempGame(
                    gameDataTemp[i + 1], gameData)

        gameId = highestPriceGame[0]
        gameName = highestPriceGame[1]
        gamePrice = highestPriceGame[4]
        gameCategory = highestPriceGame[2]
        gameRelease = highestPriceGame[3]
        gameStock = highestPriceGame[5]

        print(
            f"{listNumber + 1}. {gameId} | {Global.displayGameCharacters(gameName, 25)} | {Global.displayGameCharacters(gamePrice, 7)} | {Global.displayGameCharacters(gameCategory, 20)} | {gameRelease} | {gameStock} ")

        gameDataTemp.remove(gameId)
        listNumber += 1


def ListGameTahunAscending(gameData):
    gameDataTemp = ["" for i in range(Global.length(gameData) - 1)]
    for i in range(Global.length(gameData) - 1):
        gameDataTemp[i] = gameData[i + 1][0]

    listNumber = 0
    while Global.length(gameDataTemp) > 0:
        lowestReleaseGame = updateTempGame(gameDataTemp[0], gameData)
        for i in range(Global.length(gameDataTemp) - 1):
            if (int(lowestReleaseGame[3]) > int(gameData[int(Global.convertGameIdReverse(gameDataTemp[i + 1]))][3])):
                lowestReleaseGame = updateTempGame(
                    gameDataTemp[i + 1], gameData)

        gameId = lowestReleaseGame[0]
        gameName = lowestReleaseGame[1]
        gamePrice = lowestReleaseGame[4]
        gameCategory = lowestReleaseGame[2]
        gameRelease = lowestReleaseGame[3]
        gameStock = lowestReleaseGame[5]

        print(
            f"{listNumber + 1}. {gameId} | {Global.displayGameCharacters(gameName, 25)} | {Global.displayGameCharacters(gamePrice, 7)} | {Global.displayGameCharacters(gameCategory, 20)} | {gameRelease} | {gameStock} ")

        gameDataTemp.remove(gameId)
        listNumber += 1


def ListGameTahunDescending(gameData):
    gameDataTemp = ["" for i in range(Global.length(gameData) - 1)]
    for i in range(Global.length(gameData) - 1):
        gameDataTemp[i] = gameData[i + 1][0]

    listNumber = 0
    while Global.length(gameDataTemp) > 0:
        highestReleaseGame = updateTempGame(gameDataTemp[0], gameData)
        for i in range(Global.length(gameDataTemp) - 1):
            if (int(highestReleaseGame[3]) < int(gameData[int(Global.convertGameIdReverse(gameDataTemp[i + 1]))][3])):
                highestReleaseGame = updateTempGame(
                    gameDataTemp[i + 1], gameData)

        gameId = highestReleaseGame[0]
        gameName = highestReleaseGame[1]
        gamePrice = highestReleaseGame[4]
        gameCategory = highestReleaseGame[2]
        gameRelease = highestReleaseGame[3]
        gameStock = highestReleaseGame[5]

        print(
            f"{listNumber + 1}. {gameId} | {Global.displayGameCharacters(gameName, 25)} | {Global.displayGameCharacters(gamePrice, 7)} | {Global.displayGameCharacters(gameCategory, 20)} | {gameRelease} | {gameStock} ")

        gameDataTemp.remove(gameId)
        listNumber += 1


def updateTempGame(gameId, gameData):
    gameIdInt = int(Global.convertGameIdReverse(gameId))
    return [gameData[gameIdInt][0], gameData[gameIdInt][1], gameData[gameIdInt][2], gameData[gameIdInt][3], gameData[gameIdInt][4], gameData[gameIdInt][5]]

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
    gameDataTemp = ["" for i in range(Global.length(gameData))]
    for i in range(Global.length(gameData)):
        gameDataTemp[i] = gameData[Global.convertGameId(i + 1)]["id"]

    listNumber = 0
    while Global.length(gameDataTemp) > 0:
        lowestPriceGame = updateTempGame(gameDataTemp[0], gameData)
        for i in range(Global.length(gameDataTemp) - 1):
            if (int(lowestPriceGame["harga"]) > int(gameData[gameDataTemp[i + 1]]["harga"])):
                lowestPriceGame = updateTempGame(
                    gameDataTemp[i + 1], gameData)

        gameId = lowestPriceGame["id"]
        gameName = lowestPriceGame["nama"]
        gamePrice = lowestPriceGame["harga"]
        gameCategory = lowestPriceGame["kategori"]
        gameRelease = lowestPriceGame["tahun_rilis"]
        gameStock = lowestPriceGame["stok"]

        print(
            f"{listNumber + 1}. {gameId} | {Global.displayGameCharacters(gameName, 25)} | {Global.displayGameCharacters(gamePrice, 7)} | {Global.displayGameCharacters(gameCategory, 20)} | {gameRelease} | {gameStock} ")

        gameDataTemp.remove(gameId)
        listNumber += 1


def ListGameHargaDescending(gameData):
    gameDataTemp = ["" for i in range(Global.length(gameData))]
    for i in range(Global.length(gameData)):
        gameDataTemp[i] = gameData[Global.convertGameId(i + 1)]["id"]

    listNumber = 0
    while Global.length(gameDataTemp) > 0:
        highestPriceGame = updateTempGame(gameDataTemp[0], gameData)
        for i in range(Global.length(gameDataTemp) - 1):
            if (int(highestPriceGame["harga"]) < int(gameData[gameDataTemp[i + 1]]["harga"])):
                highestPriceGame = updateTempGame(
                    gameDataTemp[i + 1], gameData)

        gameId = highestPriceGame["id"]
        gameName = highestPriceGame["nama"]
        gamePrice = highestPriceGame["harga"]
        gameCategory = highestPriceGame["kategori"]
        gameRelease = highestPriceGame["tahun_rilis"]
        gameStock = highestPriceGame["stok"]

        print(
            f"{listNumber + 1}. {gameId} | {Global.displayGameCharacters(gameName, 25)} | {Global.displayGameCharacters(gamePrice, 7)} | {Global.displayGameCharacters(gameCategory, 20)} | {gameRelease} | {gameStock} ")

        gameDataTemp.remove(gameId)
        listNumber += 1


def ListGameTahunAscending(gameData):
    gameDataTemp = ["" for i in range(Global.length(gameData))]
    for i in range(Global.length(gameData)):
        gameDataTemp[i] = gameData[Global.convertGameId(i + 1)]["id"]

    listNumber = 0
    while Global.length(gameDataTemp) > 0:
        lowestReleaseGame = updateTempGame(gameDataTemp[0], gameData)
        for i in range(Global.length(gameDataTemp) - 1):
            if (int(lowestReleaseGame["tahun_rilis"]) > int(gameData[gameDataTemp[i + 1]]["tahun_rilis"])):
                lowestReleaseGame = updateTempGame(
                    gameDataTemp[i + 1], gameData)

        gameId = lowestReleaseGame["id"]
        gameName = lowestReleaseGame["nama"]
        gamePrice = lowestReleaseGame["harga"]
        gameCategory = lowestReleaseGame["kategori"]
        gameRelease = lowestReleaseGame["tahun_rilis"]
        gameStock = lowestReleaseGame["stok"]

        print(
            f"{listNumber + 1}. {gameId} | {Global.displayGameCharacters(gameName, 25)} | {Global.displayGameCharacters(gamePrice, 7)} | {Global.displayGameCharacters(gameCategory, 20)} | {gameRelease} | {gameStock} ")

        gameDataTemp.remove(gameId)
        listNumber += 1


def ListGameTahunDescending(gameData):
    gameDataTemp = ["" for i in range(Global.length(gameData))]
    for i in range(Global.length(gameData)):
        gameDataTemp[i] = gameData[Global.convertGameId(i + 1)]["id"]

    listNumber = 0
    while Global.length(gameDataTemp) > 0:
        highestReleaseGame = updateTempGame(gameDataTemp[0], gameData)
        for i in range(Global.length(gameDataTemp) - 1):
            if (int(highestReleaseGame["tahun_rilis"]) < int(gameData[gameDataTemp[i + 1]]["tahun_rilis"])):
                highestReleaseGame = updateTempGame(
                    gameDataTemp[i + 1], gameData)

        gameId = highestReleaseGame["id"]
        gameName = highestReleaseGame["nama"]
        gamePrice = highestReleaseGame["harga"]
        gameCategory = highestReleaseGame["kategori"]
        gameRelease = highestReleaseGame["tahun_rilis"]
        gameStock = highestReleaseGame["stok"]

        print(
            f"{listNumber + 1}. {gameId} | {Global.displayGameCharacters(gameName, 25)} | {Global.displayGameCharacters(gamePrice, 7)} | {Global.displayGameCharacters(gameCategory, 20)} | {gameRelease} | {gameStock} ")

        gameDataTemp.remove(gameId)
        listNumber += 1


def updateTempGame(gameId, gameData):
    return {
        "id": gameData[gameId]["id"],
        "nama": gameData[gameId]["nama"],
        "kategori": gameData[gameId]["kategori"],
        "tahun_rilis": gameData[gameId]["tahun_rilis"],
        "harga": gameData[gameId]["harga"],
        "stok": gameData[gameId]["stok"]
    }

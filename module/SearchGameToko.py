# SEARCH GAME TOKO MODULE

import module.globalModule as Global


def SearchGameToko(gameData):
    idInput = str(input("Masukkan ID Game: "))
    nameInput = str(input("Masukkan Nama Game: "))
    priceInput = str(input("Masukkan Harga Game: "))
    categoryInput = str(input("Masukkan Kategori Game: "))
    releaseInput = str(input("Masukkan Tahun Rilis Game: "))

    matchList = ["" for i in range(len(gameData))]
    for i in range(len(gameData)):
        matchList[i] = gameData[Global.convertGameId(i + 1)]["id"]

    matchList = filterId(gameData, matchList, idInput)
    matchList = filterName(gameData, matchList, nameInput)
    matchList = filterPrice(gameData, matchList, priceInput)
    matchList = filterCategory(gameData, matchList, categoryInput)
    matchList = filterRelease(gameData, matchList, releaseInput)

    print("Daftar game pada toko yang memenuhi kriteria:")
    for i in range(len(matchList)):
        print(f'{i + 1}. {matchList[i]} | {Global.displayGameCharacters(gameData[matchList[i]]["nama"], 25)} | {Global.displayGameCharacters(gameData[matchList[i]]["harga"], 7)} | {Global.displayGameCharacters(gameData[matchList[i]]["kategori"], 20)} | {gameData[matchList[i]]["tahun_rilis"]} | {gameData[matchList[i]]["stok"]}')


def filterId(gameData, matchList, idInput):
    if (len(idInput) == 0):
        return matchList
    else:
        return [gameData[idInput]["id"]]


def filterName(gameData, matchList, nameInput):
    if (len(nameInput) == 0):
        return matchList
    else:
        for i in range(len(matchList)):
            if (nameInput not in gameData[matchList[i]]["nama"]):
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
    if (len(priceInput) == 0):
        return matchList
    else:
        for i in range(len(matchList)):
            if (priceInput != gameData[matchList[i]]["harga"]):
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
    if (len(categoryInput) == 0):
        return matchList
    else:
        for i in range(len(matchList)):
            if (categoryInput not in gameData[matchList[i]]["kategori"]):
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
    if (len(releaseInput) == 0):
        return matchList
    else:
        for i in range(len(matchList)):
            if (releaseInput != gameData[matchList[i]]["tahun_rilis"]):
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

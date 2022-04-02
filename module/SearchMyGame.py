# SEARCH MY GAME MODULE

import module.globalModule as Global


def SearchMyGame(currentState, kepemilikanData, gameData):
    gameIdInput = str(input("Masukkan ID Game: "))
    gameReleaseInput = str(input("Masukkan Tahun Rilis Game: "))

    matchList = ["" for i in range(len(kepemilikanData))]
    matchListIndex = 0
    for i in range(len(kepemilikanData)):
        if (int(kepemilikanData[str(i + 1)]["user_id"]) == int(currentState["id"])):
            matchList[matchListIndex] = kepemilikanData[str(i + 1)]["game_id"]
            matchListIndex += 1

    matchList = filterId(gameIdInput, matchList)
    matchList = filterRelease(gameReleaseInput, gameData, matchList)
    print(matchList)  # aw

    i = 0
    while "" in matchList:
        if (matchList[i] == ""):
            matchList.pop(i)
        else:
            i += 1

    print("Daftar game pada inventory yang memenuhi kriteria:")
    if (len(matchList) > 0):
        for i in range(len(matchList)):
            print(f'{i + 1}. {matchList[i]} | {Global.displayGameCharacters(gameData[matchList[i]]["nama"], 25)} | {Global.displayGameCharacters(gameData[matchList[i]]["harga"], 7)} | {Global.displayGameCharacters(gameData[matchList[i]]["kategori"], 20)} | {gameData[matchList[i]]["tahun_rilis"]}')


def filterId(gameIdInput, matchList):
    if (len(gameIdInput) != 0):
        for i in range(len(matchList)):
            if (matchList[i] != gameIdInput):
                matchList[i] = "x"

    i = 0
    while "x" in matchList:
        if (matchList[i] == "x"):
            matchList.pop(i)
        else:
            i += 1

    return matchList


def filterRelease(gameReleaseInput, gameData, matchList):
    if (len(gameReleaseInput) != 0):
        for i in range(len(matchList)):
            if (gameData[matchList[i]]["tahun_rilis"] != gameReleaseInput):
                matchList[i] = "x"

    i = 0
    while "x" in matchList:
        if (matchList[i] == "x"):
            matchList.pop(i)
        else:
            i += 1

    return matchList

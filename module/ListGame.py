# LIST GAME MODULE

import module.globalModule as Global


def ListGame(currentState, kepemilikanData, gameData):
    currentId = currentState["id"]

    isUserHasGame = False
    for i in range(len(kepemilikanData)):
        if (kepemilikanData[str(i + 1)]["user_id"] == currentId):
            isUserHasGame = True

    if (isUserHasGame):
        print("Daftar game:")
        displayNumber = 1
        for i in range(len(kepemilikanData)):
            if (kepemilikanData[str(i + 1)]["user_id"] == currentId):
                gameId = kepemilikanData[str(i + 1)]["game_id"]
                gameName = gameData[gameId]["nama"]
                gameCategory = gameData[gameId]["kategori"]
                gameRelease = gameData[gameId]["tahun_rilis"]
                gamePrice = gameData[gameId]["harga"]
                print(
                    f"{displayNumber}. {gameId} | {Global.displayGameCharacters(gameName, 35)} | {Global.displayGameCharacters(gameCategory, 20)} | {gameRelease} | {gamePrice}")
                displayNumber += 1
    else:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")

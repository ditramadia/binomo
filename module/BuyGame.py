# BUY GAME MODULE

import datetime
import module.globalModule as Global


def BuyGame(currentState, userData, gameData, kepemilikanData, riwayatData):
    idGameInput = str(input("Masukkan ID Game: "))
    if (idGameInput in gameData):
        isGameIdValid = True
    else:
        isGameIdValid = False
    while not isGameIdValid:
        print("Tidak ada game dengan ID tersebut!")
        idGameInput = str(input("Masukkan ulang ID Game: "))
        if (idGameInput in gameData):
            isGameIdValid = True

    if (not isStockAvailable(gameData, idGameInput)):
        print("Stok Game tersebut sedang habis!")
    elif (not isSaldoAvailable(gameData, idGameInput, currentState)):
        print("Saldo Anda tidak cukup untuk membeli Game tersebut!")
        print(currentState["saldo"])
        print(gameData[idGameInput]["harga"])
    elif (isGamePurchased(currentState, kepemilikanData, idGameInput)):
        print("Anda sudah memiliki Game tersebut!")
    else:
        userId = str(currentState["id"])
        userSaldo = int(userData[userId]["saldo"])
        userSaldo -= int(gameData[idGameInput]["harga"])
        userData[userId]["saldo"] = str(userSaldo)
        gameStock = int(gameData[idGameInput]["stok"])
        gameStock -= 1
        gameData[idGameInput]["stok"] = str(gameStock)

        newKepemilikanId = str(Global.length(kepemilikanData) + 1)
        kepemilikanData[newKepemilikanId] = {
            "id": newKepemilikanId,
            "game_id": idGameInput,
            "user_id": currentState["id"],
        }

        now = datetime.datetime.now()
        buyYear = now.year
        newRiwayatId = str(Global.length(riwayatData) + 1)
        gameName = gameData[idGameInput]["nama"]
        riwayatData[newRiwayatId] = {
            "id": newRiwayatId,
            "game_id": idGameInput,
            "nama": gameName,
            "harga": gameData[idGameInput]["harga"],
            "user_id": currentState["id"],
            "tahun_beli": str(buyYear),
        }

        print(f"Game {gameName} berhasil dibeli!")


def isStockAvailable(gameData, idGameInput):
    if (gameData[idGameInput]["stok"] == 0):
        return False
    else:
        return True


def isSaldoAvailable(gameData, idGameInput, currentState):
    if (int(currentState["saldo"]) >= int(gameData[idGameInput]["harga"])):
        return True
    else:
        return False


def isGamePurchased(currentState, kepemilikanData, idGameInput):
    valid = False
    for i in range(Global.length(kepemilikanData)):
        if (kepemilikanData[str(i + 1)]["user_id"] == currentState["id"]):
            if (kepemilikanData[str(i + 1)]["game_id"] == idGameInput):
                valid = True
    return valid

# RIWAYAT MODULE

import module.globalModule as Global


def Riwayat(riwayatData, currentState):
    currentId = currentState["id"]

    isUserHasRiwayat = False
    for i in range(Global.length(riwayatData)):
        if (riwayatData[str(i + 1)]["user_id"] == currentId):
            isUserHasRiwayat = True

    if (isUserHasRiwayat):
        print("Daftar game:")
        displayNumber = 1
        for i in range(Global.length(riwayatData)):
            if (riwayatData[str(i + 1)]["user_id"] == currentId):
                gameName = riwayatData[str(i + 1)]["nama"]
                gamePrice = riwayatData[str(i + 1)]["harga"]
                purchaseYear = riwayatData[str(i + 1)]["tahun_beli"]
                print(
                    f"{displayNumber}. {Global.displayGameCharacters(gameName, 35)} | {Global.displayGameCharacters(gamePrice, 7)} | {Global.displayGameCharacters(purchaseYear, 4)}")
                displayNumber += 1
    else:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")

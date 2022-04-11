# UBAH STOK MODULE

import module.globalModule as Global


def ubahStok(gameData):
    gameId = str(input("Masukkan ID Game: "))
    if (GameIdExist(gameData, gameId)):
        isIdValid = True
    else:
        isIdValid = False
    while not isIdValid:
        print('Tidak ada game dengan ID tersebut.')
        gameId = str(input("Masukkan ulang ID Game: "))
        if (GameIdExist(gameData, gameId)):
            isIdValid = True

    newGameStockInput = int(input("Masukkan jumlah: "))
    oldGameStock = int(
        gameData[int(Global.convertGameIdReverse(gameId))][5])
    newGameStock = oldGameStock + newGameStockInput
    gameName = gameData[int(Global.convertGameIdReverse(gameId))][1]
    if (newGameStockInput >= 0):
        status = "ditambahkan"
    elif (newGameStockInput < 0):
        status = "dikurangi"
    if (newGameStock < 0):
        print(
            f"Stok game {gameName} gagal {status} karena stok kurang. Stok sekarang: {str(oldGameStock)}")
    else:
        gameData[int(Global.convertGameIdReverse(gameId))
                 ][5] = str(newGameStock)
        print(
            f"Stok game {gameName} berhasil {status}. Stok sekarang: {str(newGameStock)}")


def GameIdExist(gameData, gameId):
    valid = False
    for i in range(Global.length(gameData) - 1):
        if (gameData[i + 1][0] == gameId):
            valid = True
    return valid

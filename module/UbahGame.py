# UBAH GAME MODULE

import module.globalModule as Global


def UbahGame(gameData):
    gameId = str(input("Masukkan id game yang akan diubah: "))
    if (GameIdExist(gameData, gameId)):
        idValid = True
    else:
        idValid = False
    while not idValid:
        print('Tidak ada game dengan ID tersebut.')
        gameId = str(input('Masukkan ulang id game yang akan diubah: '))
        if (GameIdExist(gameData, gameId)):
            idValid = True

    newGameName = str(input("Masukkan nama game: "))
    newGameCategory = str(input("Masukkan kategori: "))
    newGameRelease = str(input("Masukkan tahun rilis: "))
    newGamePrice = str(input("Masukkan harga: "))

    while (Global.length(newGameName) == 0 and Global.length(newGameCategory) == 0 and Global.length(newGameRelease) == 0 and Global.length(newGamePrice) == 0):
        print("Masukkan setidaknya salah satu data game yang akan diubah")
        newGameName = str(input("Masukkan nama game: "))
        newGameCategory = str(input("Masukkan kategori: "))
        newGameRelease = str(input("Masukkan tahun rilis: "))
        newGamePrice = str(input("Masukkan harga: "))

    if (Global.length(newGameName) != 0):
        gameData[int(Global.convertGameIdReverse(gameId))][1] = newGameName
    if (Global.length(newGameCategory) != 0):
        gameData[int(Global.convertGameIdReverse(gameId))][2] = newGameCategory
    if (Global.length(newGameRelease) != 0):
        gameData[int(Global.convertGameIdReverse(gameId))][3] = newGameRelease
    if (Global.length(newGamePrice) != 0):
        gameData[int(Global.convertGameIdReverse(gameId))][4] = newGamePrice

    print("Selamat! Game berhasil diubah")


def GameIdExist(gameData, gameId):
    valid = False
    for i in range(Global.length(gameData) - 1):
        if (gameData[i + 1][0] == gameId):
            valid = True
    return valid

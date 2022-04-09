# UBAH GAME MODULE

import module.globalModule as Global


def UbahGame(gameData):
    gameId = str(input("Masukkan id game yang akan diubah: "))
    if (gameId in gameData):
        idValid = True
    else:
        idValid = False
    while not idValid:
        print('Tidak ada game dengan ID tersebut.')
        gameId = str(input('Masukkan ulang id game yang akan diubah: '))
        if (gameId in gameData):
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
        gameData[gameId]["nama"] = newGameName
    if (Global.length(newGameCategory) != 0):
        gameData[gameId]["kategori"] = newGameCategory
    if (Global.length(newGameRelease) != 0):
        gameData[gameId]["tahun_rilis"] = newGameRelease
    if (Global.length(newGamePrice) != 0):
        gameData[gameId]["harga"] = newGamePrice

    print("Selamat! Game berhasil diubah")

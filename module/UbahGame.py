# UBAH GAME MODULE

def UbahGame(gameData):
    gameId = str(input("Masukkan id game yang akan diubah: "))
    if (gameId in gameData):
        idValid = True
    else:
        idValid = False
    while not idValid:
        print('Game tidak ditemukan')
        gameId = str(input('Masukkan ulang id game yang akan diubah: '))
        if (gameId in gameData):
            idValid = True

    newGameName = str(input("Masukkan nama game: "))
    newGameCategory = str(input("Masukkan kategori: "))
    newGameRelease = str(input("Masukkan tahun rilis: "))
    newGamePrice = str(input("Masukkan harga: "))

    while (len(newGameName) == 0 and len(newGameCategory) == 0 and len(newGameRelease) == 0 and len(newGamePrice) == 0):
        print("Masukkan setidaknya salah satu data game yang akan diubah")
        newGameName = str(input("Masukkan nama game: "))
        newGameCategory = str(input("Masukkan kategori: "))
        newGameRelease = str(input("Masukkan tahun rilis: "))
        newGamePrice = str(input("Masukkan harga: "))

    if (len(newGameName) != 0):
        gameData[gameId]["nama"] = newGameName
    if (len(newGameCategory) != 0):
        gameData[gameId]["kategori"] = newGameCategory
    if (len(newGameRelease) != 0):
        gameData[gameId]["tahun_rilis"] = newGameRelease
    if (len(newGamePrice) != 0):
        gameData[gameId]["harga"] = newGamePrice

    print("Selamat! Game berhasil diubah")

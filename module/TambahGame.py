# TAMBAH GAME MODULE

import module.globalModule as Global


def TambahGame(gameData):
    newGameName = str(input("Masukkan nama game: "))
    newGameCategory = str(input("Masukkan kategori: "))
    newGameRelease = str(input("Masukkan tahun rilis: "))
    newGamePrice = str(input("Masukkan harga: "))
    newGameStock = str(input("Masukkan stok awal: "))

    while not isInputValid(newGameName) or not isInputValid(newGameCategory) or not isInputValid(newGameRelease) or not isInputValid(newGamePrice) or not isInputValid(newGameStock):
        print("Mohon measukkan semua informasi mengenai game agar dapat disimpan di BNMO")
        newGameName = str(input("Masukkan nama game: "))
        newGameCategory = str(input("Masukkan kategori: "))
        newGameRelease = str(input("Masukkan tahun rilis: "))
        newGamePrice = str(input("Masukkan harga: "))
        newGameStock = str(input("Masukkan stok awal: "))

    newGameData = [Global.convertGameId(Global.length(
        gameData)), newGameName, newGameCategory, newGameRelease, newGamePrice, newGameStock]
    gameData = Global.Append(gameData, newGameData)

    # gameData[Global.convertGameId(Global.length(gameData) + 1)] = {
    #     "id": Global.convertGameId(Global.length(gameData) + 1),
    #     "nama": newGameName,
    #     "kategori": newGameCategory,
    #     "tahun_rilis": newGameRelease,
    #     "harga": newGamePrice,
    #     "stok": newGameStock,
    # }
    print(f'Selamat! Berhasil menambahkan game {newGameName}.')

    return gameData


def isInputValid(parameter):
    if (Global.length(parameter) == 0):
        return False
    else:
        return True

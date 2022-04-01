# UBAH STOK MODULE

def ubahStok(gameData):
    gameId = str(input("Masukkan ID Game: "))
    if (gameId in gameData):
        isIdValid = True
    else:
        isIdValid = False
    while not isIdValid:
        print('Tidak ada game dengan ID tersebut.')
        gameId = str(input("Masukkan ulang ID Game: "))
        if (gameId in gameData):
            isIdValid = True

    newGameStockInput = int(input("Masukkan jumlah: "))
    oldGameStock = int(gameData[gameId]["stok"])
    newGameStock = oldGameStock + newGameStockInput
    gameName = gameData[gameId]["nama"]
    if (newGameStockInput >= 0):
        status = "ditambahkan"
    elif (newGameStockInput < 0):
        status = "dikurangi"
    if (newGameStock < 0):
        print(
            f"Stok game {gameName} gagal {status} karena stok kurang. Stok sekarang: {str(oldGameStock)}")
    else:
        gameData[gameId]["stok"] = str(newGameStock)
        print(
            f"Stok game {gameName} berhasil {status}. Stok sekarang: {str(newGameStock)}")

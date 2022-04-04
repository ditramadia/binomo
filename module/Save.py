# SAVE MODULE

import os
import time
import module.globalModule as Global


def Save(userData, gameData, kepemilikanData, riwayatData):
    saveFolder = input('Masukkan nama folder penyimpanan: ')
    # Ubah di sini
    saveDirectory = f"E:/Kuliah/ITB/IF1210/Tubes/saves/{saveFolder}"

    while os.path.exists(saveDirectory):
        print(f'Folder dengan nama {saveFolder} sudah ada.')
        saveFolder = input('Masukkan ulang nama folder penyimpanan: ')
        # Ubah di sini
        saveDirectory = f"E:/Kuliah/ITB/IF1210/Tubes/saves/{saveFolder}"

    print('Saving...')
    os.makedirs(saveDirectory)

    time.sleep(5)

    SaveUserData(userData, saveFolder)
    SaveGameData(gameData, saveFolder)
    SaveKepemilikanData(kepemilikanData, saveFolder)
    SaveRiwayatData(riwayatData, saveFolder)
    print(f'Data telah disimpan pada folder saves\{saveFolder}!')


def SaveUserData(userData, saveFolder):
    file = open(f".\\saves\\{saveFolder}\\user.csv", 'x')
    file.write("id;username;nama;password;role;saldo\n")
    file.close()

    file = open(f".\\saves\\{saveFolder}\\user.csv", 'a')
    for i in range(len(userData)):
        updateUserId = userData[str(i + 1)]["id"]
        updateUserUsername = userData[str(i + 1)]["username"]
        updateUserName = userData[str(i + 1)]["nama"]
        updateUserPassword = userData[str(i + 1)]["password"]
        updateUserRole = userData[str(i + 1)]["role"]
        updateUserSaldo = userData[str(i + 1)]["saldo"]
        file.write(
            f"{updateUserId};{updateUserUsername};{updateUserName};{updateUserPassword};{updateUserRole};{updateUserSaldo}\n")
    file.close()


def SaveGameData(gameData, saveFolder):
    file = open(f".\\saves\\{saveFolder}\\game.csv", 'x')
    file.write("id;nama;kategori;tahun_rilis;harga;stok\n")
    file.close()

    file = open(f".\\saves\\{saveFolder}\\game.csv", 'a')
    for i in range(len(gameData)):
        updateGameId = gameData[Global.convertGameId(i + 1)]["id"]
        updateGameName = gameData[Global.convertGameId(
            i + 1)]["nama"]
        updateGameCategory = gameData[Global.convertGameId(
            i + 1)]["kategori"]
        updateGameRelease = gameData[Global.convertGameId(
            i + 1)]["tahun_rilis"]
        updateGamePrice = gameData[Global.convertGameId(
            i + 1)]["harga"]
        updateGameStock = gameData[Global.convertGameId(
            i + 1)]["stok"]
        file.write(
            f"{updateGameId};{updateGameName};{updateGameCategory};{updateGameRelease};{updateGamePrice};{updateGameStock}\n")
    file.close()


def SaveKepemilikanData(kepemilikanData, saveFolder):
    file = open(f".\\saves\\{saveFolder}\\kepemilikan.csv", 'x')
    file.write("id;game_id;user_id\n")
    file.close()

    file = open(f".\\saves\\{saveFolder}\\kepemilikan.csv", 'a')
    for i in range(len(kepemilikanData)):
        updateKepemilikanId = kepemilikanData[str(i + 1)]["id"]
        updateGameId = kepemilikanData[str(i + 1)]["game_id"]
        updateUserId = kepemilikanData[str(i + 1)]["user_id"]
        file.write(
            f"{updateKepemilikanId};{updateGameId};{updateUserId}\n")
    file.close()


def SaveRiwayatData(riwayatData, saveFolder):
    file = open(f".\\saves\\{saveFolder}\\riwayat.csv", 'x')
    file.write("id;game_id;nama;harga;user_id;tahun_beli\n")
    file.close()

    file = open(f".\\saves\\{saveFolder}\\riwayat.csv", 'a')
    for i in range(len(riwayatData)):
        updateRiwayatId = riwayatData[str(i + 1)]["id"]
        updateGameId = riwayatData[str(i + 1)]["game_id"]
        updateGameName = riwayatData[str(i + 1)]["nama"]
        updateGamePrice = riwayatData[str(i + 1)]["harga"]
        updateUserId = riwayatData[str(i + 1)]["user_id"]
        updateYear = riwayatData[str(i + 1)]["tahun_beli"]
        file.write(
            f"{updateRiwayatId};{updateGameId};{updateGameName};{updateGamePrice};{updateUserId};{updateYear}\n")
    file.close()

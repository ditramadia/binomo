# SAVE MODULE

import os
import time
import module.globalModule as Global


def Save(userData, gameData):
    saveFolder = input('Masukkan nama folder penyimpanan: ')
    saveDirectory = f"E:/Kuliah/ITB/IF1210/Tubes/saves/{saveFolder}"

    while os.path.exists(saveDirectory):
        print(f'Folder dengan nama {saveFolder} sudah ada.')
        saveFolder = input('Masukkan ulang nama folder penyimpanan: ')
        saveDirectory = f"E:/Kuliah/ITB/IF1210/Tubes/saves/{saveFolder}"

    print('Saving...')
    os.makedirs(saveDirectory)

    time.sleep(5)

    SaveUserData(userData, saveFolder)
    SaveGameData(gameData, saveFolder)
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

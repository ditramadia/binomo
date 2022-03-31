# SAVE MODULE

import os
import time


def Save(userData):
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
    print(f'Data telah disimpan pada folder saves/{saveFolder}!')


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

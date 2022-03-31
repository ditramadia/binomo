# Main Program BINOMO

import module.Load as Load
import module.Help as Help
import module.Login as Login
import module.Register as Register
import module.Topup as Topup
import module.ListGameToko as ListGameToko
import module.Save as Save
import module.Exit as Exit


# LOAD DATA
# Load.LoadFolder()
print('Loading ...')
userData = Load.LoadUserData()
gameData = Load.LoadGameData()
kepemilikanData = Load.LoadKepemilikanData()
riwayatData = Load.LoadRiwayatData()
print('Selamat datang di antarmuka "Binomo"')
print("Masukkan perintah atau ketik 'help' untuk melihat daftar perintah")

# INITIAL STATE
currentState = {
    "id": None,
    "username": None,
    "nama": None,
    "password": None,
    "role": "admin",
    "saldo": None
}
programStatus = "saved"

while True:
    command = str(input(">>> "))
    if (command == "help"):
        Help.callHelp(currentState)
    elif (command == "login"):
        Login.Login(currentState, userData)
    elif (command == "register"):
        if (currentState["role"] == "admin"):
            Register.Register(currentState, userData)
            programStatus = "unsaved"
        else:
            print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
    elif (command == "topup"):
        if (currentState["role"] == "admin"):
            Topup.Topup(userData)
        else:
            print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
    elif (command == "list_game_toko"):
        if (currentState["role"] != "guest"):
            ListGameToko.ListGameToko(gameData)
        else:
            print(
                "Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”.")
    elif (command == "save"):
        Save.Save(userData)
    elif (command == "exit"):
        if (programStatus == "unsaved"):
            if (Exit.isExitConfirmed()):
                Save.Save(userData)
                Exit.Exit()
            else:
                Exit.Exit()
        else:
            Exit.Exit()
    else:
        print("Maaf, perintah tidak ditemukan. Ketik 'help' untuk melihat daftar perintah")

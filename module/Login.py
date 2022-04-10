# LOGIN MODULE

import module.globalModule as Global
import module.Cipher as Cipher


def Login(currentState, userData):
    usernameInput = input('Masukkan username: ')
    passowrdInput = input('Masukkan password: ')
    if isLoginValid(userData, usernameInput, passowrdInput):
        finalId = getLoginId(userData, usernameInput, passowrdInput)
        currentState["id"] = finalId
        currentState["username"] = userData[str(finalId)]["username"]
        currentState["nama"] = userData[str(finalId)]["nama"]
        currentState["password"] = Cipher.Cipher(
            userData[str(finalId)]["password"])
        currentState["role"] = userData[str(finalId)]["role"]
        currentState["saldo"] = userData[str(finalId)]["saldo"]
        print(f'Halo {currentState["nama"]}! Selamat datang di "Binomo"')
    else:
        print("Password atau username salah atau tidak ditemukan.")


def isLoginValid(userData, usernameInput, passwordInput):
    for i in range(Global.length(userData)):
        if (userData[str(i + 1)]["username"] == usernameInput):
            if (userData[str(i + 1)]["password"] == Cipher.Cipher(passwordInput)):
                return True
            else:
                False
        else:
            False


def getLoginId(userData, usernameInput, passwordInput):
    for i in range(Global.length(userData)):
        if (userData[str(i + 1)]["username"] == usernameInput):
            if (userData[str(i + 1)]["password"] == Cipher.Cipher(passwordInput)):
                return (i + 1)
            else:
                None
        else:
            None

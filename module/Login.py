# LOGIN MODULE

import module.globalModule as Global
import module.Cipher as Cipher


def Login(currentState, userData):
    usernameInput = input('Masukkan username: ')
    passowrdInput = input('Masukkan password: ')
    if isLoginValid(userData, usernameInput, passowrdInput):
        finalId = getLoginId(userData, usernameInput, passowrdInput)
        currentState[1][0] = finalId
        currentState[1][1] = userData[finalId][1]
        currentState[1][2] = userData[finalId][2]
        currentState[1][3] = Cipher.Cipher(
            userData[finalId][3])
        currentState[1][4] = userData[finalId][4]
        currentState[1][5] = userData[finalId][5]
        print(f'Halo {currentState[1][2]}! Selamat datang di "Binomo"')
    else:
        print("Password atau username salah atau tidak ditemukan.")


def isLoginValid(userData, usernameInput, passwordInput):
    for i in range(Global.length(userData) - 1):
        if (userData[i + 1][1] == usernameInput):
            if (userData[i + 1][3] == Cipher.Cipher(passwordInput)):
                return True
            else:
                False
        else:
            False


def getLoginId(userData, usernameInput, passwordInput):
    for i in range(Global.length(userData) - 1):
        if (userData[i + 1][1] == usernameInput):
            if (userData[i + 1][3] == Cipher.Cipher(passwordInput)):
                return (i + 1)
            else:
                None
        else:
            None

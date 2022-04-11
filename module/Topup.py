# TOPUP MODULE

import module.globalModule as Global


def Topup(userData):
    usernameInput = str(input('Masukkan username: '))
    saldoInput = int(input("Masukkan saldo: "))
    while not isUsernameExist(userData, usernameInput) or not isSaldoValid(saldoInput):
        if (not isUsernameExist(userData, usernameInput)):
            print(f"Username “{usernameInput}” tidak ditemukan.")
            usernameInput = str(input('Masukkan ulang username: '))
        if (not isSaldoValid(saldoInput)):
            print('Masukan saldo tidak valid.')

    id = getTopupId(userData, usernameInput)
    userData[id][5] = str(
        int(userData[id][5]) + saldoInput)

    return userData


def isUsernameExist(userData, usernameInput):
    usernameExist = False
    for i in range(Global.length(userData) - 1):
        if (userData[i + 1][1] == usernameInput):
            usernameExist = True
            break
    return usernameExist


def getTopupId(userData, usernameInput):
    for i in range(Global.length(userData) - 1):
        if (userData[i + 1][1] == usernameInput):
            id = i + 1
        else:
            pass
    return id


def isSaldoValid(saldoInput):
    if (saldoInput > 0):
        return True
    else:
        return False

# TOPUP MODULE

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
    userData[str(id)]["saldo"] = str(
        int(userData[str(id)]["saldo"]) + saldoInput)


def isUsernameExist(userData, usernameInput):
    usernameExist = False
    for i in range(len(userData)):
        if (userData[str(i + 1)]["username"] == usernameInput):
            usernameExist = True
            break
    return usernameExist


def getTopupId(userData, usernameInput):
    for i in range(len(userData)):
        if (userData[str(i + 1)]["username"] == usernameInput):
            id = i + 1
        else:
            pass
    return id


def isSaldoValid(saldoInput):
    if (saldoInput > 0):
        return True
    else:
        return False

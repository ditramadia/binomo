# REGISTER MODULE

def Register(currentState, userData):
    namaInput = str(input("Masukkan nama: "))
    usernameInput = str(input("Masukkan username: "))
    passwordInput = str(input("Masukkan password: "))
    while not isUsernameCharactersValid(usernameInput) or not isUsernameAvailable(userData, usernameInput):
        while not isUsernameCharactersValid(usernameInput):
            print(
                'username hanya boleh mengandung alfabet A-Z atau a-z, uderscore "_", strip "-", dan angka 0-9.')
            usernameInput = str(input("Masukkan username: "))
        while not isUsernameAvailable(userData, usernameInput):
            print(
                f'Username {usernameInput} sudah terpakai, silakan menggunakan username lain.')
            usernameInput = str(input("Masukkan username: "))
    userData[str(len(userData) + 1)] = {
        "id": str(len(userData) + 1),
        "username": usernameInput,
        "nama": namaInput,
        "password": passwordInput,
        "role": "user",
        "saldo": str(0),
    }
    print(
        f'Username {usernameInput} telah berhasil register ke dalam "Binomo".')


def isUsernameCharactersValid(usernameInput):
    validCharacters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'x',
                       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                       '-', '_']
    nCharacterValid = 0
    for characterIndex in range(len(usernameInput)):
        for validCharacterIndex in range(len(validCharacters)):
            if (usernameInput[characterIndex] == validCharacters[validCharacterIndex]):
                nCharacterValid += 1
            else:
                pass

    if (nCharacterValid == len(usernameInput)):
        return True
    else:
        return False


def isUsernameAvailable(userData, usernameInput):
    identicalUsername = 0
    for userIndex in range(len(userData)):
        if (userData[str(userIndex + 1)]["username"] == usernameInput):
            identicalUsername += 1
        else:
            pass

    if (identicalUsername < 1):
        return True
    else:
        return False

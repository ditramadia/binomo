# CIPHER MODULE

import module.globalModule as Global


def Cipher(text):
    key = Global.length(text) // 2

    list = ["" for i in range(Global.length(text))]
    for i in range(Global.length(text)):
        list[i] = text[i]

    for i in range(Global.length(list)):
        list[i] = chr(ord(list[i]) + key)

    cipheredText = ""
    for i in range(Global.length(list)):
        cipheredText += list[i]

    return cipheredText


def Decipher(text):
    key = Global.length(text) // 2

    list = ["" for i in range(Global.length(text))]
    for i in range(Global.length(text)):
        list[i] = text[i]

    for i in range(Global.length(list)):
        list[i] = chr(ord(list[i]) - key)

    decipheredText = ""
    for i in range(Global.length(list)):
        decipheredText += list[i]

    return decipheredText

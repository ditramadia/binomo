# EXIT MODULE

import sys


def Exit():
    sys.exit()


def isExitConfirmed():
    confirm = str(
        input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))
    while not isValidConfirmed(confirm):
        confirm = str(
            input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))
    if (confirm == "Y" or confirm == "y"):
        return True
    else:
        (confirm == "N" or confirm == 'y')
        return False


def isValidConfirmed(confirm):
    if (confirm == "Y" or confirm == "y" or confirm == "N" or confirm == "y"):
        return True
    else:
        return False

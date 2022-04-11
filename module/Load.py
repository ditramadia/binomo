# LOAD MODULE

from os import path
import argparse
import sys
import module.globalModule as Global


def LoadFolder():
    # Arguments
    parser = argparse.ArgumentParser(description='Load program data')
    parser.add_argument('folder', type=str,
                        help='Name of folder containing program data')
    args = parser.parse_args()

    # Check Folder
    if (path.isdir(args.folder)):
        global folderName
        folderName = args.folder
    else:
        print(f'Folder {args.folder} tidak ditemukan.')
        sys.exit()


def getFolderName():
    return folderName


def LoadUserData(folder):
    file = open(f".\\{folder}\\user.csv", 'r')
    dataFrame = []
    header = file.readline()
    header = Global.Replace(header, "\n", "")
    header = Global.seperate(header, ";")
    dataFrame = Global.Append(dataFrame, header)
    for line in file:
        linedata = Global.Replace(line, '\n', '')
        linedata = Global.seperate(linedata, ";")
        dataFrame = Global.Append(dataFrame, linedata)
    file.close()

    return dataFrame


def LoadGameData(folder):
    file = open(f".\\{folder}\\game.csv", 'r')
    dataFrame = []
    header = file.readline()
    header = Global.Replace(header, "\n", "")
    header = Global.seperate(header, ";")
    dataFrame = Global.Append(dataFrame, header)
    for line in file:
        linedata = Global.Replace(line, '\n', '')
        linedata = Global.seperate(linedata, ";")
        dataFrame = Global.Append(dataFrame, linedata)
    file.close()

    return dataFrame


def LoadKepemilikanData(folder):
    file = open(f".\\{folder}\\kepemilikan.csv", 'r')
    dataFrame = {}
    header = file.readline()
    header = Global.Replace(header, "\n", "")
    header = Global.seperate(header, ";")
    for line in file:
        linedata = line.replace('\n', '')
        linedata = Global.seperate(linedata, ";")
        row = {}
        for x in range(Global.length(header)):
            if (x in range(Global.length(linedata))):
                row[header[x]] = linedata[x]
            else:
                row[header[x]] = "null"
        dataFrame[linedata[0]] = row
    file.close()
    return dataFrame


def LoadRiwayatData(folder):
    file = open(f".\\{folder}\\riwayat.csv", 'r')
    dataFrame = {}
    header = file.readline()
    header = Global.Replace(header, "\n", "")
    header = Global.seperate(header, ";")
    for line in file:
        linedata = line.replace('\n', '')
        linedata = Global.seperate(linedata, ";")
        row = {}
        for x in range(Global.length(header)):
            if (x in range(Global.length(linedata))):
                row[header[x]] = linedata[x]
            else:
                row[header[x]] = "null"
        dataFrame[linedata[0]] = row
    file.close()
    return dataFrame

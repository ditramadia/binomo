# LOAD MODULE

from os import path
import argparse
import sys


def LoadFolder():
    # Arguments
    parser = argparse.ArgumentParser(description='Load program data')
    parser.add_argument('folder', type=str,
                        help='Name of folder containing program data')
    args = parser.parse_args()

    # Check Folder
    if (path.isdir(args.folder)):
        pass
    else:
        print(f'Folder {args.folder} tidak ditemukan.')
        sys.exit()


def LoadUserData():
    file = open(f".\\data\\user.csv", 'r')
    dataFrame = {}
    header = file.readline().replace('\n', '').split(';')
    for line in file:
        linedata = line.replace('\n', '').split(';')
        row = {}
        for x in range(len(header)):
            if (x in range(len(linedata))):
                row[header[x]] = linedata[x]
            else:
                row[header[x]] = "null"
        dataFrame[linedata[0]] = row
    file.close()
    return dataFrame


def LoadGameData():
    file = open(".\\data\\game.csv", 'r')
    dataFrame = {}
    header = file.readline().replace('\n', '').split(';')
    for line in file:
        linedata = line.replace('\n', '').split(';')
        row = {}
        for x in range(len(header)):
            if (x in range(len(linedata))):
                row[header[x]] = linedata[x]
            else:
                row[header[x]] = "null"
        dataFrame[linedata[0]] = row
    file.close()
    return dataFrame


def LoadKepemilikanData():
    file = open(".\\data\\kepemilikan.csv", 'r')
    dataFrame = {}
    header = file.readline().replace('\n', '').split(';')
    for line in file:
        linedata = line.replace('\n', '').split(';')
        row = {}
        for x in range(len(header)):
            if (x in range(len(linedata))):
                row[header[x]] = linedata[x]
            else:
                row[header[x]] = "null"
        dataFrame[linedata[0]] = [row]
    file.close()
    return dataFrame


def LoadRiwayatData():
    file = open(".\\data\\riwayat.csv", 'r')
    dataFrame = {}
    header = file.readline().replace('\n', '').split(';')
    for line in file:
        linedata = line.replace('\n', '').split(';')
        row = {}
        for x in range(len(header)):
            if (x in range(len(linedata))):
                row[header[x]] = linedata[x]
            else:
                row[header[x]] = "null"
        dataFrame[linedata[0]] = [row]
    file.close()
    return dataFrame

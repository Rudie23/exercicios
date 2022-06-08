import os
from os import path
import shutil


def CopyFile():
    if path.exists("New.txt"):
        pathCurrent = path.realpath("New.txt")
        newPath = pathCurrent + ".bkp"
        shutil.copy(pathCurrent, newPath)

        shutil.copystat(pathCurrent, newPath)


CopyFile()


def renameFile():
    if path.exists("New.txt.bkp"):
        os.rename("New.txt.bkp", "ChangedFile.txt")
        

renameFile()

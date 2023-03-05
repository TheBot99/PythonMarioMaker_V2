import numpy
import ArrayReconstruct
import MakeArrayALevel
import LevelWriter
import os


LevelName = input("Level Name: ")
LevelDirectory = "Levels/" + LevelName
PickingFile = True

while PickingFile:
    if os.path.exists(LevelDirectory+".npy"):
        PickingFile = False
    else:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("Level Not Found")
        LevelName = input("Level Name: ")
        LevelDirectory = "Levels/" + LevelName


def ReadLevel():
    global LevelDirectory
    global FromFileLoadedLevelArray
    FromFileLoadedLevelArray = ArrayReconstruct.Reconstruct(LevelDirectory)

def SaveLevel():
    global LevelDirectory
    global FromFileLoadedLevelArray
    DeconstructedArray = LevelWriter.DeconstructArray(FromFileLoadedLevelArray)
    LevelWriter.WriteLevelToFile(LevelDirectory, DeconstructedArray)

def ReadPoint():
    global FromFileLoadedLevelArray
    X = int(input("X: "))
    Y = int(input("Y: "))
    print(FromFileLoadedLevelArray[Y-1][X-1])



Asking = True

while Asking:
    WhatDoYouWantToDo = input("What do you want to do? 1: Read Level, 2: Save Level, 3: Change Point, 4: Write Back Up, 5: Read a point, 6: Quit: ")

    if WhatDoYouWantToDo == "1":
        ReadLevel()


    elif WhatDoYouWantToDo == "2":
        SaveLevel()

    elif WhatDoYouWantToDo == "3":
        X = int(input("X: "))
        Y = int(input("Y: "))
        NewValue = input("New Value: ")
        LevelWriter.ChangePoints(X-1, Y-1, FromFileLoadedLevelArray, NewValue)

    elif WhatDoYouWantToDo == "4":
        LevelWriter.WriteBackUp()

    elif WhatDoYouWantToDo == "5":
        ReadPoint()
    
    elif WhatDoYouWantToDo == "6":
        Asking = False

    else:
        print("Invalid Input")






import numpy
import ArrayReconstruct
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
    global LevelArray
    LevelArray = ArrayReconstruct.Reconstruct(LevelDirectory)

def SaveLevel():
    global LevelDirectory
    global FromFileLoadedLevelArray
    DeconstructedArray = LevelWriter.DeconstructArray(LevelArray)
    LevelWriter.WriteLevelToFile(LevelDirectory, DeconstructedArray)

def ChangePoints():
    global LevelArray
    X = int(input("X: "))
    Y = int(input("Y: "))
    NewValue = input("New Value: ")
    LevelWriter.ChangePoints(X-1, Y-1, LevelArray, NewValue)

def ReadPoint():
    global LevelArray
    X = int(input("X: "))
    Y = int(input("Y: "))
    print(LevelArray[Y-1][X-1])

def MultiChangePoints():
    global LevelArray
    X = int(input("X: "))
    Y = int(input("Y: "))
    NewValue = input("New Value: ")
    X2 = int(input("X2: "))
    Y2 = int(input("Y2: "))
    for i in range(Y, Y2+1):
        for j in range(X, X2+1):
            LevelWriter.ChangePoints(j-1, i-1, LevelArray, NewValue)

def MultiReadPoints():
    global LevelArray
    X = int(input("X: "))
    Y = int(input("Y: "))
    X2 = int(input("X2: "))
    Y2 = int(input("Y2: "))
    for i in range(Y, Y2+1):
        for j in range(X, X2+1):
            print(LevelArray[i-1][j-1])

Asking = True

while Asking:
    WhatDoYouWantToDo = input("What do you want to do? 1: Read Level, 2: Save Level, 3: Change Points, 4: Write Back Up, 5: Read a point,  6: Multi Read Points, 7: Quit: ")

    if WhatDoYouWantToDo == "1":
        ReadLevel()


    elif WhatDoYouWantToDo == "2":
        SaveLevel()

    elif WhatDoYouWantToDo == "3":
        ChangePoints()

    elif WhatDoYouWantToDo == "4":
        LevelWriter.WriteBackUp()

    elif WhatDoYouWantToDo == "5":
        ReadPoint()

    elif WhatDoYouWantToDo == "6":
        MultiReadPoints()
    
    elif WhatDoYouWantToDo == "7":
        Asking = False

    else:
        print("Invalid Input")
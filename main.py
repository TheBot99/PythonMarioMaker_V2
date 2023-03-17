import numpy
import ArrayReconstruct
import LevelWriter
import os
import time
import pygame
import sys
import threading
import keyboard




PickingFileCMD = True

if PickingFileCMD:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    LevelName = input("Level Name: ")
    LevelDirectory = "Levels/" + LevelName

while PickingFileCMD:
    if os.path.exists(LevelDirectory+".npy"):
        PickingFileCMD = False
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
    global LevelBoundX
    global LevelBoundY

    LevelArray, LevelBoundX, LevelBoundY = ArrayReconstruct.Reconstruct(LevelDirectory)

def SaveLevel():
    global LevelDirectory
    DeconstructedArray = LevelWriter.DeconstructArray(LevelArray)
    LevelWriter.WriteLevelToFile(LevelDirectory, DeconstructedArray)

def ChangePoints():
    Multi = input("Do you want to change multiple points? Y/N: ")
    if Multi == "Y":
        MultiChangePoints()
    elif Multi == "N":
        SingleChangePoints()
    else:
        print("Invalid Input")
def SingleChangePoints():
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

def MultiReadPoints(X, Y, X2, Y2):
    BlockCoordinates = []
    global LevelArray
    for i in range(Y, Y2+1):
        for j in range(X, X2+1):
            BlockCoordinates.append(LevelArray[i-1][j-1])
    return BlockCoordinates
    


AskingWindowed = True
Asking = False

while Asking:
    WhatDoYouWantToDo = input("What do you want to do? 1: Read Level, 2: Save Level, 3: Change Points, 4: Write Back Up, 5: Read a point,  6: Multi Read Points, 7: Create New Level, 8: Quit: ")

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
        LevelName = input("Level Name: ")
        LevelDirectory = "Levels/" + LevelName
        LevelWriter.CreateLevel(LevelDirectory)
    
    elif WhatDoYouWantToDo == "8":
        Asking = False

    else:
        print("Invalid Input")


def QuitWithX():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global AskingWindowed
            AskingWindowed = False


FindX1 = 1
FindY1 = 1
FindX2 = 6
FindY2 = 4

def FindCoordinatesFromMovement(Movement):  
    global LevelBoundX
    global LevelBoundY
    global FindX1
    global FindY1
    global FindX2
    global FindY2


    if Movement == "w":
        if FindY1 != 1:
            FindY1 -= 1
            FindY2 -= 1
        else:
            print("You are at the top of the level")

    elif Movement == "a":
        if FindX1 != 1:
            FindX1 -= 1
            FindX2 -= 1
        else:
            print("You are at the left of the level")

    elif Movement == "s":
        if FindY2 != LevelBoundY:
            FindY1 += 1
            FindY2 += 1
        else:
            print("You are at the bottom of the level")

    elif Movement == "d":
        if FindX2 != LevelBoundX:
            FindX1 += 1
            FindX2 += 1
        else:
            print("You are at the right of the level")


    elif Movement == "StartingInput":
       pass

    else:
        print("Invalid Input")

    return FindX1, FindY1, FindX2, FindY2


ReadLevel()







def AskMovement(Movement):
    global BlocksInListForRenderer
    global Starting

    if Movement == "quit":
        sys.exit()
        
    X1, Y1, X2, Y2 = FindCoordinatesFromMovement(Movement)
    print(X1, Y1, X2, Y2)
    BlocksInListForRenderer = MultiReadPoints(X1, Y1, X2, Y2)
    print(BlocksInListForRenderer)

PointerX = 1
PointerY = 1

def Pointer(Movement):
    global PointerX
    global PointerY

    BoundX = 6
    BoundY = 4

    if Movement == "w":
        if PointerY != 1:
            PointerY -= 1
        else:
            AskMovement("w")

    elif Movement == "a":
        if PointerX != 1:
            PointerX -= 1
        else:
            AskMovement("a")

    elif Movement == "s":
        if PointerY != BoundY:
            PointerY += 1
        else:
            AskMovement("s")

    elif Movement == "d":
        if PointerX != BoundX:
            PointerX += 1
        else:
            AskMovement("d")

    elif Movement == "quit":
        sys.exit()

    else:
        print("Invalid Input")

    print(PointerX, PointerY)



Starting = True

while True:
    if Starting:
        AskMovement("StartingInput")
        Starting = False
    else:
        Movement = input("Movement: ")
        Pointer(Movement)





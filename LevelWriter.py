import numpy
from Constants import Sprites
import math
import os
import time

Percentage = 0
PercentageBefore = 0


def WriteBackUp():
    Level = __import__("Level1")
    LevelData = Level.LevelData
    numpy.save('Levels/Level1.npy', LevelData)

def WriteLevelToFile(LevelName, Level):
    numpy.save(LevelName + '.npy', Level)
    print("Level Saved")

def DeconstructArray(ConstructedArray):
    ConversionNumber = 0
    x = ConstructedArray.shape[1]
    y = ConstructedArray.shape[0]
    DeconstructedArray = numpy.array([])
    for i in range(y):
        for j in range(x):
            for key, value in Sprites.items():
                if value == ConstructedArray[i][j]:
                    DeconstructedArray = numpy.append(DeconstructedArray, key)
                    ConversionNumber = ConversionNumber + 1
                    CalculatePercentage(ConversionNumber, y * x)

    DeconstructedArray = DeconstructedArray.reshape(ConstructedArray.shape[0], ConstructedArray.shape[1])
    return DeconstructedArray

def PercentageLoader(Percentage, PercentageBefore):
    if Percentage != 100:
        if Percentage != PercentageBefore:  
            print("Deconstructing: " + str(Percentage) + "%")
            
    else:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("Deconstructing: " + str(Percentage) + "%")
        print("Deconstruction Complete")

def CalculatePercentage(ConversionNumber, TotalBlocks):
    global Percentage
    PercentageBefore = Percentage
    Percentage = ConversionNumber / TotalBlocks
    Percentage = Percentage * 100
    Percentage = math.floor(Percentage)
    PercentageLoader(Percentage, PercentageBefore)

def ChangePoints(X, Y, LevelArray, NewValue):
    global Sprites
    LevelArray[Y][X] = Sprites[NewValue]
    print("Point Changed to " + LevelArray[Y][X] + "")

def MultiChangePoints(X1, Y1, X2, Y2, LevelArray, NewValue):
    global Sprites
    for i in range(Y1, Y2):
        for j in range(X1, X2):
            LevelArray[i][j] = Sprites[NewValue]
            print("Point" + str(j) + ", " + str(i) + " Changed to " + LevelArray[i][j] + "")

def CreateLevel(LevelName):
    X = 16
    Y = 9
    global Sprites
    LevelArray = numpy.array([])
    for i in range(Y):
        for j in range(X):
            LevelArray = numpy.append(LevelArray, "w")
    LevelArray = LevelArray.reshape(Y, X)
    WriteLevelToFile(LevelName, LevelArray)
    return "Level Created"
    

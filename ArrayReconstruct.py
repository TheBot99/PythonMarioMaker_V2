import math
import numpy
import os
import time
from Constants import *

ConversionNumber = 0
Percentage = 0



def Reconstruct(PassThroughLevelName):
    global LevelName
    LevelName = PassThroughLevelName
    del PassThroughLevelName
    global LevelData
    LevelData = numpy.load(LevelName + ".npy")
    global y
    y = LevelData.shape[0]
    print(y)
    global x
    x = LevelData.shape[1]

    def PercentageLoader(Percentage, PercentageBefore):
            
        if Percentage != 100:
            if Percentage != PercentageBefore:  
                print("Reconstructing: " + str(Percentage) + "%")
                
        else:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print("Reconstructing: " + str(Percentage) + "%")
            print("Reconstruction Complete")
        
    def CalculatePercentage(ConversionNumber, TotalBlocks):
        global Percentage
        PercentageBefore = Percentage
        Percentage = ConversionNumber / TotalBlocks
        Percentage = Percentage * 100
        Percentage = math.floor(Percentage)
        PercentageLoader(Percentage, PercentageBefore)

    def ReconstructArray():
        global ConversionNumber
        global LevelData
        global y
        global x
        global LevelName
        global Sprites
        global BlockArray
        BlockArray = numpy.array([])

        for i in range(y):
            for j in range(x):
                BlockArray = numpy.append(BlockArray, Sprites[LevelData[i][j]])
                ConversionNumber = ConversionNumber + 1
                CalculatePercentage(ConversionNumber, y * x)
                
        return numpy.reshape(BlockArray, (y, x))

    BlockLevelArray = ReconstructArray()

    global BlockArray
    global Sprites
    global ConversionNumber
    global Percentage

    del ConversionNumber
    del LevelData
    del y
    del x
    del LevelName
    del Sprites
    del BlockArray
    del CalculatePercentage
    del PercentageLoader
    del Percentage
    del ReconstructArray

    return BlockLevelArray
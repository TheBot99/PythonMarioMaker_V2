import math
import numpy
import os
import time
from Constants import *





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
                return "Reconstructing: " + str(Percentage) + "%"
                
        else:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            return "Reconstructing: " + str(Percentage) + "%"
        
    def CalculatePercentage(ConversionNumber, TotalBlocks):
        Percentage = 0
        PercentageBefore = Percentage
        Percentage = ConversionNumber / TotalBlocks
        Percentage = Percentage * 100
        Percentage = math.floor(Percentage)
        FinalPercent = PercentageLoader(Percentage, PercentageBefore)
        return FinalPercent

    def ReconstructArray():
        ConversionNumber = 0

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
                Percentage = CalculatePercentage(ConversionNumber, y * x)
                print (Percentage)
                
                
        return numpy.reshape(BlockArray, (y, x))

    BlockLevelArray = ReconstructArray()

    global BlockArray
    global Sprites


    

    return BlockLevelArray , x , y
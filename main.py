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



FromFileLoadedLevelArray = ArrayReconstruct.Reconstruct(LevelDirectory)
LevelArray = MakeArrayALevel.MakeLevel(FromFileLoadedLevelArray)
print(LevelArray)
DeconstructedArray = LevelWriter.DeconstructArray(FromFileLoadedLevelArray)
LevelWriter.WriteLevelToFile(LevelDirectory, DeconstructedArray)






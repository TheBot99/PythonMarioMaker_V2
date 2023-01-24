import numpy

LevelName = "Level1"
Level =  __import__(LevelName)

LevelData = Level.LevelData

y = LevelData.shape[0]
x = LevelData.shape[1]
print(x,y)



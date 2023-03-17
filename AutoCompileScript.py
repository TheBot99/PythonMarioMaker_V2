import os

command = open("CompiledToEXE/COMMAND.txt", "r")



os.chdir("CompiledToEXE")
os.system(command.read())
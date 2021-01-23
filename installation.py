import os

def installFile(name):
    instfile = open(name, "r")
    for line in instfile:
        command = "pip install " + line.strip()
        os.system(command)

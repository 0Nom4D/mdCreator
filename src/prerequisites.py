#!/usr/bin/env python3

def cPlusPlusPrerequisites(fileDesc):
    fileDesc.write("To use this project, you'll need C++.\n\n")
    return (0)

def pythonPrerequisites(fileDesc):
    fileDesc.write("To use this project, you'll need python.\n")
    return (0)

def cPrerequisites(fileDesc):
    fileDesc.write("To use this project, you'll need C.\n\n")
    return (0)

def haskellPrerequisites(fileDesc):
    fileDesc.write("To use this project, you'll need haskell.\n\n")
    return (0)

def noPrerequisites(fileDesc):
    fileDesc.write("mdCreator didn't find your language prerequisites. Please edit this part.\n\n")
    return (0)
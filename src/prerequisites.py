#!/usr/bin/env python3

def cPlusPlusPrerequisites(fileDesc):
    fileDesc.write("To use this project, you'll need G++ Compiler.\n\n")
    return (0)

def pythonPrerequisites(fileDesc):
    fileDesc.write("To use this project, you'll need Python (Version 3.8):\n\n* [Python Installation](https://www.python.org/downloads/)\n")
    return (0)

def cPrerequisites(fileDesc):
    fileDesc.write("To use this project, you'll need GCC Compiler.\n\n")
    return (0)

def haskellPrerequisites(fileDesc):
    fileDesc.write("To use this project, you'll need Stack:\n\n* [Stack Installation Guide](https://docs.haskellstack.org/en/stable/install_and_upgrade/)\n")
    return (0)

def noPrerequisites(fileDesc):
    fileDesc.write("mdCreator didn't find your language prerequisites. Please edit this part.\n\n")
    return (0)
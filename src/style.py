#!/usr/bin/env python3

def noStyle(fileDesc, language, project):
    fileDesc.write(project + " is developed with " + language + ". EPITECH doesn't impose any Coding Style to this but I tried to be as cleaner as possible.\n\n")
    return (0)

def cStyle(fileDesc, language, project):
    fileDesc.write(project + " is developed with " + language + ". " + project + " is compliant with **EPITECH C / C++ Coding Style**.\n\n")
    return (0)

def haskellStyle(fileDesc, language, project):
    fileDesc.write(project + " is developed with " + language + ". " + project + " is compliant with **EPITECH Haskell Coding Style**.\n\n")
    return (0)
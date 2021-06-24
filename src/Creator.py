#!/usr/bin/env python3

from Prerequisites import cPlusPlusPrerequisites, pythonPrerequisites, cPrerequisites, haskellPrerequisites, noPrerequisites
from CodingStyle import cStyle, haskellStyle, noStyle
from ApiLoader import ApiLoader
import json
import os

def find_config(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return (os.path.join(root, name))
    return ("")

class mdCreator:
    def __init__(self, projName, usedLang, gifAttr, arrOpt):
        self.project = projName
        if gifAttr is None:
            self.gifAttr = ""
        else:
            self.gifAttr = gifAttr
        self.language = usedLang
        self.fileDesc = None
        self.array = arrOpt

        self.student = False
        self.apiLoader = ApiLoader(url="https://g.tenor.com/v1/search?", search=gifAttr, limit=2)

    #Main Loop
    def launchCreator(self):
        f = 0
        index = 0
        value = 0

        self.checkExisting()
        self.addSections()
        if self.apiLoader.build:
            self.fileDesc.write("## Asked GIFS\n\n")
            gifList = self.apiLoader.searchGifs()
            while index < len(gifList):
                self.fileDesc.write("![Alt Text](" + gifList[index] + ")\n")
                index += 1
            self.fileDesc.write("\n")
        if self.array is True:
            self.printArray()
        self.fileDesc.write("\n\nThis README file has been created with mdCreator. [Please check the project by clicking this link](https://github.com/0Nom4D/mdCreator/)")
        self.fileDesc.close()
        print("\nREADME.md created.")
        print("Don't forget to edit your README.md file if something's wrong with the existing file.")
        print("if any error occurs, please create an issue or contact Nom4D- | NMS#0811 on Discord.")

    def printArray(self):
        self.fileDesc.write("## Asked Array Template:\n\n\
| Index1     | Index2        |\n\
| ---------- |:-------------:|\n\
| Key 1      | Opt1          |\n\
| Key 2      | Opt2          |\n\
| Key 3      | Opt3          |\n\
| Key 4      | Opt4          |\n\
| Key 5      | Opt5          |\n\
| Key 6      | Opt6          |\n\
| Key 7      | Opt7          |\n")

    def checkExisting(self):
        if os.path.isfile("README.md"):
            while 1:
                try:
                    value = input("README.md already exists. Do you want to create a new README.md file? [y/n] ")
                    if value == 'y':
                        self.fileDesc = open("README.md", "w")
                        self.fileDesc.truncate()
                        break
                    elif value == 'n':
                        exit(1)
                    else:
                        continue
                except EOFError as inputError:
                    print("mdCreator Stopped - creator.py: l.75")
                    exit(1)
        else:
            self.fileDesc = open("README.md", "w")
        return (0)

    #README.md Sections
    def addSections(self):
        configFile = []

        try:
            configFile = find_config("mdCreator.json", os.getenv('HOME'))
            config = open(configFile, "r")
            cfg = json.load(config)
            for lib in cfg:
                self.writeSection(cfg, lib)
        except KeyError as err:
            (x,) = err.args
            print("KeyError: " + x)
            exit(1)

    def writeSection(self, cfg, section):
        secRange = 0

        try:
            secRange = cfg[section]["range"]
        except KeyError:
            secRange = None
        if self.detect_section(secRange) is False:
            if section == "gifs":
                self.apiLoader.limit = int(cfg[section]["nbGifs"])
                self.apiLoader.buildUrl()
                return (0)
            raise Exception("RangeError", "Range is not set for " + str(section) + " section.")
        return self.redirectSections(secRange, cfg, section)

    def detect_section(self, secRange):
        if secRange is None:
            return False
        return True

    def redirectSections(self, secRange, cfg, section):
        if secRange < 1:
            raise Exception("RangeError", "Range must be higher than 0 for " + str(section) + " section.")
        while secRange != 0:
            self.fileDesc.write("#")
            secRange -= 1
        if section == "header":
            self.fileDesc.write(" " + self.project + "\n\n")
        elif cfg[section]["title"] is not None:
            self.fileDesc.write(" " + cfg[section]["title"] + "\n\n")
        if section == "style":
            self.printCodingStyle()
        elif section == "prerequisites":
            self.printPrerequisites()
        elif cfg[section]["description"][0] == ' ':
            self.fileDesc.write(self.project + cfg[section]["description"] + "\n\n")
        else:
            self.fileDesc.write(cfg[section]["description"] + "\n\n")
        return (0)

    def printPrerequisites(self):
        return({
            "c++": cPlusPlusPrerequisites,
            "c": cPrerequisites,
            "python": pythonPrerequisites,
            "haskell": haskellPrerequisites
        }.get(self.language.lower(), noPrerequisites)(self.fileDesc))

    def printCodingStyle(self):
        return ({
            "c": cStyle,
            "haskell": haskellStyle
        }.get(self.language.lower(), noStyle)(self.fileDesc, self.language, self.project))


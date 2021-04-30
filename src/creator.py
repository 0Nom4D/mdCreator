#!/usr/bin/env python3

from style import *
import requests
import os.path
import json

class mdCreator:
    def __init__(self, gifAttr, projName, usedLang, arrOpt):
        self.project = projName
        if gifAttr is None:
            self.gifAttr = ""
        else:
            self.gifAttr = gifAttr
        self.language = usedLang
        self.fileDesc = None
        self.array = arrOpt

    #Main Loop
    def launchCreator(self):
        f = 0
        index = 0
        value = 0

        self.checkExisting()
        self.addSections()
        if self.gifAttr != "":
            self.fileDesc.write("## Asked GIFS\n\n")
            gifList = self.getGifsUrl()
            while index < len(gifList):
                self.fileDesc.write("![Alt Text](" + gifList[index] + ")<br/>\n")
                index += 1
            self.fileDesc.write("\n")
        if self.array == True:
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
                    print()
                    exit(1)
        else:
            self.fileDesc = open("README.md", "w")
        return (0)

    #README.md Sections
    def addSections(self):
        _range = 0
        i = 0

        try:
            config = open("mdCreator.json", "r")
            cfg = json.load(config)
            for lib in cfg:
                self.writeSection(cfg, lib)
        except Exception as err:
            print("Fatal Error: " + str(err.args[0]))
            exit(1)

    def writeSection(self, cfg, lib):
        _range = cfg[lib]["range"]
        if _range < 1:
            print("mdCreator stopped: the " + str(lib) + "'s range is negative. Range must be between 1 and 3.")
            exit(1)
        while _range != 0:
            self.fileDesc.write("#")
            _range -= 1
        if lib == "header":
            self.fileDesc.write(" " + self.project + "\n\n")
        elif cfg[lib]["title"] is not None:
            self.fileDesc.write(" " + cfg[lib]["title"] + "\n\n")
        if lib == "style":
            self.printCodingStyle()
        elif cfg[lib]["description"][0] == ' ':
            self.fileDesc.write(self.project + cfg[lib]["description"] + "\n\n")
        else:
            self.fileDesc.write(cfg[lib]["description"] + "\n\n")
        return (0)

    def printCodingStyle(self):
        return ({
            "c": cStyle,
            "haskell": haskellStyle
        }.get(self.language.lower(), noStyle)(self.fileDesc, self.language, self.project))

    #Gifs Tenor API
    def getGifsUrl(self):
        apikey = "CSGXSUKBREYZ"
        gifsUrls = []

        r = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (self.gifAttr, apikey, 2, "minimal"))
        if r.status_code == 200 or r.status_code == 202:
            values = json.loads(r.content)
            for gif in values["results"]:
                for media in gif["media"]:
                    gifsUrls.append(media["gif"]["url"])
        else:
            print("HTTP Request Error: " + str(r.status_code))
            print("Reason: " + str(r.content))
            exit(1)
        return gifsUrls

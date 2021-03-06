#!/usr/bin/env python3
import configparser

from sources.Prerequisites import cPlusPlusPrerequisites, pythonPrerequisites, cPrerequisites, haskellPrerequisites, \
    noPrerequisites
from dotenv import dotenv_values, load_dotenv, set_key, find_dotenv
from sources.CodingStyle import cStyle, haskellStyle, noStyle
from sources.ApiLoader.ApiLoader import ApiLoader
from typing import Union, Optional
from inspect import currentframe
import json
import os


def find_config(name, path) -> str:
    """
    Find recursively a file in a directory.

    Parameters
    -------
    name : str
        Name of the file you're looking for
    path : str
        Starting directory to find

    Returns
    -------
    Returns the path to the file you're looking for
    """
    for root, dirs, files in os.walk(path):
        if name in files:
            if "mdCreator" in os.path.join(root, name):
                return os.path.join(root, name)
    return ""


class RangeError(Exception):
    """
    Exception raised when error occurs with Range Option from configuration file.

    Attributes
    ----------
    message : str
        Exception explanation
    """

    def __init__(self, message):
        """
        Constructs an actual Range Error Exception class.

        Parameters
        ----------
        message : str
            Message explaning the Range Error
        """
        self.message = message

    def __str__(self):
        """
        Returns the actual error message.

        Returns
        -------
        Actual Range Error message.
        """
        return f'RangeError: {self.message}'


class mdCreator:
    """
    Main project class having the main computing loop.

    Attributes
    ----------
    project : str
        Project's name
    gifAttr : str
        String defining the gifs you're looking for
    language : str
        Project's main language
    fileDesc : TextIOWrapper | None
        File descriptor describing the new README file descriptor
    arrOpt : bool
        Boolean telling if the user wants an array in its README file
    student : bool
        Boolean telling if the user is a student
    apiLoader : ApiLoader
        Class making every Tenor's Api calls
    """

    def __init__(self, projName, usedLang, gifAttr, arrOpt):
        self._envPath = find_config(".env", os.getenv("HOME"))
        if self._envPath == "":
            print("mdCreator .env file must be located in the mdCreator directory.")
            exit(1)
        self._envDict = dotenv_values(self._envPath)
        self._envFile = find_dotenv()
        load_dotenv(self._envFile)

        self.project = projName
        if gifAttr is None:
            self.gifAttr = ''
        else:
            self.gifAttr = gifAttr
        print(self.gifAttr)
        self.language = usedLang
        self.fileDesc = None
        self.array = arrOpt

        self.student = False
        self.apiLoader = ApiLoader(url="https://g.tenor.com/v1/search?", search=gifAttr, limit=2)

    # Main Loop
    def launchCreator(self) -> None:
        """
        Main loop function creating the README file.

        Returns
        -------
        None
        """
        index = 0

        self.checkExisting()
        self.loadConfig()
        if self.apiLoader.isUrlBuild():
            self.fileDesc.write("## Asked GIFS\n\n")
            gifList = self.apiLoader.searchGifs()
            while index < len(gifList):
                self.fileDesc.write(f'![Alt Text]({gifList[index]})\n')
                index += 1
            self.fileDesc.write("\n")
        if self.array is True:
            self.printArray()
        self.fileDesc.write(
            "\nThis README file has been created with mdCreator. [Please check the project by clicking this link.]("
            "https://github.com/0Nom4D/mdCreator/)\n")
        self.fileDesc.close()
        print("\nREADME.md created.")
        print("Don't forget to edit your README.md file if something's wrong with the existing file.")
        print("if any error occurs, please create an issue or contact Nom4D- | NMS#0811 on Discord.")

    def printArray(self) -> None:
        """
        Writing an array in the user README file.

        Returns
        -------
        None
        """
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

    def checkExisting(self) -> None:
        """
        Checks if a README file already exists into the directory.

        Returns
        -------
        None
        """
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
                except EOFError:
                    print(f"mdCreator Stopped - creator.py: l.{currentframe()}")
                    exit(1)
        else:
            self.fileDesc = open("README.md", "w")

    # README.md Sections
    def loadConfig(self) -> None:
        """
        Load configuration file.

        Returns
        -------
        None
        """
        def checkConfigMode() -> None:
            inputValue = None

            if "CONFIGTYPE" in self._envDict and self._envDict["CONFIGTYPE"] in ['student', 'pro']:
                return
            while inputValue is None:
                try:
                    inputValue = input("For your next use, would you like to use the Student Configuration? [y/n] ")
                    if inputValue == 'y':
                        set_key(self._envFile, "CONFIGTYPE", 'student')
                    elif inputValue == 'n':
                        set_key(self._envFile, "CONFIGTYPE", 'pro')
                    else:
                        continue
                except KeyError:
                    print(f"mdCreator Stopped - creator.py: l.{currentframe()}")
                    exit(1)

        def getAPIKey() -> None:
            inputValue = None

            if "APIKEY" in self._envDict and self._envDict["APIKEY"] != '':
                return
            while inputValue is None:
                try:
                    inputValue = input("In order to make mdCreator work, you need to input your Tenor API Key.\nYou can get a tutorial to how to get one at https://github.com/0Nom4D/mdCreator/wiki/API-Key-Registration.\nYour API Key: ")
                    set_key(self._envFile, 'APIKEY', inputValue)
                except KeyError:
                    print(f"mdCreator Stopped - creator.py: l.{currentframe()}")
                    exit(1)

        checkConfigMode()
        if self.gifAttr != '':
            getAPIKey()

        # Refreshes Environment Values
        self._envDict = dotenv_values(self._envPath)

        # Loading mdCreator.json config file
        configFile = find_config("mdCreator.json", os.environ['HOME'])
        config = open(configFile, "r")
        cfg = json.load(config)
        for section in cfg[self._envDict["CONFIGTYPE"]]:
            self.writeSection(cfg[self._envDict["CONFIGTYPE"]], section)

    def writeSection(self, cfg, section: Union[str, Optional[str]]) -> Union[int, None]:
        """
        Write every sections and checks the configuration.

        Parameters
        -------
        cfg : list
            List of every sections present in the configuration file
        section : list
            List of every parameters of a section

        Returns
        -------
        None
        """
        secRange = 0

        try:
            secRange = cfg[section]["range"]
        except KeyError:
            secRange = None
        if secRange is None:
            if section == "gifs":
                self.apiLoader.setLimit(int(cfg[section]["nbGifs"]))
                self.apiLoader.buildUrl(self._envDict["APIKEY"])
                return 0
            raise RangeError(f'Range is not set for {str(section)} section.')
        return self.redirectSections(secRange, cfg, section)

    def redirectSections(self, secRange, cfg, section) -> Union[int, None]:
        """
        Write the different README sections.

        Parameters
        -------
        secRange : int
            Section range
        cfg : list
            List of every sections present in the configuration file
        section : list
            List of every parameters of a section

        Returns
        -------
        None
        """
        if secRange < 1:
            raise RangeError(f'Range must be higher than 0 for {str(section)} section.')
        while secRange != 0:
            self.fileDesc.write("#")
            secRange -= 1
        if section == "header":
            self.fileDesc.write(f' {self.project}\n\n')
        elif cfg[section]["title"] is not None:
            self.fileDesc.write(f'{cfg[section]["title"]}\n\n')
        if section == "style":
            self.printCodingStyle()
        elif section == "prerequisites":
            self.printPrerequisites()
        elif cfg[section]["description"][0] == ' ':
            self.fileDesc.write(f'{self.project}{cfg[section]["description"]}\n\n')
        else:
            self.fileDesc.write(f'{cfg[section]["description"]}\n\n')
        return 0

    def printPrerequisites(self) -> int:
        """
        Write prerequisites in the created README file.
        """
        return ({
                    "c++": cPlusPlusPrerequisites,
                    "c": cPrerequisites,
                    "python": pythonPrerequisites,
                    "haskell": haskellPrerequisites
                }.get(self.language.lower(), noPrerequisites)(self.fileDesc))

    def printCodingStyle(self) -> int:
        """
        Write coding style in the created README file.
        """
        return ({
                    "c": cStyle,
                    "haskell": haskellStyle
                }.get(self.language.lower(), noStyle)(self.fileDesc, self.language, self.project))

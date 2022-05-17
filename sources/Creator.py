#!/usr/bin/env python3
import configparser

from sources.Prerequisites import c_plus_plus_prerequisites, python_prerequisites, c_prerequisites, haskell_prerequisites, \
    no_prerequisites
from dotenv import dotenv_values, load_dotenv, set_key, find_dotenv
from sources.CodingStyle import c_style, haskell_style, no_style
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


class MdCreator:
    """
    Main project class having the main computing loop.

    Attributes
    ----------
    project : str
        Project's name
    gif_keywords : str
        String defining the gifs you're looking for
    language : str
        Project's main language
    fileDesc : TextIOWrapper | None
        File descriptor describing the new README file descriptor
    array_option : bool
        Boolean telling if the user wants an array in its README file
    student : bool
        Boolean telling if the user is a student
    apiLoader : ApiLoader
        Class making every Tenor's Api calls
    """

    def __init__(self, project_name, project_language, gif_keywords, array_option):
        self._envPath = find_config(".env", os.getenv("HOME"))
        if self._envPath == "":
            print("mdCreator .env file must be located in the mdCreator directory.")
            exit(1)
        self._envDict = dotenv_values(self._envPath)
        self._envFile = find_dotenv()
        load_dotenv(self._envFile)

        self.project = project_name
        if gif_keywords is None:
            self.gifAttr = ''
        else:
            self.gifAttr = gif_keywords
        print(self.gifAttr)
        self.language = project_language
        self.fileDesc = None
        self.array = array_option

        self.student = False
        self.apiLoader = ApiLoader(url="https://g.tenor.com/v1/search?", search=gif_keywords, limit=2)

    # Main Loop
    def launch_creator(self) -> None:
        """
        Main loop function creating the README file.

        Returns
        -------
        None
        """
        index = 0

        self.check_existing()
        self.load_config()
        if self.apiLoader.is_url_build():
            self.fileDesc.write("## Asked GIFS\n\n")
            gif_list = self.apiLoader.search_gifs()
            while index < len(gif_list):
                self.fileDesc.write(f'![Alt Text]({gif_list[index]})\n')
                index += 1
            self.fileDesc.write("\n")
        if self.array is True:
            self.print_array()
        self.fileDesc.write(
            "\nThis README file has been created with mdCreator. [Please check the project by clicking this link.]("
            "https://github.com/0Nom4D/mdCreator/)\n")
        self.fileDesc.close()
        print("\nREADME.md created.")
        print("Don't forget to edit your README.md file if something's wrong with the existing file.")
        print("if any error occurs, please create an issue or contact Nom4D- | NMS#0811 on Discord.")

    def print_array(self) -> None:
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

    def check_existing(self) -> None:
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
    def load_config(self) -> None:
        """
        Load configuration file.

        Returns
        -------
        None
        """
        def check_config_mode() -> None:
            input_value = None

            if "CONFIGTYPE" in self._envDict and self._envDict["CONFIGTYPE"] in ['student', 'pro']:
                return
            while input_value is None:
                try:
                    input_value = input("For your next use, would you like to use the Student Configuration? [y/n] ")
                    if input_value == 'y':
                        set_key(self._envFile, "CONFIGTYPE", 'student')
                    elif input_value == 'n':
                        set_key(self._envFile, "CONFIGTYPE", 'pro')
                    else:
                        continue
                except KeyError:
                    print(f"mdCreator Stopped - creator.py: l.{currentframe()}")
                    exit(1)

        def get_api_key() -> None:
            input_value = None

            if "APIKEY" in self._envDict and self._envDict["APIKEY"] != '':
                return
            while input_value is None:
                try:
                    input_value = input("In order to make mdCreator work, you need to input your Tenor API Key.\nYou can get a tutorial to how to get one at https://github.com/0Nom4D/mdCreator/wiki/API-Key-Registration.\nYour API Key: ")
                    set_key(self._envFile, 'APIKEY', input_value)
                except KeyError:
                    print(f"mdCreator Stopped - creator.py: l.{currentframe()}")
                    exit(1)

        check_config_mode()
        if self.gifAttr != '':
            get_api_key()

        # Refreshes Environment Values
        self._envDict = dotenv_values(self._envPath)

        # Loading mdCreator.json config file
        config_file = find_config("mdCreator.json", os.environ['HOME'])
        config = open(config_file, "r")
        cfg = json.load(config)
        for section in cfg[self._envDict["CONFIGTYPE"]]:
            self.write_section(cfg[self._envDict["CONFIGTYPE"]], section)

    def write_section(self, cfg, section: Union[str, Optional[str]]) -> Union[int, None]:
        """
        Write every section and checks the configuration.

        Parameters
        -------
        cfg : list
            List of every sections present in the configuration file
        section : list
            List of every parameter of a section

        Returns
        -------
        None
        """
        sec_range = 0

        try:
            sec_range = cfg[section]["range"]
        except KeyError:
            sec_range = None
        if sec_range is None:
            if section == "gifs":
                self.apiLoader.set_limit(int(cfg[section]["nbGifs"]))
                self.apiLoader.build_url(self._envDict["APIKEY"])
                return 0
            raise RangeError(f'Range is not set for {str(section)} section.')
        return self.redirect_sections(sec_range, cfg, section)

    def redirect_sections(self, sec_range, cfg, section) -> Union[int, None]:
        """
        Write the different README sections.

        Parameters
        -------
        sec_range : int
            Section range
        cfg : list
            List of every sections present in the configuration file
        section : list
            List of every parameter of a section

        Returns
        -------
        None
        """
        if sec_range < 1:
            raise RangeError(f'Range must be higher than 0 for {str(section)} section.')
        while sec_range != 0:
            self.fileDesc.write("#")
            sec_range -= 1
        if section == "header":
            self.fileDesc.write(f' {self.project}\n\n')
        elif cfg[section]["title"] is not None:
            self.fileDesc.write(f'{cfg[section]["title"]}\n\n')
        if section == "style":
            self.print_coding_style()
        elif section == "prerequisites":
            self.print_prerequisites()
        elif cfg[section]["description"][0] == ' ':
            self.fileDesc.write(f'{self.project}{cfg[section]["description"]}\n\n')
        else:
            self.fileDesc.write(f'{cfg[section]["description"]}\n\n')
        return 0

    def print_prerequisites(self) -> int:
        """
        Write prerequisites in the created README file.
        """
        return ({
                    "c++": c_plus_plus_prerequisites,
                    "c": c_prerequisites,
                    "python": python_prerequisites,
                    "haskell": haskell_prerequisites
                }.get(self.language.lower(), no_prerequisites)(self.fileDesc))

    def print_coding_style(self) -> int:
        """
        Write coding style in the created README file.
        """
        return ({
                    "c": c_style,
                    "haskell": haskell_style
                }.get(self.language.lower(), no_style)(self.fileDesc, self.language, self.project))

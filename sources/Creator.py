#!/usr/bin/env python3
import configparser

from sources.Prerequisites import c_plus_plus_prerequisites, python_prerequisites, c_prerequisites, haskell_prerequisites, no_prerequisites
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
            Message explaining the Range Error
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
    template_name : str
        Template's name the user wants to base its README on
    project : str
        Project's name
    gif_keywords : str
        String defining the gifs you're looking for
    language : str
        Project's main language
    file_desc : TextIOWrapper | None
        File descriptor describing the new README file descriptor
    array : bool
        Boolean telling if the user wants an array in its README file
    use_config : bool
        Boolean telling if the user is a student
    api_loader : ApiLoader
        Class making every Tenor's Api calls
    """

    def __init__(self, options):
        self._envPath = find_config(".env", os.getenv("HOME"))
        if self._envPath == "":
            print("mdCreator .env file must be located in the mdCreator directory.")
            exit(1)
        self._env_dict = dotenv_values(self._envPath)
        self._env_file = find_dotenv()
        load_dotenv(self._env_file)

        self.project = options.project_name
        self.gif_keywords = ''
        if options.gif_keywords is not None:
            self.gif_keywords = options.gif_keywords
        self.language = options.language
        self.file_desc = None
        self.array = options.asked_array
        self.template_name = options.template_name

        if self.template_name is not None:
            self.use_config = False
        self.api_loader = ApiLoader(url="https://g.tenor.com/v1/search?", limit=5)

    # Main Loop
    def launch_creator(self) -> None:
        """
        Main loop function creating the README file.

        Returns
        -------
        None
        """
        self.check_existing()
        self.load_config()
        self.get_gifs()
        if self.array is True:
            self.print_array()
        self.file_desc.write("\nThis README file has been created with mdCreator. [Please check the project by clicking this link.](""https://github.com/0Nom4D/mdCreator/)\n")
        self.file_desc.close()
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
        self.file_desc.write(
            "## Asked Array Template:\n\n"
            "| Index1     | Index2        |\n"
            "|:----------:|:-------------:|\n"
            "| Key 1      | Opt1          |\n"
            "| Key 2      | Opt2          |\n"
            "| Key 3      | Opt3          |\n"
            "| Key 4      | Opt4          |\n"
            "| Key 5      | Opt5          |\n"
            "| Key 6      | Opt6          |\n"
            "| Key 7      | Opt7          |\n"
        )

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
                        self.file_desc = open("README.md", "w")
                        self.file_desc.truncate()
                        break
                    elif value == 'n':
                        exit(1)
                    else:
                        continue
                except EOFError:
                    print(f"mdCreator Stopped - creator.py: l.{currentframe()}")
                    exit(1)
        else:
            self.file_desc = open("README.md", "w")

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

            if "CONFIGTYPE" in self._env_dict and self._env_dict["CONFIGTYPE"] in ['student', 'pro']:
                return
            while input_value is None:
                try:
                    input_value = input("For your next use, would you like to use the Student Configuration? [y/n] ")
                    if input_value == 'y':
                        set_key(self._env_file, "CONFIGTYPE", 'student')
                    elif input_value == 'n':
                        set_key(self._env_file, "CONFIGTYPE", 'pro')
                    else:
                        continue
                except KeyError:
                    print(f"mdCreator Stopped - creator.py: l.{currentframe()}")
                    exit(1)

        check_config_mode()

        # Refreshes Environment Values
        self._env_dict = dotenv_values(self._envPath)
        self.use_config = True

        # Loading mdCreator.json config file
        config_file = find_config("mdCreator.json", os.environ['HOME'])
        fd_config = open(config_file, "r")
        config = json.load(fd_config)
        for section in config[self._env_dict["CONFIGTYPE"]]:
            self.write_section(config[self._env_dict["CONFIGTYPE"]], section)
        fd_config.close()

    def write_section(self, config, section) -> Union[int, None]:
        """
        Write every section and checks the configuration.

        Parameters
        -------
        config : list
            List of every sections present in the configuration file
        section : list
            List of every parameter of a section

        Returns
        -------
        None
        """
        sec_range = 0

        try:
            sec_range = config[section]["range"]
        except KeyError:
            sec_range = None
        if sec_range is None:
            if section == "gifs":
                return 0
            raise RangeError(f'Range is not set for {str(section)} section.')
        return self.redirect_sections(sec_range, config, section)

    def redirect_sections(self, sec_range, config, section) -> Union[int, None]:
        """
        Write the different README sections.

        Parameters
        -------
        sec_range : int
            Section range
        config : list
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
            self.file_desc.write("#")
            sec_range -= 1
        if section == "header":
            self.file_desc.write(f' {self.project}\n\n')
        elif config[section]["title"] is not None:
            self.file_desc.write(f'{config[section]["title"]}\n\n')
        if section == "style":
            self.print_coding_style()
        elif section == "prerequisites":
            self.print_prerequisites()
        elif config[section]["description"][0] == ' ':
            self.file_desc.write(f'{self.project}{config[section]["description"]}\n\n')
        else:
            self.file_desc.write(f'{config[section]["description"]}\n\n')
        return 0

    def ask_api_key(self) -> None:
        """
        Asks the user for its Tenor API Key

        Returns
        -------
        None
        """
        input_value = None

        if "APIKEY" in self._env_dict and self._env_dict["APIKEY"] != '':
            return
        while input_value is None:
            try:
                input_value = input("In order to make mdCreator work, you need to input your Tenor API Key.\nYou can get a tutorial to how to get one at https://github.com/0Nom4D/mdCreator/wiki/API-Key-Registration.\nYour API Key: ")
                set_key(self._env_file, 'APIKEY', input_value)
            except KeyError:
                print(f"mdCreator Stopped - creator.py: l.{currentframe()}")
                exit(1)

    def get_gifs(self) -> None:
        """
        Setups GIF ApiLoader if the user uses the configuration mode and build the Tenor API route.

        Returns
        -------
        None
        """

        def setup_gifs() -> None:
            config_file = find_config("mdCreator.json", os.environ['HOME'])
            fd_config = open(config_file, "r")
            config = json.load(fd_config)
            self.api_loader.set_limit(config[self._env_dict["CONFIGTYPE"]]["gifs"]["nbGifs"])
            fd_config.close()

        if self.gif_keywords != '':
            self.ask_api_key()
            self._env_dict = dotenv_values(self._envPath)
            if self.use_config:
                setup_gifs()
            self.api_loader.build_url(self.gif_keywords, self._env_dict["APIKEY"])
            if self.api_loader.is_url_build():
                self.file_desc.write("## Asked GIFS\n\n")
                gif_list = self.api_loader.get_gifs()
                for gif in gif_list:
                    self.file_desc.write(f'![Alt Text]({gif})\n')
                self.file_desc.write("\n")

    def print_prerequisites(self) -> int:
        """
        Write prerequisites in the created README file.
        """
        return ({
                    "c++": c_plus_plus_prerequisites,
                    "c": c_prerequisites,
                    "python": python_prerequisites,
                    "haskell": haskell_prerequisites
                }.get(self.language.lower(), no_prerequisites)(self.file_desc))

    def print_coding_style(self) -> int:
        """
        Write coding style in the created README file.
        """
        return ({
                    "c": c_style,
                    "haskell": haskell_style
                }.get(self.language.lower(), no_style)(self.file_desc, self.language, self.project))

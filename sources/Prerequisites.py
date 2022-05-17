#!/usr/bin/env python3

def c_plus_plus_prerequisites(file_desc):
    """
    Writes the prerequisites depending on the main's project language.

    Parameters
    -------
    file_desc : TextIOWrapper | None
        File descriptor describing the README.md file
    """
    file_desc.write("To use this project, you'll need G++ Compiler.\n\n")
    return 0


def python_prerequisites(file_desc):
    """
    Writes the prerequisites depending on the main's project language.

    Parameters
    -------
    file_desc : TextIOWrapper | None
        File descriptor describing the README.md file
    """
    file_desc.write("To use this project, you'll need Python (Version 3.8):\n\n* [Python Installation]("
                   "https://www.python.org/downloads/)\n\n")
    return 0


def c_prerequisites(file_desc):
    """
    Writes the prerequisites depending on the main's project language.

    Parameters
    -------
    file_desc : TextIOWrapper | None
        File descriptor describing the README.md file
    """
    file_desc.write("To use this project, you'll need GCC Compiler.\n\n")
    return 0


def haskell_prerequisites(file_desc):
    """
    Writes the prerequisites depending on the main's project language.

    Parameters
    -------
    file_desc : TextIOWrapper | None
        File descriptor describing the README.md file
    """
    file_desc.write("To use this project, you'll need Stack:\n\n* [Stack Installation Guide]("
                   "https://docs.haskellstack.org/en/stable/install_and_upgrade/)\n\n")
    return 0


def no_prerequisites(file_desc):
    """
    Writes the prerequisites depending on the main's project language.

    Parameters
    -------
    file_desc : TextIOWrapper | None
        File descriptor describing the README.md file
    """
    file_desc.write("mdCreator didn't find your language prerequisites. Please edit this part.\n\n")
    return 0

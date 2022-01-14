#!/usr/bin/env python3

def cPlusPlusPrerequisites(fileDesc):
    """
    Writes the prerequisites depending on the main's project language.

    Parameters
    -------
    fileDesc : TextIOWrapper | None
        Filedescriptor describing the README.md file
    """
    fileDesc.write("To use this project, you'll need G++ Compiler.\n\n")
    return 0


def pythonPrerequisites(fileDesc):
    """
    Writes the prerequisites depending on the main's project language.

    Parameters
    -------
    fileDesc : TextIOWrapper | None
        Filedescriptor describing the README.md file
    """
    fileDesc.write("To use this project, you'll need Python (Version 3.8):\n\n* [Python Installation]("
                   "https://www.python.org/downloads/)\n\n")
    return 0


def cPrerequisites(fileDesc):
    """
    Writes the prerequisites depending on the main's project language.

    Parameters
    -------
    fileDesc : TextIOWrapper | None
        Filedescriptor describing the README.md file
    """
    fileDesc.write("To use this project, you'll need GCC Compiler.\n\n")
    return 0


def haskellPrerequisites(fileDesc):
    """
    Writes the prerequisites depending on the main's project language.

    Parameters
    -------
    fileDesc : TextIOWrapper | None
        Filedescriptor describing the README.md file
    """
    fileDesc.write("To use this project, you'll need Stack:\n\n* [Stack Installation Guide]("
                   "https://docs.haskellstack.org/en/stable/install_and_upgrade/)\n\n")
    return 0


def noPrerequisites(fileDesc):
    """
    Writes the prerequisites depending on the main's project language.

    Parameters
    -------
    fileDesc : TextIOWrapper | None
        Filedescriptor describing the README.md file
    """
    fileDesc.write("mdCreator didn't find your language prerequisites. Please edit this part.\n\n")
    return 0

#!/usr/bin/env python3

firstStand = " is developed with "


def noStyle(fileDesc, language, project):
    """
    Writes the coding style in the README file depending of the project main language.

    Parameters
    -------
    fileDesc : TextIOWrapper | None
        Filedescriptor describing the README.md file
    language : str
        Project Main's language
    project : str
        Project name
    """
    fileDesc.write(f'{project}{firstStand}{language}. EPITECH doesn\'t impose any Coding Style to this but I tried to be as cleaner as possible.\n\n')
    return 0


def cStyle(fileDesc, language, project):
    """
    Writes the coding style in the README file for C projects.

    Parameters
    -------
    fileDesc : TextIOWrapper | None
        Filedescriptor describing the README.md file
    language : str
        Project Main's language
    project : str
        Project name
    """
    fileDesc.write(f'{project}{firstStand}{language}. {project} is compliant with **EPITECH C / C++ Coding Style**.\n\n')
    return 0


def haskellStyle(fileDesc, language, project):
    """
    Writes the coding style in the README file for Haskell projects.

    Parameters
    -------
    fileDesc : TextIOWrapper | None
        Filedescriptor describing the README.md file
    language : str
        Project Main's language
    project : str
        Project name
    """
    fileDesc.write(f'{project}{firstStand}{language}. {project} is compliant with **EPITECH Haskell Coding Style**.\n\n')
    return 0
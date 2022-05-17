#!/usr/bin/env python3

firstStand = " is developed with "


def no_style(file_desc, language, project):
    """
    Writes the coding style in the README file depending on the project main language.

    Parameters
    -------
    file_desc : TextIOWrapper | None
        file_descriptor describing the README.md file
    language : str
        Project Main's language
    project : str
        Project name
    """
    file_desc.write(f'{project}{firstStand}{language}. EPITECH doesn\'t impose any Coding Style to this but I tried to be as cleaner as possible.\n\n')
    return 0


def c_style(file_desc, language, project):
    """
    Writes the coding style in the README file for C projects.

    Parameters
    -------
    file_desc : TextIOWrapper | None
        file_descriptor describing the README.md file
    language : str
        Project Main's language
    project : str
        Project name
    """
    file_desc.write(f'{project}{firstStand}{language}. {project} is compliant with **EPITECH C / C++ Coding Style**.\n\n')
    return 0


def haskell_style(file_desc, language, project):
    """
    Writes the coding style in the README file for Haskell projects.

    Parameters
    -------
    file_desc : TextIOWrapper | None
        file_descriptor describing the README.md file
    language : str
        Project Main's language
    project : str
        Project name
    """
    file_desc.write(f'{project}{firstStand}{language}. {project} is compliant with **EPITECH Haskell Coding Style**.\n\n')
    return 0

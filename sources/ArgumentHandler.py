#!/usr/bin/env python3

import argparse


def parse_args(args):
    """
    Parses arguments passed to the program.

    Parameters
    -------
    args : Sequence[str]
        List of arguments given as parameters

    Returns
    -------
    Class built depending on the arguments.
    """
    parser = argparse.ArgumentParser(prog="mdCreator", description='Options Parser for mdCreator')
    parser.add_argument('--template', required=False, dest='template_name', type=str, help='Template to fetch')
    parser.add_argument('-p', '--pname', required=True, dest='project_name', type=str, help='Project\'s Name')
    parser.add_argument('-l', '--language', required=True, dest='language', type=str, help='Project\'s Main Language')
    parser.add_argument('-a', '--array', dest='array', default=False, action='store_true', help='Adds an array template inside your README.md file')
    parser.add_argument('-g', '--gif', dest='gif_keywords', type=str, nargs='+', help='Keywords to find a gif')

    options = parser.parse_args(args)
    return options

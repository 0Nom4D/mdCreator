#!/usr/bin/env python3

import argparse
import sys

def parseArgs(args):
    parser = argparse.ArgumentParser(prog="mdCreator", description='Options Parser for mdCreator')
    parser.add_argument('-p', '--pname', required=True, dest='projectName', type=str, help='Project\'s Name')
    parser.add_argument('-l', '--language', required=True, dest='language', type=str, help='Project\'s Main Language')
    parser.add_argument('-a', '--array', dest='array', default=False, action='store_true', help='Adds an array template inside your README.md file')
    parser.add_argument('-g', '--gif', dest='gifKeywords', type=str, nargs='+', help='Keywords to find a gif')
    return (parser.parse_args(args))
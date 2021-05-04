#!/usr/bin/env python3

from argHandling import *
from creator import *
import sys

def main():
    args = parseArgs(sys.argv[1:])
    creator = mdCreator(args.projectName, args.language, args.gifKeywords, args.array)
    creator.launchCreator()
    return (0)

if __name__ == "__main__":
    exit(main())
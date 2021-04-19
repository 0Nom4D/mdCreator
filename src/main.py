#!/usr/bin/env python3

from argHandling import parseArgs
from creator import mdCreator
import sys

def main():
    args = parseArgs()
    creator = mdCreator(args.gifKeywords, args.projectName, args.language, args.array)
    creator.launchCreator()
    return (0)

if __name__ == "__main__":
    exit(main())
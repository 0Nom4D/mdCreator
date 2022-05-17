#!/usr/bin/env python3

from sources.ArgumentHandler import parse_args
from sources.Creator import MdCreator
import sys


def main():
    options = parse_args(sys.argv[1:])
    creator = MdCreator(options)
    creator.launch_creator()
    return 0


if __name__ == "__main__":
    exit(main())
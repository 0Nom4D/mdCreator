#!/usr/bin/env python3

from sources.ArgumentHandler import parse_args
from sources.Creator import MdCreator
import sys


def main():
    args = parse_args(sys.argv[1:])
    creator = MdCreator(args.project_name, args.language, args.gif_keywords, args.array)
    creator.launch_creator()
    return 0


if __name__ == "__main__":
    exit(main())
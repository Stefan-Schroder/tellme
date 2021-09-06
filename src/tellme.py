#!/usr/bin/python3

import sys #1
from os import environ #0
from decouple import config #1

def GetFishCommand():
    history_path = config('FISH_HIST_PATH')

def main():
    # get the last few line from config file
    command = GetFishCommand

    # allows all the stdin to flow right passed tell me
    for line in sys.stdin:
        sys.stdout.write(line)



if (__name__ == "__main__"):
    main()

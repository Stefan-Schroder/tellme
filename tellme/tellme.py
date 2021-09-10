#!/home/stefan/.pyenv/shims/python3
#!/usr/bin/python3

import telegram_tellme
import sys
from decouple import config

def GetFishCommand():
    # history_path = config('FISH_HIST_PATH')
    return "hi"

def main():
    # get the last few line from config file
    command = GetFishCommand()

    # allows all the stdin to flow right passed tell me
    for line in sys.stdin:
        sys.stdout.write(line)

    telegram_tellme.send_message(command)


if (__name__ == "__main__"):
    main()

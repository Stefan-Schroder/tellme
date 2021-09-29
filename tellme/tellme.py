#!/home/stefan/.pyenv/shims/python3
#!/usr/bin/python3

import telegram_tellme
import sys
import subprocess
import configparser
from decouple import config
from dotenv import load_dotenv
import os

def GetFishCommand(history_path):
    # I will give my left sock for someone to find a more efficient way to do this
    # - dont load the whole file into memory (history can be huge)
    # - dont use 700 lines to do it
    # 20 is arbritrary, just need to find the last tellme command (sometimes its not the last command used)
    command = subprocess.check_output('tail -n 20 '+history_path+' | grep -E "^- cmd:" | grep -E "[\| ]tellme" | tail -n 1', shell=True)
    return command[6:-1]
    

def main():
    # Getting Root directory of this program
    root_dir = os.path.dirname(sys.executable)[:-5]

    # loading in configs
    load_dotenv(root_dir+"/.env")

    config_file = configparser.ConfigParser()
    config_file.read(root_dir+'/config.ini')

    # get the last few line from config file
    if (config_file['USER']['SHELL']=='FISH'):
        command = GetFishCommand(config_file['USER']['FISH_HIST_PATH'])

    # allows all the stdin to flow right passed tell me
    for line in sys.stdin:
        sys.stdout.write(line)

    telegram_tellme.send_message(command, root_dir)


if (__name__ == "__main__"):
    main()

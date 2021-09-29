#!/usr/bin/python3

from decouple import config
import telebot
import sys
from dotenv import load_dotenv

def send_message(message):
    load_dotenv
    # API_KEY = config('API_KEY')
    API_KEY = os.getenv('API_KEY')
    bot = telebot.TeleBot(API_KEY)

    # USER=config('USER_ID')
    USER = os.getenv('USER_ID')
    bot.send_message(USER, message) 

if __name__=="__main__":
    send_message(sys.argv[1])

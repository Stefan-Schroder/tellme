#!/usr/bin/python3

from decouple import config
import telebot
import sys

def send_message(message):
    API_KEY = config('API_KEY')
    bot = telebot.TeleBot(API_KEY)

    USER=config('USER_ID')
    bot.send_message(USER, message) 

if __name__=="__main__":
    send_message(sys.argv[1])

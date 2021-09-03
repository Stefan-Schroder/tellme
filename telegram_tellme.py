#!/usr/bin/python3

from decouple import config
import telebot
import sys

API_KEY = config('API_KEY')
bot = telebot.TeleBot(API_KEY)

USER=config('USER_ID')
message = sys.argv[1]
bot.send_message(USER, message) 

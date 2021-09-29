#!/usr/bin/python3

from decouple import config
import telebot
import sys
from dotenv import load_dotenv
import os

def send_message(message, root_dir):
    load_dotenv()

    API_KEY = os.getenv('API_KEY')
    bot = telebot.TeleBot(API_KEY)

    USER = os.getenv('USER_ID')
    bot.send_message(USER, message) 

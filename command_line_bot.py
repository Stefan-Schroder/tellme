#!/usr/bin/python3

from decouple import config
import telebot
import sys

API_KEY = config('API_KEY')
bot = telebot.TeleBot(API_KEY)

STEF=config('STEFS_KEY')
message = sys.argv[1]
bot.send_message(STEF, message) 








# @bot.message_handler(commands=['Greet'])
# def greet_poop(message):
#     bot.reply_to(message, "Yo what is the hap")

# @bot.message_handler(commands=['Yeet'])
# def greet_poop(message):
#     bot.send_message(message.chat.id, "Yeet this feetus")
#     print(message.chat.id)

# this is when the bot is checking for the messages
# bot.polling()

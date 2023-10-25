#!/usr/bin/env python3

import sys
from dotenv import load_dotenv
import os

#telegram
import asyncio
import telegram
from telegram.ext import ApplicationBuilder

# using telegram.Bot
async def send(chat, msg, key):
    await telegram.Bot(key).sendMessage(chat_id=chat, text=msg, parse_mode="MarkdownV2")

def send_message(message, root_dir):
    load_dotenv(root_dir+"/.env")

    API_KEY = os.getenv('API_KEY')
    USER = os.getenv('USER_ID')

    msg=message.replace('\\n', '\n')\
            .replace('\\r', '\r')\
            .replace('\\t', '\t')\
            .replace('-','\-')\
            .replace('.','\.')\
            .replace('=','\=')

    asyncio.run(send(USER, msg, API_KEY))

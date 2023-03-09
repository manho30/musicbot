#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description :
@File        : util.py
@IDE         : PyCharm
@Date        : 9/3/2023 18:15
"""

import threading
import os

import telebot
from telebot import types
from mutagen.mp3 import MP3

from utils.search import search
from utils.parse import parse
from utils.treeify import treeify
from utils.download import download
from utils.info import *

TOKEN = '5480116977:AAGE0NAiG_kBG5M6Ljn1LrXAifvu5kkS-9s'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    # create an inline keyboard with the "流行歌曲" button
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text='Try Now!', callback_data='pop_songs 1'))
    bot.send_message(message.chat.id,
                     "Hi! This bot can make Music search from YouTube. Send me a song name, that's all! I will download it for you.",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data.split(' ')[0] == 'pop_songs':
        CURRENT_PAGE = int(call.data.split(' ')[1])

        keyboard = types.InlineKeyboardMarkup()
        have_entry = ''
        try:
            have_entry = call.data.split(' ')[2]
        except IndexError:
            pass

        if CURRENT_PAGE > 1 or have_entry == '-':
            songs = parse(search('流行歌曲', 10, CURRENT_PAGE))

            button = []
            for i, song in enumerate(songs, 1):
                if i % 5 == 1:
                    button = []
                button.append(types.InlineKeyboardButton(text=str((CURRENT_PAGE - 1) * 10 + i), callback_data=f'dl:{song["id"]}'))
                if i % 5 == 0 or i == len(songs):
                    keyboard.add(*button)

            keyboard.add(
                types.InlineKeyboardButton(text='Previous', callback_data=F'pop_songs {CURRENT_PAGE - 1} -'),
                types.InlineKeyboardButton(text='Next', callback_data=F'pop_songs {CURRENT_PAGE + 1}'),
            )

            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=treeify(songs, index=CURRENT_PAGE),
                                  reply_markup=keyboard)

        else:
            searching = bot.send_message(call.message.chat.id, "Search for popular songs...")
            songs = parse(search('流行歌曲', 10, 1))

            button = []
            for i, song in enumerate(songs, 1):
                if i % 5 == 1:
                    button = []
                button.append(types.InlineKeyboardButton(text=str((CURRENT_PAGE - 1) * 10 + i), callback_data=f'dl:{song["id"]}'))
                if i % 5 == 0 or i == len(songs):
                    keyboard.add(*button)

            keyboard.add(types.InlineKeyboardButton(text='Next', callback_data='pop_songs 2'))

            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=searching.message_id,
                                  text=treeify(songs, index=1),
                                  reply_markup=keyboard
                                  )
    elif call.data.split(':')[0] == 'dl':
        song = getInfo(parse(search(call.data.split(':')[1], 1, 1)), call.data.split(':')[1])
        downloading = bot.send_message(call.message.chat.id,
                         f"Downloading songs...\n"
                         f"Artist: {getArtistName(song)}\n"
                         f"Title: {getTitle(song)}"
                         )
        download(call.data.split(':')[1])
        bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=downloading.message_id,
                                text=f"Uploading songs!\n"
                                     f"Artist: {getArtistName(song)}\n"
                                     f"Title: {getTitle(song)}\n"
                                     f"Duration: {getDuration(song)}\n"
                                     f"Size: {(os.path.getsize(f'../songs/{getTitle(song)}.mp3') / (1024 * 1024)):.2f} MB\n"
                                     f"Bitrate: {MP3(f'../songs/{getTitle(song)}.mp3').info.bitrate} Kbps\n"
                                     f"URL: {getURL(song)}"
                                )
        bot.send_chat_action(call.message.chat.id, 'upload_audio')
        print(f'../songs/{getTitle(song)}.mp3')
        bot.send_audio(call.message.chat.id, audio=open(f'../songs/{getTitle(song)}.mp3', 'rb'), timeout=150)

if __name__ == '__main__':
    bot.polling()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : This is fake api using to cheat the hosting platform
@File        : api.py
@IDE         : PyCharm
@Date        : 9/3/2023 21:58
"""

from flask import Flask, request, jsonify

from bot.util import bot

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'

bot.polling()
print('Bot started')
app.run(host='0.0.0.0', port=5000)
# cheeky start the bot

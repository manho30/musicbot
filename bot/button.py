#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@File        : button.py
@IDE         : PyCharm
@Date        : 9/3/2023 19:45
"""


def generateInlineKeyboardMarkup(array):
    inlineKeyboardMarkup = {
        'inline_keyboard': []
    }
    count = 0
    for i in range(2):
        keyboardRow = []
        for j in range(5):
            button = array[i * 5 + j]
            keyboardRow.append(button)
            count += 1
            if count >= len(array):
                break
        inlineKeyboardMarkup['inline_keyboard'].append(keyboardRow)
    print(inlineKeyboardMarkup)
    return inlineKeyboardMarkup
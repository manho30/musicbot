#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@File        : treeify.py
@IDE         : PyCharm
@Date        : 9/3/2023 18:25
"""


from .search import search
from .parse import parse

def treeify(data, index=1)-> str:
    """
    Treeify the music data.

    Args:
        data list: The music data.
        index int: The index of the music data.

    Returns:
        str: The treeified music data.

    Raises:
        ValueError: If the music data is not found.
    """
    tree = f"🎵 I found the following music for you:\n"
    for i, song in enumerate(data, 1):
        if i == len(data):
            tree += f"└ {(index-1) * 10 + i} {song['title']} ({song['duration']})\n"
            tree += f"  └ {song['artist']}\n"
        else:
            tree += f"├ {((index-1) * 10) + i} {song['title']} ({song['duration']})\n"
            tree += f"│ └ {song['artist']}\n"
    return tree



if __name__ == '__main__':
    data = parse(search('yihuik', 10, 2))
    print(treeify(data, index=1))
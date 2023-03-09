#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@File        : edit.py
@IDE         : PyCharm
@Date        : 9/3/2023 16:13
"""

import os

import eyed3
from eyed3.id3.frames import ImageFrame
import requests

from .search import search
from .parse import parse
from .info import getInfo
from .crop import crop

def edit(path: str, vid_id: str) -> None:
    """
    Edits the metadata of a song.

    Args:
        path str: The path of the song.
        vid_id str: The ID of the song.

    Returns:
        None

    Raises:
        ValueError: If the song is not found.
    """
    songs = parse(search(vid_id, 4, 1))
    song = getInfo(songs, vid_id)

    audio = eyed3.load(path)

    thumnail = requests.get(song['thumbnail']).content
    with open(f'../thumnail/{song["id"]}.jpg', 'wb') as f:
        f.write(thumnail)

    crop(f'../thumnail/{song["id"]}.jpg')

    audio.tag.artist = song['artist']
    audio.tag.album = song['album']

    audio.tag.album_artist = song['artist']
    audio.tag.title = song['title']

    audio.tag.images.set(ImageFrame.FRONT_COVER, open(f'../thumnail/{song["id"]}.jpg', 'rb').read(), 'image/jpeg')

    audio.tag.save()

    os.remove(f'../thumnail/{song["id"]}.jpg')

    print(f'Edited {song["title"]}... from {song["artist"]}\r')

if __name__ == '__main__':
    edit('../songs/想見你想見你想見你.mp3', 'Zh7gmg8VjFc')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@File        : download.py
@IDE         : PyCharm
@Date        : 9/3/2023 13:35
"""


import threading

import yt_dlp

from .info import *
from .search import search
from .parse import parse
from .edit import edit

def download(vid_id: str) -> None:
    """
    Downloads a song.

    Args:
        vid_id str: The ID of the song.

    Returns:
        None

    Raises:
        ValueError: If the song is not found.
    """
    print('start download')
    songs = parse(search(vid_id,1, 1))
    print(songs)
    song = getInfo(songs, vid_id)
    def download_single():
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'../songs/{song["title"]}',
            'quiet': True,
            'no_warnings': True,
            'nocheckcertificate': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f'Downloading {song["title"]} -> from {song["artist"]}\r')
            ydl.download([f'https://www.youtube.com/watch?v={song["id"]}'])
            print(f'Downloaded {song["title"]} -> from {song["artist"]}\r')
            edit(f'../songs/{song["title"]}.mp3', vid_id)
    thread = threading.Thread(target=download_single)
    thread.start()
    thread.join()
if __name__ == '__main__':
    download('ACmDS_BtI-A')
    download('m1zY_QdMwO0')
    download('Zh7gmg8VjFc')
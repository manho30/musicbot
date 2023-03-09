#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@File        : info.py
@IDE         : PyCharm
@Date        : 9/3/2023 13:39
"""


from typing import List, Dict, Any

from .search import search
from .parse import parse


def getInfo(songs: List[Dict[str, str]], vid_id: str) -> Dict[str, str]:
    """
    Gets information about a song.

    Args:
        songs List[Dict[str, str]]: The result of a search query.
        vid_id str: The query used to search for the song.

    Returns:
        Dict[str, str]: The information about the song.

    Raises:
        ValueError: If the song is not found.

    Examples:
        >>> getInfo(parse(search('yihuik', 4, 1)), 'ACmDS_BtI-A')
        {'id': 'ACmDS_BtI-A', 'title': '喜欢你 (心动版)', 'artist': 'yihuik苡慧', 'album': '喜欢你 (心动版)', 'album_id': 'MPREb_VotPJnGS8ic', 'duration': '3:36', 'thumbnail': 'https://lh3.googleusercontent.com/trYCjA9akf-8hFHBrhSqX2erUnxSNVfe779e61bs7sZjt52tKtgBb6BAhVTRdcmPP6fkH1wzg7jkxVm7_g=w60-h60-l90-rj', 'url': 'https://www.youtube.com/watch?v=ACmDS_BtI-A'}


    """
    for song in songs:
        if song['id'] == vid_id:
            return song

    raise ValueError('Song not found.')


def getArtistName(songs: Dict[str, Any]) -> str:
    """
    Gets the artist of a song.

    Args:
        songs List[Dict[str, str]]: The result of a search query.

    Returns:
        str: The artist of the song.

    Raises:
        ValueError: If the artist is not found.

    Examples:
        >>> getArtistName(getInfo(parse(search('yihuik', 4, 1)), 'ACmDS_BtI-A'))
        'yihuik苡慧'
    """

    artist = songs.get('artist')
    if artist:
        return artist
    else:
        raise ValueError('Artist not found.')


def getAlbumName(songs: Dict[str, Any]) -> str:
    """
    Gets the album of a song.

    Args:
        songs List[Dict[str, str]]: The result of a search query.

    Returns:
        str: The album of the song.

    Raises:
        ValueError: If the album is not found.

    Examples:
        >>> getAlbumName(getInfo(parse(search('yihuik', 4, 1)), 'ACmDS_BtI-A'))
        '喜欢你 (心动版)'
    """

    album = songs.get('album')
    if album:
        return album
    else:
        raise ValueError('Album not found.')


def getAlbumID(songs: Dict[str, Any]) -> str:
    """
    Gets the album ID of a song.

    Args:
        songs List[Dict[str, str]]: The result of a search query.

    Returns:
        str: The album ID of the song.

    Raises:
        ValueError: If the album ID is not found.

    Examples:
        >>> getAlbumID(getInfo(parse(search('yihuik', 4, 1)), 'ACmDS_BtI-A'))
        'MPREb_VotPJnGS8ic'
    """

    album_id = songs.get('album_id')
    if album_id:
        return album_id
    else:
        raise ValueError('Album ID not found.')


def getDuration(songs: Dict[str, Any]) -> str:
    """
    Gets the duration of a song.

    Args:
        songs List[Dict[str, str]]: The result of a search query.

    Returns:
        str: The duration of the song.

    Raises:
        ValueError: If the duration is not found.

    Examples:
        >>> getDuration(getInfo(parse(search('yihuik', 4, 1)), 'ACmDS_BtI-A'))
        '3:36'
    """

    duration = songs.get('duration')
    if duration:
        return duration
    else:
        raise ValueError('Duration not found.')


def getThumbnail(songs: Dict[str, Any]) -> str:
    """
    Gets the thumbnail of a song.

    Args:
        songs List[Dict[str, str]]: The result of a search query.

    Returns:
        str: The thumbnail of the song.

    Raises:
        ValueError: If the thumbnail is not found.

    Examples:
        >>> getThumbnail(getInfo(parse(search('yihuik', 4, 1)), 'ACmDS_BtI-A'))
        'https://lh3.googleusercontent.com/trYCjA9akf-8hFHBrhSqX2erUnxSNVfe779e61bs7sZjt52tKtgBb6BAhVTRdcmPP6fkH1wzg7jkxVm7_g=w60-h60-l90-rj'
    """

    thumbnail = songs.get('thumbnail')
    if thumbnail:
        return thumbnail
    else:
        raise ValueError('Thumbnail not found.')

def getURL(songs: Dict[str, Any]) -> str:
    """
    Gets the URL of a song.

    Args:
        songs List[Dict[str, str]]: The result of a search query.

    Returns:
        str: The URL of the song.

    Raises:
        ValueError: If the URL is not found.

    Examples:
        >>> getURL(getInfo(parse(search('yihuik', 4, 1)), 'ACmDS_BtI-A'))
        'https://www.youtube.com/watch?v=ACmDS_BtI-A'
    """

    url = songs.get('url')
    if url:
        return url
    else:
        raise ValueError('URL not found.')


def getTitle(songs: Dict[str, Any]) -> str:
    """
    Gets the title of a song.

    Args:
        songs List[Dict[str, str]]: The result of a search query.

    Returns:
        str: The title of the song.

    Raises:
        ValueError: If the title is not found.

    Examples:
        >>> getTitle(getInfo(parse(search('yihuik', 4, 1)), 'ACmDS_BtI-A'))
        '喜欢你 (心动版)'
    """

    title = songs.get('title')
    if title:
        return title
    else:
        raise ValueError('Title not found.')
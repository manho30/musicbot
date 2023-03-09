#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@File        : parse.py
@IDE         : PyCharm
@Date        : 9/3/2023 13:06
"""

from typing import List, Dict

from .search import search


def parse(songs: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Parses the result of a search query.

    Args:
        result List[Dict[str, str]]: The result of a search query.

    Returns:
        dict: A dictionary containing information about the search result.

    Examples:
        >>> parse(search('yihuik', 5, 1))
        [{'id': 'ACmDS_BtI-A', 'title': '喜欢你 (心动版)', 'artist': 'yihuik苡慧', 'album': '喜欢你 (心动版)', 'album_id': 'MPREb_VotPJnGS8ic', 'duration': '3:36', 'thumbnail': 'https://lh3.googleusercontent.com/trYCjA9akf-8hFHBrhSqX2erUnxSNVfe779e61bs7sZjt52tKtgBb6BAhVTRdcmPP6fkH1wzg7jkxVm7_g=w60-h60-l90-rj', 'url': 'https://www.youtube.com/watch?v=ACmDS_BtI-A'}, {'id': 'Gc4kpwP_mVU', 'title': '致你', 'artist': 'yihuik苡慧', 'album': '致你', 'album_id': 'MPREb_TS747FDG9Ih', 'duration': '4:32', 'thumbnail': 'https://lh3.googleusercontent.com/SS9oO_A6OCZVPqr2CZzOM2NMqfEzPjMhQBff7ZymDil7B61_H_NzxHka5cBWVkaCUbBZ7fJ0PTskmjK3=w60-h60-l90-rj', 'url': 'https://www.youtube.com/watch?v=Gc4kpwP_mVU'}, {'id': 'C02L1SqAfWs', 'title': '就是爱你', 'artist': 'yihuik苡慧', 'album': '就是爱你', 'album_id': 'MPREb_53IsnbVXAUl', 'duration': '3:55', 'thumbnail': 'https://lh3.googleusercontent.com/ap8VyyIwOJHaLHB_UZSmht80eCS745D5hMy5X3WWS2Z5Bq8EFxKURO2XVavJ766W56IJS0cA2-nqIBsV-Q=w60-h60-l90-rj', 'url': 'https://www.youtube.com/watch?v=C02L1SqAfWs'}, {'id': 'xLrQeEChJIc', 'title': 'Galaxy and Stars', 'artist': 'Yihuik', 'album': 'Galaxy and Stars', 'album_id': 'MPREb_Fl7SwhUmyqb', 'duration': '3:15', 'thumbnail': 'https://lh3.googleusercontent.com/IEA1ET93j-VC3yl8YRLObe4i9F_4r0qtPcxc4_r5N3x1eaet1cZTEuGZerdk_SmKJtX_N9ODx2AyB7i8MQ=w60-h60-l90-rj', 'url': 'https://www.youtube.com/watch?v=xLrQeEChJIc'}, {'id': 'PJgbQ7cKfbg', 'title': 'Wheat Waves', 'artist': 'Yihuik', 'album': 'Wheat Waves', 'album_id': 'MPREb_S4UuXezovnV', 'duration': '3:06', 'thumbnail': 'https://lh3.googleusercontent.com/pItPeNw1xZVb8mxGv9x1Ixi0Qf_qgRkHRG8NFG3CS11YY9bYQRdPmElByR92UhEG2lizu6Hx-ulVhXsm=w60-h60-l90-rj', 'url': 'https://www.youtube.com/watch?v=PJgbQ7cKfbg'}]

    """

    result = []

    for song in songs:
        result.append({
            'id': song['videoId'],
            'title': song['title'],
            'artist': song['artists'][0]['name'],
            'album': song['album']['name'],
            'album_id': song['album']['id'],
            'duration': song['duration'],
            'thumbnail': f'https://img.youtube.com/vi/{song["videoId"]}/maxresdefault.jpg',
            'url': f'https://www.youtube.com/watch?v={song["videoId"]}'
        })

    return result

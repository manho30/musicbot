#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@File        : search.py
@IDE         : PyCharm
@Date        : 9/3/2023 12:20
"""
from typing import List, Dict
from pprint import pprint

from ytmusicapi import YTMusic


def search(name: str, total: int = 10, offset: int = 1) -> List[Dict]:
    """
    Search for music on YouTube Music using the ytmusicapi library.

    Args:
        name (str): The name of the song or artist to search for. Can be a partial name or ID.
        total (int): The total number of results to return. Defaults to 10.
        offset (int): The index of the first result to return. Defaults to 1.

    Returns:
        list: A list of dictionaries containing information about the search results.

    Examples:
        >>> search('yihuik', 5, 1)
        [{'category': 'Songs', 'resultType': 'song', 'title': '喜欢你 (心动版)', 'album': {'name': '喜欢你 (心动版)', 'id': 'MPREb_VotPJnGS8ic'}, 'feedbackTokens': {'add': None, 'remove': None}, 'videoId': 'ACmDS_BtI-A', 'videoType': 'MUSIC_VIDEO_TYPE_ATV', 'duration': '3:36', 'year': None, 'artists': [{'name': 'yihuik苡慧', 'id': 'UCgF4picTs24cmn8Kw10uI5g'}], 'duration_seconds': 216, 'isExplicit': False, 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/trYCjA9akf-8hFHBrhSqX2erUnxSNVfe779e61bs7sZjt52tKtgBb6BAhVTRdcmPP6fkH1wzg7jkxVm7_g=w60-h60-l90-rj', 'width': 60, 'height': 60}, {'url': 'https://lh3.googleusercontent.com/trYCjA9akf-8hFHBrhSqX2erUnxSNVfe779e61bs7sZjt52tKtgBb6BAhVTRdcmPP6fkH1wzg7jkxVm7_g=w120-h120-l90-rj', 'width': 120, 'height': 120}]}, {'category': 'Songs', 'resultType': 'song', 'title': '致你', 'album': {'name': '致你', 'id': 'MPREb_TS747FDG9Ih'}, 'feedbackTokens': {'add': None, 'remove': None}, 'videoId': 'Gc4kpwP_mVU', 'videoType': 'MUSIC_VIDEO_TYPE_ATV', 'duration': '4:32', 'year': None, 'artists': [{'name': 'yihuik苡慧', 'id': 'UCgF4picTs24cmn8Kw10uI5g'}], 'duration_seconds': 272, 'isExplicit': False, 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/SS9oO_A6OCZVPqr2CZzOM2NMqfEzPjMhQBff7ZymDil7B61_H_NzxHka5cBWVkaCUbBZ7fJ0PTskmjK3=w60-h60-l90-rj', 'width': 60, 'height': 60}, {'url': 'https://lh3.googleusercontent.com/SS9oO_A6OCZVPqr2CZzOM2NMqfEzPjMhQBff7ZymDil7B61_H_NzxHka5cBWVkaCUbBZ7fJ0PTskmjK3=w120-h120-l90-rj', 'width': 120, 'height': 120}]}, {'category': 'Songs', 'resultType': 'song', 'title': '就是爱你', 'album': {'name': '就是爱你', 'id': 'MPREb_53IsnbVXAUl'}, 'feedbackTokens': {'add': None, 'remove': None}, 'videoId': 'C02L1SqAfWs', 'videoType': 'MUSIC_VIDEO_TYPE_ATV', 'duration': '3:55', 'year': None, 'artists': [{'name': 'yihuik苡慧', 'id': 'UCgF4picTs24cmn8Kw10uI5g'}], 'duration_seconds': 235, 'isExplicit': False, 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/ap8VyyIwOJHaLHB_UZSmht80eCS745D5hMy5X3WWS2Z5Bq8EFxKURO2XVavJ766W56IJS0cA2-nqIBsV-Q=w60-h60-l90-rj', 'width': 60, 'height': 60}, {'url': 'https://lh3.googleusercontent.com/ap8VyyIwOJHaLHB_UZSmht80eCS745D5hMy5X3WWS2Z5Bq8EFxKURO2XVavJ766W56IJS0cA2-nqIBsV-Q=w120-h120-l90-rj', 'width': 120, 'height': 120}]}, {'category': 'Songs', 'resultType': 'song', 'title': 'Wheat Waves', 'album': {'name': 'Wheat Waves', 'id': 'MPREb_S4UuXezovnV'}, 'feedbackTokens': {'add': None, 'remove': None}, 'videoId': 'PJgbQ7cKfbg', 'videoType': 'MUSIC_VIDEO_TYPE_ATV', 'duration': '3:06', 'year': None, 'artists': [{'name': 'Yihuik', 'id': 'UCgF4picTs24cmn8Kw10uI5g'}], 'duration_seconds': 186, 'isExplicit': False, 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/pItPeNw1xZVb8mxGv9x1Ixi0Qf_qgRkHRG8NFG3CS11YY9bYQRdPmElByR92UhEG2lizu6Hx-ulVhXsm=w60-h60-l90-rj', 'width': 60, 'height': 60}, {'url': 'https://lh3.googleusercontent.com/pItPeNw1xZVb8mxGv9x1Ixi0Qf_qgRkHRG8NFG3CS11YY9bYQRdPmElByR92UhEG2lizu6Hx-ulVhXsm=w120-h120-l90-rj', 'width': 120, 'height': 120}]}, {'category': 'Songs', 'resultType': 'song', 'title': 'Galaxy and Stars', 'album': {'name': 'Galaxy and Stars', 'id': 'MPREb_Fl7SwhUmyqb'}, 'feedbackTokens': {'add': None, 'remove': None}, 'videoId': 'xLrQeEChJIc', 'videoType': 'MUSIC_VIDEO_TYPE_ATV', 'duration': '3:15', 'year': None, 'artists': [{'name': 'Yihuik', 'id': 'UCgF4picTs24cmn8Kw10uI5g'}], 'duration_seconds': 195, 'isExplicit': False, 'thumbnails': [{'url': 'https://lh3.googleusercontent.com/IEA1ET93j-VC3yl8YRLObe4i9F_4r0qtPcxc4_r5N3x1eaet1cZTEuGZerdk_SmKJtX_N9ODx2AyB7i8MQ=w60-h60-l90-rj', 'width': 60, 'height': 60}, {'url': 'https://lh3.googleusercontent.com/IEA1ET93j-VC3yl8YRLObe4i9F_4r0qtPcxc4_r5N3x1eaet1cZTEuGZerdk_SmKJtX_N9ODx2AyB7i8MQ=w120-h120-l90-rj', 'width': 120, 'height': 120}]}]

    """
    ytmusic = YTMusic()

    start_index = (offset - 1) * total
    limit = total if offset == 1 else start_index + total
    search_results = ytmusic.search(name, filter='songs', limit=limit)
    search_results = search_results[start_index:]
    return search_results[:total]

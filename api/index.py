#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description :
@File        : index.py
@IDE         : PyCharm
@Date        : 10/3/2023 14:27
"""

import os
import time
from typing import Tuple

import requests
from flask import Flask, jsonify, Response, request, send_file
from flask_cors import CORS

from utils.search import search
from utils.parse import parse
from utils.info import getInfo
from utils.crop import crop
from utils.download import download

app = Flask(__name__)
CORS(app)

@app.errorhandler(404)
def not_found_error(error) -> tuple[Response, int]:
    return jsonify({
        'ok': False,
        'status': 404,
        'result': 'Not Found'
    }), 404

@app.route('/', methods=['GET'])
def _index() -> tuple[Response, int]:
    return jsonify({
        'ok': True,
        'status': 200,
        'result': 'Welcome to the API'
    }), 200


@app.route('/__internal__/clear', methods=['GET'])
def _clear() -> tuple[Response, int]:
    # THIS IS FOR INTERNAL USE ONLY, TO CLEAR THE THUMBNAIL CACHE
    for file in os.listdir('../thumnail'):
        os.remove(f'../thumnail/{file}')

    for song in os.listdir('../songs'):
        os.remove(f'../songs/{song}')

    return jsonify({
        'ok': True,
        'status': 200,
        'result': 'Cleared Cache'
    }), 200

@app.route('/api/search', methods=['GET'])
def _search() -> tuple[Response, int]:
    """
    Searches for a song.

    Args:
        vid_id str: The ID of the song.

    Returns:
        Response: The response.
    """
    start = time.time()
    QUERY = request.args.get('query') or None
    TOTAL = request.args.get('limit') or 10
    PAGE = request.args.get('page') or 1

    if TOTAL > 25:
        return jsonify({
            'ok': False,
            'status': 429,
            'result': 'Too Many Requests'
        }), 429
    if QUERY is None:
        return jsonify({
            'ok': False,
            'status': 400,
            'result': 'Bad Request'
        }), 400

    try :
        result = parse(search(QUERY, TOTAL, PAGE))
    except Exception as e:
        return jsonify({
            'ok': False,
            'status': 400,
            'result': 'Bad Request'
        }), 400
    end = time.time()
    return jsonify({
        'ok': True,
        'status': 200,
        'result': result,
        'time': float(f'{end - start:2f}')
    }), 200

@app.route('/api/info', methods=['GET'])
def info() -> tuple[Response, int]:
    """
    Gets the info of a song.

    Args:
        vid_id str: The ID of the song.

    Returns:
        Response: The response.
    """
    start = time.time()
    VID_ID = request.args.get('id')
    if VID_ID is None:
        return jsonify({
            'ok': False,
            'status': 400,
            'result': 'Bad Request'
        }), 400
    try:
        result = getInfo(parse(search(VID_ID, 1, 1)), VID_ID)
    except Exception as e:
        return jsonify({
            'ok': False,
            'status': 400,
            'result': 'Bad Request'
        }), 400
    end = time.time()
    return jsonify({
        'ok': True,
        'status': 200,
        'result': result,
        'time': float(f'{end - start:2f}')
    }), 200


@app.route('/api/thumnail', methods=['GET'])
def _thumnail() -> tuple[Response, int] | Response:
    start = time.time()
    """
    Gets the thumnail of a song.

    Args:
        vid_id str: The ID of the song.

    Returns:
        Response: The response.
    """
    VID_ID = request.args.get('id')
    if VID_ID is None:
        return jsonify({
            'ok': False,
            'status': 400,
            'result': 'Bad Request'
        }), 400
    try:
        song = getInfo(parse(search(VID_ID, 1, 1)), VID_ID)
    except Exception as e:
        return jsonify({
            'ok': False,
            'status': 400,
            'result': 'Bad Request'
        }), 400
    thumnail = requests.get(song['thumbnail']).content
    with open(f'../thumnail/{song["id"]}.jpg', 'wb') as f:
        f.write(thumnail)
    crop(f'../thumnail/{song["id"]}.jpg')
    end = time.time()
    print(float(f'{end - start:2f}'))
    res = send_file(f'../thumnail/{song["id"]}.jpg', mimetype='image/jpg')
    return res

@app.route('/api/download', methods=['GET'])
def _download() -> tuple[Response, int] | Response:
    """
    Downloads a song.

    Args:
        vid_id str: The ID of the song.

    Returns:
        Response: The response.
    """
    start = time.time()
    VID_ID = request.args.get('id')
    if VID_ID is None:
        return jsonify({
            'ok': False,
            'status': 400,
            'result': 'Bad Request'
        }), 400
    try:
        song = getInfo(parse(search(VID_ID, 1, 1)), VID_ID)

        # check if the song is already downloaded
        if not os.path.exists(f'../songs/{song["title"]}.mp3'):
            download(song)
    except Exception as e:
        return jsonify({
            'ok': False,
            'status': 400,
            'result': 'Bad Request'
        }), 400
    end = time.time()
    return send_file(f'../songs/{song["title"]}.mp3', mimetype='audio/mpeg')


if __name__ == '__main__':
    app.run()

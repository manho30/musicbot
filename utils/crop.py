#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@File        : crop.py
@IDE         : PyCharm
@Date        : 9/3/2023 17:01
"""

from PIL import Image, ImageFilter

def crop(image_path: str, img_return=False) -> None:
    """
    Crops an image to a square.

    Args:
        image_path str: The path of the image.
        img_return bool: Whether to return the image.
    """
    with Image.open(image_path) as img:
        width, height = img.size
        if width == height:
            return img
        else:
            if width > height:
                left = (width - height) // 2
                right = width - left
                top = 0
                bottom = height
            else:
                top = (height - width) // 2
                bottom = height - top
                left = 0
                right = width
            img.crop((left, top, right, bottom)).save(image_path)
# encoding: utf-8

"""
2018-7-16 23:36, img_property.py created by wq.
"""

import cv2

img = cv2.imread("car.jpg")
# 返回行、列、通道，例如，(768, 1024, 3)，灰白图像只返回行列
print(img.shape)

# 返回像素数，例如，2359296。
print(img.size)

# 返回图像的数据类型，例如，uint8。
print(img.dtype)

# encoding: utf-8

"""
2018-7-18 20:49, img_add.py created by wq.
"""

import cv2
import numpy as np

x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x, y))

print(x + y)

# 结果
# [[255]]
# [4]

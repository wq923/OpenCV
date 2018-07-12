# encoding: utf-8

"""
2018-7-12 21:39, draw_line.py created by wq.
"""

import numpy as np
import cv2


def show_drawable(name, img):
    cv2.namedWindow(name)
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyWindow(name)


# 创建一个黑块
# 返回来一个给定形状和类型的用0填充的数组（创建零矩阵，每个0由8位组成，即一个字节）
# 此处返回一个512行、511列的
img = np.zeros((512, 511, 3), np.uint8)

# 画一条直线， 起始点、BGR、粗细
cv2.line(img, (0, 0), (511, 511), (0, 0, 255), 2)

show_drawable("line", img)

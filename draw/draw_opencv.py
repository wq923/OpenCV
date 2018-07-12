# encoding: utf-8

"""
2018-7-12 22:01, draw_rect.py created by wq.
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
cv2.rectangle(img, (0, 0), (512, 511), (255, 255, 255), -1)

# 画椭圆，中心点坐标、长短轴长度、旋转角度、椭圆沿逆时针旋转角度，椭圆弧沿顺时针角度、实心空心
cv2.ellipse(img, (250, 100), (50, 50), 135, 0, 270, (0, 0, 255), 30)
cv2.ellipse(img, (175, 215), (50, 50), 0, 0, 270, (0, 255, 0), 30)
cv2.ellipse(img, (325, 215), (50, 50), -45, 0, 270, (255, 0, 0), 30)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV", (110, 345), font, 2.3, 0, 5)

show_drawable("OpenCV", img)

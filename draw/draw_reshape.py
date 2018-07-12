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

# 画一条直线， 起始点、BGR、粗细
cv2.line(img, (0, 0), (511, 511), (0, 0, 255), 3)

# 画矩形， 起始点、BGR、粗细
cv2.rectangle(img, (384, 5), (505, 128), (0, 255, 0), 6)

# 画圆形，圆心坐标、半径
cv2.circle(img, (447, 63), 48, (255, 0, 0,), 4)

# 画椭圆，中心点坐标、长短轴长度、旋转角度、椭圆沿逆时针旋转角度，椭圆弧沿顺时针角度、实心空心
cv2.ellipse(img, (256, 256), (100, 80), 0, 0, 90, (0, 255, 0), -1)

# 画多边形，4个顶点的多边形
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img,  np.array([pts]), True, 255, 4)


# show_drawable("line", img)
# show_drawable("rectangle", img)
# show_drawable("circle", img)
# show_drawable("ellipse", img)

show_drawable("reshape", img)

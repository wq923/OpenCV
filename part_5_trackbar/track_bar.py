# encoding: utf-8

"""
2018-7-16 20:56, track_bar.py created by wq.
"""

# 把滑动条绑定到 OpenCV窗口。通过调节滑动条，调节画板颜色。
import cv2
import numpy as np


def nothing(x):
    pass


# 创建一副黑色图像
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow("canvas")

# 创建四个滑动条，参数分别是：名称、所属窗口，默认值、最大值、滑动过程同步回调函数
cv2.createTrackbar('R', "canvas", 0, 255, nothing)
cv2.createTrackbar('G', "canvas", 0, 255, nothing)
cv2.createTrackbar('B', "canvas", 0, 255, nothing)

switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch, "canvas", 0, 1, nothing)

while 1:
    cv2.imshow("canvas", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    r = cv2.getTrackbarPos("R", 'canvas')
    g = cv2.getTrackbarPos("G", 'canvas')
    b = cv2.getTrackbarPos("B", 'canvas')
    s = cv2.getTrackbarPos(switch, 'canvas')

    # 禁止 各个滑动条的功能
    if s == 0:
        img[:] = 0
    # 使能各个滑动条的功能，将 img 的所有像素改成 BGR
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()

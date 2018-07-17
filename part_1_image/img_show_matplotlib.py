# encoding: utf-8

"""
2018-7-11 20:39, img_show_matplotlib.py created by wq.
"""

# matplotlib 是 Python 的一个绘图库，用 matplotlib 显示图像

import cv2
from matplotlib import pyplot as plt

# OpenCV 加载彩色图像为 BGR 模式，matplotlib 加载彩色图像为 RGB 模式
img = cv2.imread("car.jpg", cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap = 'gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])

plt.show()

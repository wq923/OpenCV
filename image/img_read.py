# encoding: utf-8

"""
2018-7-10 22:53, img_read.py created by wq.
"""

import cv2

# imread:读取图像
# param1：文件路径,当路径错误，打印 None
# param2：读取方式，例如：
#   cv2.IMREAD_COLOR,表示读取彩色图像，透明度被忽略。
#   cv2.IMREAD_GRAYSCALE,表示以灰度模式读取图像
img = cv2.imread("car.jpg", 0)
print(img)

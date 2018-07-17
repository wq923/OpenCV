# encoding: utf-8

"""
2018-7-16 23:25, img_px.py created by wq.
"""

# 获取并修改像素值

import cv2

img = cv2.imread("car.jpg")

# 根据行和列获取像素值，对于彩色图像，返回（R\G\B）
px = img[100, 100]
print(px)
blue = img[100, 100, 0]
print(blue)

# 修改像素的值
img[100, 100] = [255, 255, 255]
print(img[100, 100])


# 逐个修改每个像素的值会很慢，尽量使用 Numpy 矩阵运算
print(img.item(10, 10, 2))
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))

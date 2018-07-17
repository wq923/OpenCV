# encoding: utf-8

"""
2018-7-17 20:49, img_make_border.py created by wq.
"""

import cv2
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]

img = cv2.imread("car.jpg")

# 原始图像、上下左右对应的像素数，添加边界的类型（拉最外面一层像素、拉镜像像素等）
replicate = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REFLECT)
reflect_101 = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT)


# 2行 3列的图表
plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('BORDER_REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('BORDER_REFLECT')
plt.subplot(234), plt.imshow(reflect_101, 'gray'), plt.title('BORDER_REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('BORDER_WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('BORDER_CONSTANT')

plt.show()

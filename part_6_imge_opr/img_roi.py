# encoding: utf-8

"""
2018-7-16 23:43, img_roi.py created by wq.
"""

import cv2

img = cv2.imread("car.jpg")
print(img.shape)

# 注意，OpenCV 里的坐标系，先行后列，即img[y, x]
car = img[500:600, 400:500]
img[0:100, 0:100] = car

cv2.imwrite("car_copy.jpg", img)

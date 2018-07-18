# encoding: utf-8

"""
2018-7-18 20:49, img_add.py created by wq.
"""

import cv2

# 注意 523*526 ，两张图像需要有相同长宽的像素数
img1 = cv2.imread("img2.png")
img2 = cv2.imread("OpenCV.png")

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow("weighted", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


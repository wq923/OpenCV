# encoding: utf-8

"""
2018-7-11 0:04, img_show_size.py created by wq.
"""

import cv2

# 先创建一个窗口，之后再加载图像，可以决定窗口是否可以调整大小。
# 如果图像太大或添加轨迹条时，调整大小很有用。
cv2.namedWindow("Car", cv2.WINDOW_NORMAL)
img = cv2.imread("car.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Car", img)

cv2.waitKey(8000)
cv2.destroyAllWindows()

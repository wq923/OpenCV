# encoding: utf-8

"""
2018-7-11 0:08, img_write.py created by wq.
"""

import cv2

img = cv2.imread("car.jpg", cv2.IMREAD_GRAYSCALE)

# 将 img 保存到名为 car_write_copy.jpg 的文件。
# param1：将要生成的文件名称
# param2：将要保存的图像数据
cv2.imwrite("car_write_copy.jpg", img)

# 读取新生成的文件，并显示出来
img_copy = cv2.imread("car_write_copy.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("car_write_copy", img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
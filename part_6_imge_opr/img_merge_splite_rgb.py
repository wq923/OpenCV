# encoding: utf-8

"""
2018-7-17 20:27, img_merge_splite_rgb.py created by wq.
"""

# 拆分和合并图像通道

import cv2

# img = cv2.imread("car.jpg")
#
# cv2.split 拆分通道比较耗时，尽量用 Numpy
# b, g, r = cv2.split(img)
# img = cv2.merge([b, g, r])
#
# cv2.imshow("img", img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


img = cv2.imread('car.jpg')
# 让所有像素的红色通道都为 0 ，不必先拆分再赋值
img[:, :, 2] = 0

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

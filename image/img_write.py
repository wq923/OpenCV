# encoding: utf-8

"""
2018-7-11 0:08, img_write.py created by wq.
"""

import cv2

img = cv2.imread("car.jpg", cv2.IMREAD_GRAYSCALE)

img_copy = cv2.imwrite("car_write_copy.jpg", img)

cv2.imshow("car_write_copy", img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
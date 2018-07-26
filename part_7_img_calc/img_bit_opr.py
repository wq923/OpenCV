# encoding: utf-8

"""
2018-7-26 23:20, img_bit_opr.py created by wq.
"""

import cv2

# 加载图像
img1 = cv2.imread("img2.png")
img2 = cv2.imread("OpenCV.png")

# 想要将logo放到左上角，所以，创建一个ROI
rows, cols, chnanels = img1.shape
roi = img1[0:rows, 0:cols]

# 创建一个mask logo 并创建它的反转mask
img22gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow("灰度", img22gray)

ret, mask = cv2.threshold(img22gray, 175, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask)

cv2.imshow("img1_bg", img1_bg)

img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
cv2.imshow("img2_fg", img2_fg)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow("res", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# encoding: utf-8

"""
2018-7-11 0:39, img_demo.py created by wq.
"""

import cv2

# 读取、显示
img = cv2.imread("car_write_copy.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Easy Test", img)

# 等待按键按下，并判断是否为 s 键或者是 ESC 键
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("demo_save.jpg", img)
    cv2.destroyAllWindows()
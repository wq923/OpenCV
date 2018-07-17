# encoding: utf-8

"""
2018-7-10 23:43, img_show.py created by wq.
"""

import cv2

# img = cv2.imread("car.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("car.jpg", cv2.IMREAD_COLOR)

# 在窗口中显示一张图片
# param1: 窗口标题
# param2: 要显示的图片
cv2.imshow("Car", img)

# 键盘绑定函数，入参单位为毫秒，入参为0表示无限等待用户键盘事件
# 当等待事件内有任何按键按下，该函数将返回按键的 ASCII 码值，如果没有按键按下，
# 程序将继续运行，最后到达延时时间后，返回-1。
cv2.waitKey(8000)

# 删除任何建立的窗口，删除特定窗口可以调用 cv2.destroyWindows("Car")
cv2.destroyAllWindows()

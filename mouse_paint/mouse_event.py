# encoding: utf-8

"""
2018-7-14 14:13, mouse_event.py created by wq.
"""

import cv2
import numpy as np


# 该文件实现两个功能：
# 1、打印出所有的鼠标事件
# 2、在窗口中，鼠标双击的位置画一个圆

def print_all_mouse_events():
    events = [i for i in dir(cv2) if 'EVENT' in i]
    print(events)


# 画图监听，监听鼠标事件（包括鼠标事件和事件发生位置）
def draw_listener(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 80, (0, 0, 255), -1)


print_all_mouse_events()
img = np.zeros((512, 512, 3), np.int8)
cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_listener)   # 为鼠标事件设置监听回调函数

while 1:
    cv2.imshow("image", img)

    if cv2.waitKey(20) & 0xff == 27:  # 等待按键按下，返回按键的 ASCII 码
        break

cv2.destroyAllWindows()

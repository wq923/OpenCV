# encoding: utf-8

"""
2018-7-14 14:13, mouse_event.py created by wq.
"""

import cv2
import numpy as np

# 该文件实现功能：
# 根据我们选择的模式，选择拖动鼠标时画圆还是画矩形


drawing = False  # 当鼠标按下时，变为True
mode = True  # 如果 mode 为 True ，则绘制矩形；按下 ‘m’ 变成绘制曲线

ix, iy = -1, -1


# 画图监听，监听鼠标事件（包括鼠标事件和事件发生位置）
def draw_listener(event, x, y, flags, param):
    global ix, iy, drawing, mode

    # 当按下左键，是返回起始位置坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    # 当左键按下，并移动是绘制图形，flags 表示是否按下
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if (drawing == True):
            if (mode == True):
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
            else:
                cv2.circle(img, (ix, iy), 3, (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


def draw_listener2(event, x, y, flags, param):
    global ix, iy, drawing, mode
    # cv2.line(img, (x, -600), (x, 600), (0, 0, 255), 2)
    # cv2.line(img, (-600, y), (600, y), (0, 0, 255), 2)


    # 当按下左键，是返回起始位置坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        if (mode == True):
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        else:
            cv2.circle(img, (ix, iy), 3, (0, 0, 255), -1)


def print_all_mouse_events():
    events = [i for i in dir(cv2) if 'EVENT' in i]
    print(events)


print_all_mouse_events()
img = np.zeros((512, 512, 3), np.int8)
cv2.namedWindow("part_1_image")
cv2.setMouseCallback("part_1_image", draw_listener2)  # 为鼠标事件设置监听回调函数

while 1:
    cv2.imshow("part_1_image", img)

    k = cv2.waitKey(20) & 0xff
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()

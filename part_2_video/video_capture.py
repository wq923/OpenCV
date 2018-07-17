# encoding: utf-8

"""
2018-7-11 20:56, video_capture.py created by wq.
"""

import cv2

# 捕获视频 VideoCapture
# param : 索引号 或者 视频文件
capture = cv2.VideoCapture(0)

# 循环：捕获-处理-展示
while(True):
    # capture frame-by-frame，捕获一帧帧数据
    ret, frame = capture.read()
    capture.set(3, 320)
    capture.set(4, 240)

    # our operations on the frame come here，处理每一帧数据，彩色转灰度
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display the resulting frame，展示每一帧数据
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()


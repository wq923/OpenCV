# encoding: utf-8

"""
2018-7-11 22:06, video_save.py created by wq.
"""

import cv2

# 保存视频
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        # cv2.flip 图像翻转 进行 数据增强
        # 0表示将一帧数据垂直翻转，1表示将一帧数据水平翻转，-1表示水平垂直翻转
        frame = cv2.flip(frame, 1)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()


## 用滑动条做调色板
常用 API

    cv2.createTrackbar
    cv2.getTrackbarPos

    switch = '0:OFF\n1:ON'
    # 创建进度条，包括名称、默认值、最大值和回调函数
    cv2.createTrackbar('R', "canvas", 0, 255, nothing)
    cv2.createTrackbar('G', "canvas", 0, 255, nothing)
    cv2.createTrackbar('B', "canvas", 0, 255, nothing)
    cv2.createTrackbar(switch, "canvas", 0, 1, nothing)
    
    # 获取当前进度条滑动到的位置，设置 BGR
    r = cv2.getTrackbarPos("R", 'canvas')
    g = cv2.getTrackbarPos("G", 'canvas')
    b = cv2.getTrackbarPos("B", 'canvas')
    s = cv2.getTrackbarPos(switch, 'canvas')

结果        
![Alt Text](https://github.com/wq923/OpenCV/blob/master/trackbar/trackbar.png)    

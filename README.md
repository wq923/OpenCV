# OpenCV
OpenCV Practice.

# 一、简述
## 1.1、为何使用 Python

（1）简单、易入门    
（2）第三方库强大，例如 Numpy、matplotlib    
（3）作为胶水语言，在Linux下组成功能负责的工作流    

## 1.2、为何使用 Python-OpenCV
（1）Python 很强大，有自己的图像处理库 PIL    
（2）OpenCV 相比更加强大，且提供了完善的 Python 接口，提供超过2500个算法和函数，超级方便。    


# 二、实践
## 2.1 图片
常用 API 
    
    cv2.imread()
    cv2.imshow()
    cv2.imwrite()

## 2.2 视频

常用 API 
    
    cv2.VideoCapture(0)
    cv2.VideoWriter()

    //设置 3 号、4 号属性（分别代表宽度和高度，总共0-18个属性）
    capture.set(3, 320)
    capture.set(4, 240)     

保存录制的视频
    
    保存图片用 cv2.imgwrite(),保存视频稍复杂，需要先创建 VideoWriter 对象，然后确定输出视频文件名称，最后指定 FOURCC 编码，播放频率和帧大小，
    是否彩色等
    
## 2.3 画图
常用 API

    cv2.line()
    cv2.circle()
    cv2.rectangle()
    cv2.ellipse()
    cv2.putText()

    
## 2.4 鼠标当画笔

学习使用 OpenCV 处理鼠标事件

常用 API

    cv2.setMouseCallback("image", draw_listener2)
    
第一个参数为监听的窗口，第二个参数为回调函数，鼠标触发的任何事件，都将立刻通知draw_listener2。

(1)、在窗口中，鼠标双击位置画圆        
![Alt Text](https://github.com/wq923/OpenCV/blob/master/mouse_paint/circle.png)    
![Alt Text](https://github.com/wq923/OpenCV/blob/master/mouse_paint/circle01.png)    

(2)、在窗口中，鼠标拖动的区域画圆或者矩形        
最终虽然实现了实践中要求的画矩形，但是是鼠标左键抬起时才开始绘制，绘制过程看不到，效果不是很好。    
![Alt Text](https://github.com/wq923/OpenCV/blob/master/mouse_paint/rectangle01.png)        

后续是否可以通过增加透明图层的方式进行绘制？        

![Alt Text](https://github.com/wq923/OpenCV/blob/master/mouse_paint/rectangle.png)

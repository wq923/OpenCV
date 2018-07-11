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
## 图像上的算术运算

图像上的算术运算包括加法、减法、位运算等。
    
    cv2.add()           //图像加法
    cv2.addWeighted()   //图像混合

### 图像加法
使用cv2.add()可以对两幅图像进行加法运算，当然也可以使用 Numpy，res = img1 + img2。

    注意：
    1、两幅图像大小和类型必须一致；或者第二幅图像可以简单使用标量值
    2、OpenCV 中的加法操作是一种”饱和操作”，Numpy 的加法是“模操作”。

OpenCV 加法和 Numpy 加法的操作结果有很大不同，如下程序：
    
    import cv2
    import numpy as np
    
    x = np.uint8([250])
    y = np.uint8([10])
    
    print(cv2.add(x, y))
    
    print(x + y)
    
    # 结果
    # [[255]]
    # [4]

这种差别在图像进行加法时将更加明显。OpenCV 的结果要好一些，所以尽量使用 OpenCV 中的函数。
    
### 图像混合

这其实也是加法，但是可以设置两幅图像为不同权重，给人一种透明或混合的感觉。

图像混合的公式如下：

    g（x） = （1-a）*f（x） + a*f（x）

通过修改a（0-1之间）的值，实现很酷炫的混合效果。

取 a = 0.7，混合 OpenCV.png 和 img2.png

    import cv2
    
    # 注意 523*526 ，两张图像需要有相同长宽的像素数
    img1 = cv2.imread("img2.png")
    img2 = cv2.imread("OpenCV.png")
    
    dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
    
    cv2.imshow("weighted", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

混合结果：
![Alt Text](https://github.com/wq923/OpenCV/blob/master/part_7_img_calc/after_weighted.png)    

### 按位运算
位操作：
    
    AND、OR、NOT、XOR
当我们提取图像一部分，选择非矩形的ROI时，这些操作会很有用。
下面的例子教我们如何改变一幅图的一部分区域。
要把 OpenCV 标志放到另一幅图像上。使用加法，会导致颜色会改变；使用混合，
会有透明效果；如果用ROI，又不是矩形。所以选择位运算。



## 1、获取并修改像素值
    
    # 获取并修改像素值

    import cv2
    
    img = cv2.imread("car.jpg")
    
    # 根据行和列获取像素值，对于彩色图像，返回（R\G\B）
    px = img[100, 100]
    print(px)
    blue = img[100, 100, 0]
    print(blue)
    
    # 修改像素的值
    img[100, 100] = [255, 255, 255]
    print(img[100, 100])
    
    
    # 逐个修改每个像素的值会很慢，尽量使用 Numpy 矩阵运算
    print(img.item(10, 10, 2))
    img.itemset((10, 10, 2), 100)
    print(img.item(10, 10, 2))


## 2、获取图像属性
图像属性包括：
    
    ·行           img.shape
    ·列           img.shape
    ·通道         img.shape
    ·图像数据类型   img.dtype
    ·像素数目      img.size

    import cv2

    img = cv2.imread("car.jpg")
    # 返回行、列、通道，例如，(768, 1024, 3)，灰白图像只返回行列
    print(img.shape)
    
    # 返回像素数，例如，2359296。
    print(img.size)
    
    # 返回图像的数据类型，例如，uint8。
    print(img.dtype)


## 3、图像ROI
    ROI（region of interest），感兴趣区域。机器视觉、图像处理中，从被处理的图像以方框、圆、椭圆、不规则多边形等方式勾勒出需要处理的区域，称为感兴趣区域，ROI。
    在Halcon、OpenCV、Matlab等机器视觉软件上常用到各种算子（Operator）和函数来求得感兴趣区域ROI，并进行图像的下一步处理。

对图像中的特定区域，进行操作。例如，我们检测出一张图中的眼睛位置，我们首先找到脸，再在脸中找到眼睛，而不是直接在一副图中查找人眼。
这样会大大提高程序准确率和性能。
    
    //例子中找到了车的名称位置，并扣取出来。
    import cv2

    img = cv2.imread("car.jpg")
    print(img.shape)
    
    # 注意，OpenCV 里的坐标系，先行后列，即img[y, x]
    car = img[500:600, 400:500]
    img[0:100, 0:100] = car
    
    cv2.imwrite("car_copy.jpg", img)

![Alt Text](https://github.com/wq923/OpenCV/blob/master/part_6_imge_opr/roi.png)    


## 4、拆分和合并图像通道
有时我们需要对BGR三个通道分别进行操作，这时就需要把 BGR 拆成单通道，有时也需要把独立通道的图片合并成一个 BGR 图像。

    # 拆分和合并图像通道

    import cv2
    
    # img = cv2.imread("car.jpg")
    #
    # cv2.split 拆分通道比较耗时，尽量用 Numpy
    # b, g, r = cv2.split(img)
    # img = cv2.merge([b, g, r])
            
    img = cv2.imread('car.jpg')
    # 让所有像素的红色通道都为 0 ，不必先拆分再赋值
    img[:, :, 2] = 0
    
    cv2.imshow("img", img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

## 5、为图像扩边
如果你想要在图像周围创建一个边，类似相框。使用如下API：
    
    cv2.copyMakeBorder()

这经常在卷积运算或者 0 填充时用到。

    import cv2
    from matplotlib import pyplot as plt

    BLUE = [255, 0, 0]
    
    img = cv2.imread("car.jpg")
    
    # 原始图像、上下左右对应的像素数，添加边界的类型（拉最外面一层像素、拉镜像像素等）
    replicate = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REFLECT)
    reflect_101 = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_WRAP)
    constant = cv2.copyMakeBorder(img, 20, 20, 20, 20, cv2.BORDER_CONSTANT)
    
    
    # 2行 3列的图表
    plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
    plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('BORDER_REPLICATE')
    plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('BORDER_REFLECT')
    plt.subplot(234), plt.imshow(reflect_101, 'gray'), plt.title('BORDER_REFLECT_101')
    plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('BORDER_WRAP')
    plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('BORDER_CONSTANT')
    
    plt.show()
    
    

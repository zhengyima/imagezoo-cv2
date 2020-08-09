"""
目标
    访问和修改图片像素点的值
    获取图片的宽、高、通道数等属性
    了解感兴趣区域ROI
    分离和合并图像通道

    img[y,x]获取/设置像素点值
    img.shape：图片的形状（行数、列数、通道数）
    img.dtype：图像的数据类型。
    img[y1:y2,x1:x2]进行ROI截取
    cv2.split()/cv2.merge()通道分割/合并
    更推荐的获取单通道方式：b = img[:, :, 0]。

"""
import cv2

img = cv2.imread('ims/1.jpg')

# 1、获取和修改像素点值
px = img[100, 90]
print(px)
px_blue = img[100, 90, 0]  # 只获取蓝色blue通道的值
print(px_blue)
img[100, 90] = [255, 255, 255]  # 修改像素的值
print(img[100, 90])  # [255 255 255]

# 2、 图片属性
height, width, channels = img.shape  # 行数（高度）、列数（宽度）和通道数
print(height, width, channels)
print(img.dtype)  # 获取图像数据类型
print(img.size)   # 获取图像总像素数

# 3、ROI  感兴趣区域。什么意思呢？比如我们要检测眼睛，因为眼睛肯定在脸上，所以我们感兴趣的只有脸这部分，其他都不care，所以可以单独把脸截取出来，这样就可以大大节省计算量，提高运行速度。

face = img[500:800, 515:888]


# 4、通道分割与合并
b, g, r = cv2.split(face)
img = cv2.merge((b, g, r))

b = img[:, :, 0]
cv2.imshow('blue', b)
cv2.waitKey(0)
"""
目标

    实现旋转、平移和缩放图片
    OpenCV函数：cv2.resize(), cv2.flip(), cv2.warpAffine()

    cv2.resize()缩放图片，可以按指定大小缩放，也可以按比例缩放。
    cv2.flip()翻转图片，可以指定水平/垂直/水平垂直翻转三种方式。
    平移/旋转是靠仿射变换cv2.warpAffine()实现的。

"""

import cv2
import numpy as np

img = cv2.imread('3.jpg')


# 1、按照指定的宽度、高度缩放图片
res1 = cv2.resize(img, (132, 150))

# 2、按照比例缩放，如x,y轴均放大一倍
res2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# 3、翻转图片
res3 = cv2.flip(img, 0)
cv2.imshow('zoom', res3)
cv2.waitKey(0)

# 4、平移图片
rows, cols = img.shape[:2]
# 定义平移矩阵，需要是numpy的float32类型
# x轴平移100，y轴平移50
M = np.float32([[1, 0, 100], [0, 1, 50]])
res4 = cv2.warpAffine(img, M, (cols, rows)) # 用仿射变换实现平移

# 5、旋转图片
rows, cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.5) # 45°旋转图片并缩小一半
res5 = cv2.warpAffine(img, M, (cols, rows)) # 平移/旋转是靠仿射变换

cv2.imshow('zoom', res5)
cv2.waitKey(0)



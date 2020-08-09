"""
目标

    模糊/平滑图片来消除图片噪声
    OpenCV函数：cv2.blur(), cv2.GaussianBlur(), cv2.medianBlur(), cv2.bilateralFilter()
小结

    在不知道用什么滤波器好的时候，优先高斯滤波cv2.GaussianBlur()，然后均值滤波cv2.blur()。
    斑点和椒盐噪声优先使用中值滤波cv2.medianBlur()。
    要去除噪点的同时尽可能保留更多的边缘信息，使用双边滤波cv2.bilateralFilter()。
    线性滤波方式：均值滤波、方框滤波、高斯滤波（速度相对快）。
    非线性滤波方式：中值滤波、双边滤波（速度相对慢）。

"""
import cv2
import numpy as np

# img = cv2.imread('./ims/lena.jpg')
# # 1.均值滤波
# blur = cv2.blur(img, (3, 3))
#
# # 上面的均值滤波也可以用方框滤波实现：normalize=True
# # blur = cv2.boxFilter(img, -1, (3, 3), normalize=True)
#
#
# # 2.高斯滤波
# gau_blur = cv2.GaussianBlur(img, (3, 3), 0)
#
# # 三张图片横向叠加对比显示
# res = np.hstack((img, blur, gau_blur))
# cv2.imshow('res', res)
# cv2.waitKey(0)


# # 均值滤波vs高斯滤波
# img = cv2.imread('./ims/gaussian_noise.bmp')
# blur = cv2.blur(img, (5, 5))  # 均值滤波
# gaussian = cv2.GaussianBlur(img, (5, 5), 1)  # 高斯滤波
#
# res = np.hstack((img, blur, gaussian))
# cv2.imshow('gaussian vs average', res)
# cv2.waitKey(0)

# # 3.均值滤波vs中值滤波
# img = cv2.imread('./ims/salt_noise.bmp', 0)
#
# blur = cv2.blur(img, (5, 5))  # 均值滤波
# median = cv2.medianBlur(img, 5)  # 中值滤波
#
# res = np.hstack((img, blur, median))
# cv2.imshow('median vs average', res)
# cv2.waitKey(0)

# 4.双边滤波vs高斯滤波
img = cv2.imread('ims/lena.jpg', 0)
gau = cv2.GaussianBlur(img, (5, 5), 0)  # 高斯滤波
blur = cv2.bilateralFilter(img, 5, 75, 75)  # 双边滤波

res = np.hstack((img, gau, blur))
cv2.imshow('res', res)
cv2.waitKey(0)











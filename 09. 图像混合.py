import cv2
import numpy as np

# 1.图片相加
x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x, y))  # 250+10 = 260 => 255
print(x + y)  # 250+10 = 260 % 256 = 4


# 2.图像混合
# img1 = cv2.imread('./ims/2.jpg')
# img2 = cv2.imread('./ims/3.jpg')
# res = cv2.addWeighted(img1, .6, img2, .4, 0)
#
# cv2.imshow('blending', res)
# cv2.waitKey(0)


# 3.按位操作
img1 = cv2.imread('ims/1.jpg')
img2 = cv2.imread('3.jpg')

# 把logo放在左上角，所以我们只关心这一块区域
rows, cols = img2.shape[:2]
roi = img1[:rows, :cols]

# 创建掩膜
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# 保留除logo外的背景
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
dst = cv2.add(img1_bg, img2)  # 进行融合
img1[:rows, :cols] = dst  # 融合后放在原图上

cv2.imshow('result', img1)
cv2.waitKey(0)
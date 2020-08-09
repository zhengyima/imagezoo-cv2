import cv2

# 灰度图读入
img = cv2.imread('3.jpg', 0)

# 阈值分割 固定阈值
ret, th = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO_INV)
# 自适应阈值
th2 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
cv2.imshow('thresh', th2)
cv2.waitKey(0)


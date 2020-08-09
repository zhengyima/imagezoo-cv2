import cv2
img = cv2.imread("ims/1.jpg", 0)
print(img)
cv2.namedWindow('lena1',cv2.WINDOW_NORMAL)
cv2.imshow('lena1', img)
cv2.waitKey(0)

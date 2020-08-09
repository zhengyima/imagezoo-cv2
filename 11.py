# ex2tron's blog:
# http://ex2tron.wang

import cv2
import numpy as np
import os

# def track_back(x):
#     pass
#
# PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
# data_path = os.path.join(PROJECT_ROOT, "3.jpg")
# img = cv2.imread(data_path, 0)
# cv2.namedWindow('window')
#
# # 创建滑动条
# cv2.createTrackbar('maxVal', 'window', 100, 255, track_back)
# cv2.createTrackbar('minVal', 'window', 200, 255, track_back)
#
# while(True):
#     # 获取滑动条的值
#     max_val = cv2.getTrackbarPos('maxVal', 'window')
#     min_val = cv2.getTrackbarPos('minVal', 'window')
#
#     edges = cv2.Canny(img, min_val, max_val)
#     cv2.imshow('window', edges)
#
#     # 按下ESC键退出
#     if cv2.waitKey(30) == 27:
#         break

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    edges = cv2.Canny(frame, 100, 100)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # 灰度图
    cv2.namedWindow('shen', cv2.WINDOW_NORMAL)
    cv2.imshow('shen', edges)
    if cv2.waitKey(1) == ord('q'):
        break
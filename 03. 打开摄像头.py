import cv2
capture = cv2.VideoCapture(0)
# 获取捕获的分辨率
# propId可以直接写数字，也可以用OpenCV的符号表示
width, height = capture.get(3), capture.get(4)
print(width, height)
# 以原分辨率的一倍来捕获
capture.set(cv2.CAP_PROP_FRAME_WIDTH, width * 5)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height * 5)
while True:
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # 灰度图
    cv2.namedWindow('shen', cv2.WINDOW_NORMAL)
    cv2.imshow('shen', gray)
    if cv2.waitKey(1) == ord('q'):
        break

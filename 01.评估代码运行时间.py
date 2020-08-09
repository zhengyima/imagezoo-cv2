import cv2
import time
start = cv2.getTickCount()

for i in range(3):
    print("111")
    time.sleep(1)

end = cv2.getTickCount()

print((end - start) / cv2.getTickFrequency())
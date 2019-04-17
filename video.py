import cv2
import numpy
import time

cap = cv2.VideoCapture(0)
time.sleep(5)

while True:
    ret, frame = cap.read()
    print(ret)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

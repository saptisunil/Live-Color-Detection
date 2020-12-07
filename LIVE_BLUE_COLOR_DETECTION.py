import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    result = frame.copy()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([94,80,2])
    upper = np.array([126,255,255])
    mask = cv2.inRange(frame, lower, upper)
    result = cv2.bitwise_and(result, result, mask=mask)
    cv2.imshow('result', result)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import os
import cv2

''' Altered from https://www.codingforentrepreneurs.com/blog/how-to-record-video-in-opencv-python '''

filename = 'Video/video.avi'
frames_per_second = 24.0
res = (1280, 720)

cap = cv2.VideoCapture(0)
cap.set(3, res[0])
cap.set(4, res[1])
out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'XVID'), 25, (res[0], res[1]))

while True:
    ret, frame = cap.read()
    out.write(frame)
    print(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()
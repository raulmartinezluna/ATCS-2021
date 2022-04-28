import os
import cv2

''' Altered from https://www.codingforentrepreneurs.com/blog/how-to-record-video-in-opencv-python '''

class Video:

    filename = 'Video/video.mp4'
    framesPerSecond = 24.0
    resolution = (1280, 720)
    def __init__(self, fn, fps, w, h):
        filename = fn
        framesPerSecond = fps
        resolution = (w, h)

    def create(self):
        width = self.resolution[0]
        height = self.resolution[1]
        cap = cv2.VideoCapture(0)
        cap.set(3, width)
        cap.set(4, height)
        out = cv2.VideoWriter(self.filename, cv2.VideoWriter_fourcc(*'XVID'), 25, (width, height))

        while True:
            ret, frame = cap.read()
            out.write(frame)
            print(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    video = Video('Video/video.mp4', 24.0, 1280, 720)
    video.create()
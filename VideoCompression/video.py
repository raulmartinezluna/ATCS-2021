import os
import cv2 as cv

class Video:

    filenameOriginal = 'Video/videoOriginal.mp4'
    filenameCompressed = 'Video/videoCompressed.mp4'
    framesPerSecond = 24.0
    resolution = (1280, 720)

    def __init__(self, fnO, fnC, fps, w, h):
        self.filenameOriginal = fnO
        self.filenameCompressed = fnC
        self.framesPerSecond = fps
        self.resolution = (w, h)

    def create(self):
        ''' Altered from https://www.codingforentrepreneurs.com/blog/how-to-record-video-in-opencv-python '''
        width = self.resolution[0]
        height = self.resolution[1]
        cap = cv.VideoCapture(0)
        cap.set(3, width)
        cap.set(4, height)
        videoOriginal = cv.VideoWriter(self.filenameOriginal, cv.VideoWriter_fourcc(*'XVID'), 25, (width, height))
        videoCompressed = cv.VideoWriter(self.filenameCompressed, cv.VideoWriter_fourcc(*'XVID'), 25, (width, height))


        while True:
            ret, frame = cap.read()
            videoOriginal.write(frame)
            #Alter frames right here

            videoCompressed.write(frame)
            #Alter frames right here
            cv.imshow('frame', frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        videoOriginal.release()
        videoCompressed.release()
        cv.destroyAllWindows()
        ''' Altered from https://www.codingforentrepreneurs.com/blog/how-to-record-video-in-opencv-python '''

if __name__ == '__main__':
    video = Video('Video/videoOriginal.mp4', 'Video/videoCompressed.mp4', 24.0, 1280, 720)
    video.create()
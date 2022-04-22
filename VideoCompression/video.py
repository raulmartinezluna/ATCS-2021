'''
Program: Records a video and provides an original version and a compressed version
Teacher: Nandhini Namasivayam
Student Author: Raul Martinez Luna
Started: April 22nd, 2020
Finished: N/A
'''

''' Libraries '''
import cv2 as cv
import os

''' Object handles video recording '''
class VideoRecorder:
    '''
        Function takes in cv and returns a tuple of retList & frameList.
        ret is a boolean that says whether it's accompanying frame is usable.
        (ret makes up retList & frame makes up frameList)
        '''

    def takeVideo(self):

        ''' Code below is partially from https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/ '''

        webcam = cv.VideoCapture(0)
        retList = []
        frameList = []

        while (True):
            ret, frame = webcam.read()
            cv.imshow('Recorder', frame)
            retList.append(ret)
            frameList.append(frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        webcam.release()
        cv.destroyAllWindows()

        ''' Code above is partially from https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/ '''
        return zip(retList, frameList)

if __name__ == '__main__':
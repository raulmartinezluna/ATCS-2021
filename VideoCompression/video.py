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

    ''' Object Variables '''
    framesDirectory = ""
    videoDirectory = ""

    '''
    Initiates class by receiving the objects variables
    '''
    def __init__(self, fD, vD):
        self.framesDirectory = fD
        self.videoDirectory = vD

    '''
    Function deletes every image in the Frames folder, this is done so that frames from a previous run do not conflict with the new run.
    '''
    def deleteFilesInFramesFolder(self):
        ''' Code below is from https://www.techiedelight.com/delete-all-files-directory-python/ '''
        for file in os.listdir(self.framesDirectory):
            os.remove(os.path.join(self.framesDirectory, file))
        ''' Code above is from https://www.techiedelight.com/delete-all-files-directory-python/ '''

    '''
    Function deletes every image in the Video folder, this is done so that frames from a previous run do not conflict with the new run.
    '''
    def deleteFilesInVideoFolder(self):
        ''' Code below is from https://www.techiedelight.com/delete-all-files-directory-python/ '''
        for file in os.listdir(self.videoDirectory):
            os.remove(os.path.join(self.videoDirectory, file))
        ''' Code above is from https://www.techiedelight.com/delete-all-files-directory-python/ '''

    '''
    Function deletes every image in the Video and Frames folder, clearing the folders for further use.
    '''
    def deleteFiles(self):
        self.deleteFilesInFramesFolder()
        self.deleteFilesInVideoFolder()

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

    '''
    Function takes in zipped retList & frameList and combines them into a single variable in a certain format.
    '''
    def makeVideo(self, videoAspects):
        video = []
        for ret, frame in self.takeVideo():
            temp_list = [ret, frame]
            video.append(temp_list)
        return video

    def downloadFrames(self, video):
        count = 1
        for frame in video:
            if frame[0] == True:
                # Subsequent line taken from https://appdividend.com/2020/06/23/python-cv2-imwrite-python-cv2-save-image-example/ and alter slightly
                cv.imwrite(self.framesDirectory+'/Frame_' + str(count) + '.jpg', frame[1])
                count += 1

    '''
    Counts the amount of frames in a video
    '''
    def countFramesInVideo(self, video):
        count = 1
        for frame in video:
            if frame[0] == True:
                count += 1
        print("Amount of Frames: " + str(count - 1))

if __name__ == '__main__':
    recorder = VideoRecorder(fD="Frames", vD="Video" )
    recorder.deleteFiles()
    video = recorder.makeVideo(recorder.takeVideo())
    recorder.downloadFrames(video)
    recorder.countFramesInVideo(video)
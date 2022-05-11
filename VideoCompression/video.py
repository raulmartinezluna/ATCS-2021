''' Libraries '''
import os
import cv2 as cv
from compressor import FrameCompressor

'''
Class Purpose: Creates a class that records and outputs an uncompressed and compressed video
'''
class Video:

    '''
    Purpose: initializer
    '''
    def __init__(self, fnV, fnO, fnC, fps, w, h):
        self.filenameVideo = fnV
        self.filenameOriginal = fnO
        self.filenameCompressed = fnC
        self.framesPerSecond = fps
        self.resolution = (w, h)


    '''
    Purpose: cleans up the code nicely
    '''
    def create(self):
        self.clearMemory()
        self.createVideo()
        self.createFrames()
        self.compressFrames()
        self.createUncompressedVideo()
        self.createCompressedVideo()

    '''
    Purpose: clears every directory this program requires
    '''
    def clearMemory(self):
        self.deleteFilesInFramesFolder()
        self.deleteFilesInVideoFolder()

    '''
     Purpose: deletes every image in 'Frames', this is done so that frames from a previous run do not conflict with the new run.
     '''
    def deleteFilesInFramesFolder(self):
        ''' Code below is from https://www.techiedelight.com/delete-all-files-directory-python/ '''
        for file in os.listdir("Frames/FramesUncompressed"):
            os.remove(os.path.join("Frames/FramesUncompressed", file))
        for file in os.listdir("Frames/FramesCompressed"):
            os.remove(os.path.join("Frames/FramesCompressed", file))
        ''' Code above is from https://www.techiedelight.com/delete-all-files-directory-python/ '''

    '''
    Purpose: deletes every image in 'Video', this is done so that frames from a previous run do not conflict with the new run.
    '''
    def deleteFilesInVideoFolder(self):
        ''' Code below is from https://www.techiedelight.com/delete-all-files-directory-python/ '''
        for file in os.listdir("Video"):
            os.remove(os.path.join("Video", file))
        ''' Code above is from https://www.techiedelight.com/delete-all-files-directory-python/ '''

    '''
    Purpose: takes video and stores it in video folder
    '''
    def createVideo(self):
        ''' Altered from https://www.codingforentrepreneurs.com/blog/how-to-record-video-in-opencv-python '''
        cap = cv.VideoCapture(0)
        cap.set(3, self.resolution[0])
        cap.set(4, self.resolution[1])
        video = cv.VideoWriter(self.filenameVideo, cv.VideoWriter_fourcc(*'XVID'), self.framesPerSecond, (self.resolution[0], self.resolution[1]))
        while True:
            ret, frame = cap.read()
            video.write(frame)
            cv.imshow('Recording...', frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        video.release()
        cv.destroyAllWindows()
        ''' Altered from https://www.codingforentrepreneurs.com/blog/how-to-record-video-in-opencv-python '''

    '''
    Purpose: extracts frames from the video that is taken and inserts it into 'Frame/FramesOriginal' 
    '''
    def createFrames(self):
        cap = cv.VideoCapture(self.filenameVideo)
        ret, frame = cap.read()
        count = 0
        while ret:
            cv.imwrite("Frames/FramesUncompressed/frame%d.jpg" % count, frame)  # save frame as jpg file
            ret, frame = cap.read()
            count += 1

    '''
    Purpose: compresses frames from 'Frame/FramesOriginal' and inserts them into 'Frame/FramesCompressed'
    '''
    def compressFrames(self):
        compressor = FrameCompressor()
        for frameIndex in range(0, len(os.listdir("Frames/FramesUncompressed"))):
            frame = cv.imread('Frames/FramesUncompressed/frame'+str(frameIndex)+'.jpg', 1)
            frame = compressor.compressImage(compressor.loadImage(frame), 2)
            cv.imwrite("Frames/FramesCompressed/frame%d.jpg" % frameIndex, frame)  # save frame as jpg file

    ''' 
    Purpose: creates an uncompressed video in 'Frames' from frames in 'Frames/FramesUncompressed'
    '''
    def createUncompressedVideo(self):
        ''' Altered from https://www.codingforentrepreneurs.com/blog/how-to-record-video-in-opencv-python '''
        video = cv.VideoWriter(self.filenameOriginal, cv.VideoWriter_fourcc(*'mp4v'), self.framesPerSecond, (self.resolution[0], self.resolution[1]))

        for frameIndex in range(0, len(os.listdir("Frames/FramesUncompressed"))):
            frame = cv.imread('Frames/FramesUncompressed/frame'+str(frameIndex)+'.jpg', 1)
            video.write(frame)

        cv.destroyAllWindows()
        video.release()

        ''' Altered from https://www.codingforentrepreneurs.com/blog/how-to-record-video-in-opencv-python '''
    '''
    Purpose: creates a compressed video in 'Frames' from frames in 'Frames/FramesCompressed'
    '''
    def createCompressedVideo(self):
        ''' Altered from https://www.codingforentrepreneurs.com/blog/how-to-record-video-in-opencv-python '''
        video = cv.VideoWriter(self.filenameCompressed, cv.VideoWriter_fourcc(*'mp4v'), self.framesPerSecond, (self.resolution[0], self.resolution[1]))

        for frameIndex in range(0, len(os.listdir("Frames/FramesCompressed"))):
            frame = cv.imread('Frames/FramesCompressed/frame'+str(frameIndex)+'.jpg', 1)
            video.write(frame)

        cv.destroyAllWindows()
        video.release()
        ''' Altered from https://www.codingforentrepreneurs.com/blog/how-to-record-video-in-opencv-python '''

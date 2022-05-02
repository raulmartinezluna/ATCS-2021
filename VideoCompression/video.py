import os
import cv2 as cv
import numpy as np
from sklearn.cluster import KMeans

class FrameCompressor:

    def __init__(self):
        self.img_size = None

    def loadImage(self, frame):
        """
        Loads the image from the path as a 2D List (Height x Width) of [R,G,B] values.
        :param filepath: Path to the original image
        :return: 2D List of [R, G, B] values
        """
        # Read the image
        img = frame
        self.img_size = img.shape

        return img

    def convertTo1D(self, img):
        """
        Converts a 2D List of [R,G,B] values into a 1D List of [R,G,B] values
        :param img: 2D List of [R,G,B] values that represent an image
        :return: 1D List of [R,G,B] values that represent an image
        """
        return img.reshape(self.img_size[0] * self.img_size[1], self.img_size[2])

    def convertTo2D(self, img):
        """
        Converts a 1D List of pixels where each pixel is represented by [R,G,B] into
        a 2D List of dimensions height x width where each entry is a [R,G,B] pixel
        :param img: 1D List of [R,G,B] values for each pixel
        :return: 2D list of dimensions height x width where each entry is an [R,G,B] pixel
        """
        img = np.clip(img.astype('uint8'), 0, 255)
        img = img.reshape(self.img_size[0], self.img_size[1], self.img_size[2])
        return img

    def compressImage(self, img, num_colors):
        """
        Compresses the image using KMeans clustering to contain
        only a set number of colors
        :param img: A 2D List of [R, G, B] values representing the image
        :return: A 2D List of [R, G, B] values representing the compressed image
        """
        # TODO
        compressed_img = self.convertTo1D(img)

        ''' Create the Model '''
        #Amount of colors
        k = num_colors
        km = KMeans(n_clusters=k).fit(compressed_img)

        centroids = km.cluster_centers_
        labels = km.labels_

        for i in range(len(compressed_img)):
            compressed_img[i] = centroids[labels[i]]

        compressed_img = self.convertTo2D(compressed_img)

        return compressed_img

class Video:

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

        frameList = []
        while True:
            ret, frame = cap.read()
            frameList.append(frame)
            videoOriginal.write(frame)
            cv.imshow('Recording...', frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        videoOriginal.release()
        cv.destroyAllWindows()
        print("Total Frames: " + str(len(frameList)))
        count = 1
        for frame in frameList:
            compressor = FrameCompressor()
            compressedFrame = compressor.compressImage(compressor.loadImage(frame), 10)
            videoCompressed.write(compressedFrame)
            print("Frames Compressed: "+ str(count))
            count+= 1
        videoCompressed.release()
        ''' Altered from https://www.codingforentrepreneurs.com/blog/how-to-record-video-in-opencv-python '''

if __name__ == '__main__':
    video = Video('Video/videoOriginal.mp4', 'Video/videoCompressed.mp4', 24.0, 1280, 720)
    video.create()
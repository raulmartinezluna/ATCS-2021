''' Libraries '''
from sklearn.cluster import KMeans
import numpy as np

class FrameCompressor:

    def __init__(self):
        self.img_size = None

    """
    Loads the image from the path as a 2D List (Height x Width) of [R,G,B] values.
    :param filepath: Path to the original image
    :return: 2D List of [R, G, B] values
    """
    def loadImage(self, frame):

        # Read the image
        img = frame
        self.img_size = img.shape

        return img

    """
    Converts a 2D List of [R,G,B] values into a 1D List of [R,G,B] values
    :param img: 2D List of [R,G,B] values that represent an image
    :return: 1D List of [R,G,B] values that represent an image
    """
    def convertTo1D(self, img):

        return img.reshape(self.img_size[0] * self.img_size[1], self.img_size[2])

    """
    Converts a 1D List of pixels where each pixel is represented by [R,G,B] into
    a 2D List of dimensions height x width where each entry is a [R,G,B] pixel
    :param img: 1D List of [R,G,B] values for each pixel
    :return: 2D list of dimensions height x width where each entry is an [R,G,B] pixel
    """
    def convertTo2D(self, img):

        img = np.clip(img.astype('uint8'), 0, 255)
        img = img.reshape(self.img_size[0], self.img_size[1], self.img_size[2])
        return img

    """
    Compresses the image using KMeans clustering to contain
    only a set number of colors
    :param img: A 2D List of [R, G, B] values representing the image
    :return: A 2D List of [R, G, B] values representing the compressed image
    """
    def compressImage(self, img, num_colors):

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
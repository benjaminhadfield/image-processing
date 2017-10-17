import math

from PIL import Image
import numpy as np
from sklearn.cluster import KMeans as _KMeans
import matplotlib.pyplot as plt


class KMeans:
    """
    K-Means.
    For simplicity images used are converted to greyscale.
    """
    def __init__(self, image, k=2):
        """
        :param k: Number of clusters.
        """
        self.k = k
        self.im = Image.open(image).convert('L')
        self.result = self.im.copy()
        self.pixels = self.im.getdata()
        self.histogram = self.im.histogram()

        # Run K-Means algorithm.
        self.run()

    @staticmethod
    def _assign_pixel_labels(pixels, centroids):
        """
        Returns an array of labels corresponding to the labels given to each
        pixel in pixels.
        """
        if not pixels or not centroids:
            raise ValueError()
        labels = []
        for p in pixels:
            distances = []
            for c in centroids:
                distances.append(abs(p - c))
            labels.append(distances.index(min(distances)))
        return labels

    @staticmethod
    def _amplify_pixels(pixels, k):
        return list(map(lambda x: x * 255 / (k-1), pixels))

    def run(self):
        """
        For simplicity, this implementation will only deal with greyscale
        images.
        :return: [c, l] - array (len k) of centroid coords, array of size of
        input image containing pixel labels.
        """
        # Select random starting centroids. These centroids are simple
        # one-dimensional scalars representing pixel intensity.
        # If this implementation dealt with RGB images, then each centroid would
        # have three dimensions, one for each channel.
        centres = list(map(lambda v: math.floor(v * 255), np.random.rand(self.k)))
        labelled_pixels = self._assign_pixel_labels(self.pixels, centres)
        labelled_pixels = self._amplify_pixels(labelled_pixels, self.k)
        self.result.putdata(labelled_pixels)
        return self

    def print_result(self):
        self.result.save('img/out/k-means-{}.jpg'.format(self.k))


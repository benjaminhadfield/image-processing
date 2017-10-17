import math

from PIL import Image
import numpy as np
from sklearn.cluster import KMeans as _KMeans
import matplotlib.pyplot as plt


def setup():
    try:
        k = int(input('Enter the k value.\n'))
        if k < 1:
            raise ValueError()
        return KMeans('img/river.jpg', k)
    except:
        print('Please enter a positive integer.')
        setup()


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
        self.pixels = self.im.getdata()
        self.histogram = self.im.histogram()

    @staticmethod
    def _lists_equal(a, b, threshold=1):
        """
        Takes two lists of equal length, and returns true if each zipped pair
        is at most `threshold` apart.
        e.g. ([1.2, 10.5], [1.5, 12], 1) would check
            - abs(1.2 - 1.5) < 1
            - abs(10.5 - 12) < 1
        and return the AND of each check.
        """
        if len(a) != len(b):
            raise ValueError('Both lists must have the same length.')
        checks = map(lambda x: abs(x[0] - x[1]) <= threshold, zip(a, b))
        return all(checks)

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

    def _generate_centroids(self, labels, prev_centroids):
        centroids = []
        for i in range(self.k):
            pixels_for_centroid = list(map(
                lambda x: x[0],
                filter(lambda x: x[1] == i, zip(self.pixels, labels))))
            length = len(pixels_for_centroid)
            if length == 0:
                centroids.append(prev_centroids[i])
            else:
                centroids.append(float(
                    sum(pixels_for_centroid) / len(pixels_for_centroid)))
        return centroids

    def _amplify_pixels(self, pixels):
        return list(map(lambda x: x * 255 / (self.k-1), pixels))

    def run(self, threshold=1, print_iter=False, save_result=False):
        """
        For simplicity, this implementation will only deal with greyscale
        images.
        :return: [c, l] - array (len k) of centroid coords, array of size of
        input image containing pixel labels.
        """
        # (Step 1)
        # Select random starting centroids. These centroids are simple
        # one-dimensional scalars representing pixel intensity.
        # If this implementation dealt with RGB images, then each centroid would
        # have three dimensions, one for each channel.
        labels = []
        centroids = list(map(
            lambda v: math.floor(v * 255), np.random.rand(self.k)))
        # Sort so centroids for higher intensity have higher index.
        centroids.sort()
        prev_centroids = None
        if print_iter:
            print('starting centroids', centroids)
        # Repeat until convergence
        while not prev_centroids \
                or not self._lists_equal(centroids, prev_centroids, threshold):
            prev_centroids = centroids
            # (Step 2)
            # Label each pixel with the index of the closes centroid.
            labels = self._assign_pixel_labels(self.pixels, centroids)
            # (Step 3)
            # Update each centroid to the mean of pixels labeled to it.
            centroids = self._generate_centroids(labels, prev_centroids)
            if print_iter:
                print('centroids', centroids, 'prev', prev_centroids)
        # At this point the centroids have stabilised to a point satisfying
        # `threshold`.
        if print_iter:
            print('Converged (t={})\n'.format(threshold), centroids)
        if save_result:
            self.save_result(labels)
        return labels, centroids

    def save_result(self, labels):
        w, h = self.im.size
        adjusted_labels = self._amplify_pixels(labels)
        image = [adjusted_labels[i:i + w] for i in range(0, len(adjusted_labels), w)]
        arr = np.array(image, dtype=np.uint8)
        out = Image.fromarray(arr)
        out.save('img/out/k-means-{}.jpg'.format(self.k))

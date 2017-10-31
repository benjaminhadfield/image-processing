from PIL import Image
import numpy as np

from src.utils.models import ImageModel
from src.utils.validation import is_gt, is_int


class KMeans(ImageModel):
    """
    K-Means.
    For simplicity images used are converted to greyscale.
    """
    def __init__(self, k=2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.k = k
        self.t = 1

    @staticmethod
    def setup():
        try:
            k = int(input('Enter the k value.\n'))
            _ = is_gt(k, threshold=0)
            return KMeans(k, image='img/river.jpg')
        except ValueError:
            print('Please enter a positive integer.')
            return KMeans.setup()

    def _lists_equal(self, a, b):
        """
        Takes two lists of equal length, and returns true if each zipped pair
        is at most `threshold` apart.
        e.g. ([1.2, 10.5], [1.5, 12], 1) would check
            - abs(1.2 - 1.5) < 1
            - abs(10.5 - 12) < 1
        returning the AND of each check.
        """
        if len(a) != len(b):
            raise ValueError('Both lists must have the same length.')
        checks = map(lambda x: abs(x[0] - x[1]) <= self.t, zip(a, b))
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
        pixels = self.im.getdata()
        centroids = []
        for i in range(self.k):
            pixels_for_centroid = list(map(
                lambda x: x[0],
                filter(lambda x: x[1] == i, zip(pixels, labels))))
            length = len(pixels_for_centroid)
            if length == 0:
                centroids.append(prev_centroids[i])
            else:
                centroids.append(float(
                    sum(pixels_for_centroid) / len(pixels_for_centroid)))
        return centroids

    def _amplify_pixels(self, pixels):
        return list(map(lambda x: x * 255 / (self.k-1), pixels))

    def run(self):
        labels = []
        # (Step 1)
        # Select random starting centroids. These centroids are simple
        # one-dimensional scalars representing pixel intensity.
        # If this implementation dealt with RGB images, then each centroid would
        # have three dimensions, one for each channel.
        centroids = [i * (255 / self.k) for i in range(self.k)]
        prev_centroids = None
        # Repeat until convergence
        while not prev_centroids \
                or not self._lists_equal(centroids, prev_centroids):
            prev_centroids = centroids
            # (Step 2)
            # Label each pixel with the index of the closes centroid.
            labels = self._assign_pixel_labels(self.pixels, centroids)
            # (Step 3)
            # Update each centroid to the mean of pixels labeled to it.
            centroids = self._generate_centroids(labels, prev_centroids)
        # At this point the centroids have stabilised to a point satisfying
        # `threshold`.
        matrix = self.pixel_matrix(
            self._amplify_pixels(labels), self.im.size)
        return Image.fromarray(matrix)

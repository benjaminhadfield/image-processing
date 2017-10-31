import uuid

from PIL import Image
import numpy as np


class ImageModel:
    """
    Base class for image models.
    Sets `self.im` from the image path path given to the constructor, and
    implements the `run` stub method, intended to be overridden.
    """
    def __init__(self, *args, **kwargs):
        # Get the image either as a keyword param or the first argument.
        image = kwargs.get('image') or args[0]
        if not image:
            raise AttributeError('No image supplied to ModelImage instance.')
        # Open the specified image and convert to greyscale.
        self.im = Image.open(image).convert('L')
        self.pixels = self.im.getdata()

    @staticmethod
    def setup():
        """
        Used to initialise a new instance of the model.
        This method should take user input (in needed) and return a model
        instance.
        """
        raise NotImplementedError

    @staticmethod
    def pixel_matrix(pixels, size):
        """
        Takes an array and a size and returns a 2D matrix of pixels of the
        specified size. Size = (rows, columns).
        """
        matrix = np.array(pixels, dtype=np.uint8)
        matrix.shape = size[1], size[0]
        return matrix

    def run(self, *args, **kwargs):
        """Should run the algorithm and return an Image instance."""
        raise NotImplementedError

    def save(self, image, name=None, ext='jpg'):
        """Takes an image and saves it to img/out/."""
        name = name or self.__class__.__name__
        uid = str(uuid.uuid4())[:5]
        image.save('img/out/{name}-{hash}.{ext}'.format(
            name=name, hash=uid, ext=ext))

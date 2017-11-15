from PIL import Image
import numpy as np
from scipy import ndimage

from src.utils.models import ImageModel
from src.utils.validation import is_gt, is_odd


class BoxBlur(ImageModel):
    def __init__(self, image, width=3, *args, **kwargs):
        super().__init__(image, *args, **kwargs)
        self.width = width

    @staticmethod
    def setup():
        try:
            width = int(input('Enter the kernel width (e.g. 3).\n'))
            _ = is_gt(width)
            _ = is_odd(width)
            return BoxBlur('img/river.jpg', width)
        except ValueError:
            return BoxBlur.setup()

    def run(self, *args, **kwargs):
        a = np.array(self.pixel_matrix(self.pixels, self.im.size))
        kernel = np.ones((self.width, self.width)) / self.width ** 2
        result = ndimage.convolve(a, kernel, mode='constant')
        self.save(Image.fromarray(result), name='boxblur-w{width}'.format(width=self.width))

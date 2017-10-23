from PIL import Image


class ImageModel:
    """
    Base class for image models.
    Sets `self.im` from the image path path given to the constructor, and
    implements the `run` stub method, intended to be overridden.
    """
    def __init__(self, image):
        # Open the specified image and convert to greyscale.
        self.im = Image.open(image).convert('L')

    @staticmethod
    def setup():
        """
        Used to initialise a new instance of the model.
        This method should get user input (in needed) and return a new Model
        instance.
        """
        raise NotImplementedError

    def run(self, *args, **kwargs):
        raise NotImplementedError

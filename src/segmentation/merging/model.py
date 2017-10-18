from PIL import Image


def setup():
    return Merging('img/river.jpg')


class Merging:
    def __init__(self, image):
        self.im = Image.open(image).convert('L')

    def run(self):
        print('Running...')
        print('Done.')

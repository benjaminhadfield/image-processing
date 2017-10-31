import math

from src.utils.models import ImageModel


class HistogramEqualiser(ImageModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.histogram = self.im.histogram()  # get the histogram
        self.L = 256  # The number of greyscale values.

    @staticmethod
    def setup():
        return HistogramEqualiser('img/river.jpg')

    def get_cumulative_histogram(self):
        ch = []
        for k, pixel_count in enumerate(self.histogram):
            ch_value = math.floor((self.L - 1) * sum(map(
                lambda x: x / (self.im.width * self.im.height),
                self.histogram[:k+1])))
            ch.append(ch_value)
        return ch
        #
        # cumulative_histogram = []
        # for (i, value) in enumerate(self.histogram):
        #     c_value = value + cumulative_histogram[i-1] if i > 0 else 0
        #     cumulative_histogram.append(c_value)
        # return cumulative_histogram

    def run(self, *args, **kwargs):
        print(self.histogram, self.get_cumulative_histogram())
        print(sum(self.histogram), sum(self.get_cumulative_histogram()))

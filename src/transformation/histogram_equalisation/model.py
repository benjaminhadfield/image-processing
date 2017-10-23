from src.utils.models import ImageModel


class HistogramEqualiser(ImageModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.histogram = self.im.histogram()

    @staticmethod
    def setup():
        return HistogramEqualiser('img/river.jpg')

    def get_cumulative_histogram(self):
        cumulative_histogram = []
        for (i, value) in enumerate(self.histogram):
            c_value = value + cumulative_histogram[i-1] if i > 0 else 0
            cumulative_histogram.append(c_value)
        return cumulative_histogram

    def run(self, *args, **kwargs):
        print(self.histogram, self.get_cumulative_histogram())

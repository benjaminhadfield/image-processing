from src.utils.models import ImageModel


class NLMeans(ImageModel):
    @staticmethod
    def setup():
        return NLMeans('img/river.jpg')

    def run(self, *args, **kwargs):
        pass

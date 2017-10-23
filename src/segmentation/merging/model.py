from src.utils.models import ImageModel


class Merging(ImageModel):
    @staticmethod
    def setup():
        return Merging('img/river.jpg')

    @staticmethod
    def _create_cost_graph(image):
        """
        Takes an Image object and returns an initialised two-dimensional graph
        representation, with all values initialised to `None`.
        """
        w, h = image.size
        pixels = image.getdata()
        # Costs is an array of edge costs between pixel `p` and it's neighbours
        # to the top, right, bottom and left. Costs are represented for each
        # pixel by the 4-tuple (top, right, bottom, left).
        costs = []
        for (i, p) in enumerate(pixels):
            tc = None if (i < w) else abs(p - pixels[i-w])
            rc = None if (i + 1) % w == 0 else abs(p - pixels[i+1])
            bc = None if (i >= len(pixels) - w) else abs(p - pixels[i+w])
            lc = None if (i % w == 0) else abs(p - pixels[i-1])
            costs.append((tc, rc, bc, lc))
        return costs

    def run(self):
        costs = self._create_cost_graph(self.im)

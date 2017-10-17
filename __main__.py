from src.segmentation.connected_components import ConnectedComponent
from src.segmentation.k_means import KMeans


if __name__ == '__main__':
    km = KMeans('img/river.jpg', 3)
    km.print_result()
    # cc = ConnectedComponent()

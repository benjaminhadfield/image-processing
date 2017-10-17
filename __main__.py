from src.segmentation.k_means.model import KMeans


if __name__ == '__main__':
    km = KMeans('img/river.jpg', 2)
    labels, centroids = km.run()
    km.print_result(labels)

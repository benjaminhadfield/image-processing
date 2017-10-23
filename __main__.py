from termcolor import colored, cprint

from src.segmentation.k_means.model import KMeans
from src.segmentation.merging.model import Merging
from src.transformation.histogram_equalisation.model import HistogramEqualiser


def run_model(options):
    print('\nAvailable models are:')
    for name in options.keys():
        cprint(' - {}'.format(name), 'magenta')
    selected = input(
        colored('\nWhich model would you like to use? ', attrs=['bold']))
    try:
        return options[selected]().run()
    except KeyError:
        cprint('Model \'{0}\' was not found. Please try a different model.'
               .format(selected), 'yellow')
        return run_model(options)


if __name__ == '__main__':
    models = {
        'k-means': KMeans.setup,
        'merging': Merging.setup,
        'hist-eq': HistogramEqualiser.setup,
    }

    _ = run_model(models)

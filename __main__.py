from termcolor import colored, cprint

from src.utils.validation import is_gt
from src.segmentation.k_means.model import KMeans
from src.segmentation.merging.model import Merging
from src.transformation.histogram_equalisation.model import HistogramEqualiser
from src.filtering.gaussian.model import Gaussian


def select_model(options):
    print('Available models are:')
    for i, option in enumerate(options):
        cprint(
            '{index} {option}'.format(index=i + 1, option=option.__name__),
            'magenta')
    choice = input(colored(
        '\nWhich model would you like to use? (1 to {}) '.format(len(options)),
        attrs=['bold']))
    try:
        # Validate selection.
        selection = int(choice)
        _ = is_gt(selection)
        # Setup and run the model.
        return options[selection - 1].setup().run()
    except (IndexError, ValueError):
        cprint(
            '\nNo model with number {}. Please try again.\n'.format(choice),
            'yellow')
        return select_model(options)


if __name__ == '__main__':
    models = (
        KMeans,
        Merging,
        HistogramEqualiser,
        Gaussian,
    )

    _ = select_model(models)

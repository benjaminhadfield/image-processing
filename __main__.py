from termcolor import colored, cprint

from src.utils.validation import is_gt
from src.segmentation.k_means.model import KMeans
from src.segmentation.merging.model import Merging
from src.transformation.histogram_equalisation.model import HistogramEqualiser
from src.filtering.box_blur.model import BoxBlur


def select_model(options):
    print('Available models are:')
    for i, option in enumerate(options):
        cprint(
            '{index} {option}'.format(index=i + 1, option=option.__name__),
            'magenta')
    _input = input(colored(
        '\nWhich model would you like to use? (1 to {}) '.format(len(options)),
        attrs=['bold']))
    try:
        # Validate selection.
        choice = int(_input)
        _ = is_gt(choice)
        # Setup and run the model.
        return options[choice - 1].setup().run()
    except (IndexError, ValueError):
        cprint(
            '\nNo model with number {}. Please try again.\n'.format(_input),
            'yellow')
        return select_model(options)


if __name__ == '__main__':
    models = (
        KMeans,
        Merging,
        HistogramEqualiser,
        BoxBlur,
    )

    _ = select_model(models)

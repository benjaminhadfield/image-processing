from termcolor import colored, cprint

from src.segmentation.k_means.model import setup as k_setup
from src.segmentation.merging.model import setup as m_setup


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
        'k-means': k_setup,
        'merging': m_setup,
    }

    _ = run_model(models)

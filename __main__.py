from src.segmentation.k_means.model import setup as k_setup


def run_model(options):
    model_names = [' - {}\n'.format(name) for name in options.keys()]
    selected = input('Which model would you like to use?\nOptions are:\n{}'
                     .format(*model_names))
    try:
        return options[selected]().run()
    except KeyError:
        print('Model \'{0}\' was not found. Please try a different model.'
              .format(selected))
        return run_model(options)


if __name__ == '__main__':
    models = {
        'k': k_setup
    }

    _ = run_model(models)

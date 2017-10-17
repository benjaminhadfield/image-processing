from src.segmentation.k_means.model import setup as k_setup


def run_model(models):
    model_name = input('What model would you like to use?\n')
    try:
        return models[model_name]().run(save_result=True)
    except KeyError:
        print('Model \'{0}\' was not found. Please enter one of:\n{1}'.format(
            model_name, *['\t- {}\n'.format(name) for name in models.keys()]))
        return run_model(models)


if __name__ == '__main__':
    models = {
        'k': k_setup
    }

    _ = run_model(models)




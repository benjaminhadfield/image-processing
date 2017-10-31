def _throw_or_return(result, throw, error=ValueError):
    """
    Takes `result` and `throw`, and returns `True` if result is `True`, else
    raises `error` if `throw` is `True`, else returns `False`.
    """
    if throw and not result:
        raise error()
    return result


def is_gt(*args, threshold=0, throw=True):
    """Checks `test` is strictly larger than `threshold`."""
    result = all([test > threshold for test in args])
    return _throw_or_return(result, throw)


def is_lt(*args, threshold=0, throw=True):
    """Checks `test` is strictly less than than `threshold`."""
    result = all([test < threshold for test in args])
    return _throw_or_return(result, throw)


def is_int(*args, throw=True):
    """Checks all args are instances of `int`."""
    result = all([isinstance(test, int) for test in args])
    return _throw_or_return(result, throw)


def is_number(*args, throw=True):
    """Checks all args are instances of `int`, `float` or `complex`."""
    result = all([isinstance(test, (int, float, complex)) for test in args])
    return _throw_or_return(result, throw)


def is_odd(*args, throw=True):
    result = all([test % 2 == 1 for test in args])
    return _throw_or_return(result, throw)

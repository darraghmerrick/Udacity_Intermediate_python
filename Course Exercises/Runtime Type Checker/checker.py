import functools

import helper


def check_types(severity=1):
    def checker(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)
        return wrapper
    return checker
+-
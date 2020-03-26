from functools import wraps
from .error import SatangProError


def check_in_kwargs(kwarg_names):
    """
    check if the wrapped function's class have the specified attributes
    :param kwarg_names: array of kwargs names to check
    :return:
    """
    def layer(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            for kwarg in kwarg_names:
                if kwarg not in kwargs:
                    raise SatangProError("{0} must be defined".format(kwarg))
            return func(self, *args, **kwargs)
        return wrapper
    return layer

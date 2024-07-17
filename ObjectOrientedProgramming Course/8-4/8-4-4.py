import functools


class returns:

    def __init__(self, datatype):
        self.allowed_datetype = datatype

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)

            if isinstance(value, self.allowed_datetype):

                return value
            else:
                raise TypeError

        return wrapper
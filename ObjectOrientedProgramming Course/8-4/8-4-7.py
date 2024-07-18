import functools


class type_check:

    def __init__(self, types: list):
        self.types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            zipper = map(lambda x: x[0] == x[1], zip(self.types, [type(i) for i in args]))

            if all(zipper):
                value = func(*args, **kwargs)
                return value
            else:
                raise TypeError

        return wrapper

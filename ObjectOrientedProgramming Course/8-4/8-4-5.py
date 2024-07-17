import functools


class exception_decorator:

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):

        try:
            value = self.func(*args, **kwargs)
            error = None
        except Exception as e:
            value = None
            error = type(e)

        return value, error
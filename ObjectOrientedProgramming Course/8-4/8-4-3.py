import functools

class takes_numbers:

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):

        args_values = [True if isinstance(i, int) or isinstance(i, float) else False for i in args]
        kwargs_values = [True if isinstance(i, int) or isinstance(i, float) else False for i in kwargs.values()]

        if all(args_values) and all(kwargs_values):
            value = self.func(*args, *[i for i in kwargs.values()])
        else:
            raise TypeError('Аргументы должны принадлежать типам int или float')

        return value
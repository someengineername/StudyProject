import functools


class ignore_exception:

    def __init__(self, *args):
        if args:
            self.exception_list = [i for i in args]
        else:
            self.exception_list = []

        # print(self.exception_list)

    def __call__(self, func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            value = None

            try:
                value = func(*args, **kwargs)
            except Exception as e:
                if type(e) in self.exception_list:
                    print(f'Исключение {type(e).__name__} обработано')
                else:
                    raise e

            return value

        return wrapper

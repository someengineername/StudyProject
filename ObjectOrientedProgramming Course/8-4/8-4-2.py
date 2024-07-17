import functools


class MaxCallsException(Exception):
    pass


class limited_calls:

    def __init__(self, n):
        self.counter = n + 1

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.counter -= 1
            if self.counter == 0:
                raise MaxCallsException('Превышено допустимое количество вызовов')

            value = func(*args, **kwargs)
            return value

        return wrapper


@limited_calls(3)
def add(a, b):
    return a + b


print(add(1, 2))
print(add(3, 4))
print(add(5, 6))

try:
    print(add())
except MaxCallsException as e:
    print(e)

class predicate:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __and__(self, other):
        return predicate(lambda *args, **kwargs: self(*args, **kwargs) and other(*args, **kwargs))

    def __or__(self, other):
        return predicate(lambda *args, **kwargs: self(*args, **kwargs) or other(*args, **kwargs))

    def __invert__(self):
        return predicate(lambda *args, **kwargs: not self(*args, **kwargs))

    def __eq__(self, other):
        return predicate(lambda *args, **kwargs: self(*args, **kwargs) == other(*args, **kwargs))

    def __lt__(self, other):
        return predicate(lambda *args, **kwargs: self(*args, **kwargs) < other(*args, **kwargs))
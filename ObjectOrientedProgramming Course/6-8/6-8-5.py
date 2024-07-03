class RandomNumber:

    def __init__(self, start, end, cache=False):
        from random import randint as rnd

        self.start = start
        self.end = end
        self.cache = cache

        if self.cache:
            self.cached_int = rnd(self.start, self.end)

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):

        if instance is None:
            return self

        from random import randint as rnd

        if self.cache:
            return self.cached_int
        else:
            return rnd(self.start, self.end)

    def __set__(self, instance, value):
        raise AttributeError('Изменение невозможно')

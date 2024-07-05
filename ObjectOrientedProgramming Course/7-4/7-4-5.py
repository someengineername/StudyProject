from collections import UserList


class NumberList(UserList):

    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []

        for pos in iterable:
            if self.is_number(pos):
                pass
            else:
                raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

        super().__init__(iterable)

    @staticmethod
    def is_number(n):
        return isinstance(n, int) or isinstance(n, float)

    def __add__(self, other):
        if isinstance(other, NumberList):
            return NumberList(self.data + other)
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def __iadd__(self, other):
        if isinstance(other, NumberList):
            return NumberList(self.data + other)
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def append(self, item):
        if self.is_number(item):
            self.data.append(item)
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def extend(self, other):

        for pos in other:
            if self.is_number(pos):
                pass
            else:
                raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

        self.data.extend(other)

    def insert(self, i, item):
        if self.is_number(item):
            self.data.insert(i, item)
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def __setitem__(self, key, value):
        if self.is_number(value):
            self.data[key] = value
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

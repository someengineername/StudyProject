from collections import UserDict


class TwoWayDict(UserDict):

    def __init__(self, iterable=None):
        if iterable is None:
            iterable = {}

        super().__init__(iterable)

    def __setitem__(self, key, value):
        self.data[key] = value
        self.data[value] = key

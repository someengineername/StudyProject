from collections import UserDict


class EasyDict(UserDict):

    def __init__(self, iterable):
        self.__dict__.update(iterable)
        super().__init__(iterable)

    def __setitem__(self, key, value):
        self.data[key] = value
        self.__dict__.update({key: value})





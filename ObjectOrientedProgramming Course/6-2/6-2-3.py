import itertools


class CyclicList:

    def __init__(self, iterable=[]):
        self.iterable = [i for i in iterable]
        self.counter = -1

    def append(self, item):
        self.iterable.append(item)

    def pop(self, item=-1):
        return self.iterable.pop(item)

    def __len__(self):
        return len(self.iterable)

    def __iter__(self):
        yield from itertools.cycle(self.iterable)

    def __getitem__(self, item):
        return self.iterable[item % len(self.iterable)]


from collections.abc import Sequence


class SortedList(Sequence):

    def __init__(self, iterable=None):
        if iterable is None:
            self.db = []
        else:
            self.db = sorted([i for i in iterable])

    def __len__(self):
        return len(self.db)

    def __getitem__(self, item):
        return self.db[item]

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __repr__(self):
        return f'SortedList({self.db})'

    def add(self, item):
        self.db.append(item)
        self.db.sort()

    def discard(self, item):
        self.db = sorted(list(filter(lambda x: x != item, self.db)))

    def update(self, iterable):
        self.db.extend(iterable)
        self.db.sort()

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return SortedList(self.db + other.db)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.db += other.db
            self.db.sort()
            return self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return SortedList(self.db * other)
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            self.db *= other
            self.db.sort()
            return self
        return NotImplemented

    def __delitem__(self, key):
        del self.db[key]
        self.db.sort()

    def append(self, obj):
        raise NotImplementedError

    def insert(self, *obj):
        raise NotImplementedError

    def extend(self, obj):
        raise NotImplementedError

    def reverse(self, obj=None):
        raise NotImplementedError

    def __reversed__(self):
        raise NotImplementedError

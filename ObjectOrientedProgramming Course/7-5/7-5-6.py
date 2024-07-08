from collections.abc import Sequence


class BitArray(Sequence):

    def __init__(self, iterable=None):
        self.db = []
        if iterable is None:
            self.db = []
        else:
            for pos in iterable:
                self.db.append(pos)

    def __len__(self):
        return len(self.db)

    def __getitem__(self, item):
        return self.db[item]

    def __repr__(self):
        return f'{self.db}'

    def __invert__(self):
        return BitArray([1 if i == 0 else 0 for i in self.db])

    def __or__(self, other):

        if isinstance(other, self.__class__):

            if len(self.db) != len(other):
                raise TypeError

            return BitArray([i[0] | i[1] for i in (zip(self.db, other))])
        return NotImplemented

    def __and__(self, other):

        if isinstance(other, self.__class__):
            if len(self.db) != len(other):
                raise TypeError

            return BitArray([i[0] & i[1] for i in (zip(self.db, other))])
        return NotImplemented

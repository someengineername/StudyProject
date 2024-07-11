class Vector:

    def __init__(self, *args):
        self.db = [i for i in args]

    def __repr__(self):
        return f'{tuple(self.db)}'

    def __add__(self, other):
        if len(self.db) == len(other.db):
            pass
        else:
            raise ValueError('Векторы должны иметь равную длину')

        if isinstance(other, self.__class__):
            if len(self.db) == len(other.db):
                return self.__class__(*[sum(i) for i in zip(self.db, other.db)])
        return NotImplemented

    def __sub__(self, other):
        if len(self.db) == len(other.db):
            pass
        else:
            raise ValueError('Векторы должны иметь равную длину')

        if isinstance(other, self.__class__):
            if len(self.db) == len(other.db):
                return self.__class__(*[i[0] - i[1] for i in zip(self.db, other.db)])
        return NotImplemented

    def __mul__(self, other):

        if len(self.db) == len(other.db):
            pass
        else:
            raise ValueError('Векторы должны иметь равную длину')

        if isinstance(other, self.__class__):
            if len(self.db) == len(other.db):
                return sum([i[0] * i[1] for i in zip(self.db, other.db)])
        return NotImplemented

    def norm(self):
        import math
        return math.sqrt(sum([i ** 2 for i in self.db]))

    def __eq__(self, other):
        if len(self.db) == len(other.db):
            return self.db == other.db
        else:
            raise ValueError('Векторы должны иметь равную длину')
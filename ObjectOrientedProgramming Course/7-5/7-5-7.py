from collections.abc import Sequence


class DNA(Sequence):

    def __init__(self, object):
        self.dna_rules = {
            "T": "A",
            "A": "T",
            "G": "C",
            "C": "G"
        }
        self.db = []

        for pos in object:
            self.db.append(pos)

    def __getitem__(self, item):
        return self.db[item], self.dna_rules[self.db[item]]

    def __len__(self):
        return len(self.db)

    def __repr__(self):
        return f'{''.join(self.db)}'

    def __contains__(self, item):
        return item in self.db

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(str(self) + str(other))
        return NotImplemented

    def __str__(self):
        return ''.join(self.db)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return str(self) == str(other)
        return NotImplemented

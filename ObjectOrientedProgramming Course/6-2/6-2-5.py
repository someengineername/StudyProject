class OrderedSet:

    def __init__(self, iterable=[]):
        self.ordered_set = list(dict.fromkeys(iterable))

    def __iter__(self):
        yield from self.ordered_set

    def __len__(self):
        return len(self.ordered_set)

    def add(self, item):
        if item not in self.ordered_set:
            self.ordered_set.append(item)

    def discard(self, item):
        if item in self.ordered_set:
            self.ordered_set.pop(self.ordered_set.index(item))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            temp1 = list(enumerate(self.ordered_set))
            temp2 = list(enumerate(other))
            return temp1 == temp2
        if isinstance(other, set):
            temp1 = set(self.ordered_set)
            return temp1 == other
        return NotImplemented
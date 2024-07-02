import random


class RandomLooper:

    def __init__(self, *args):
        self.db = []
        for pos in args:
            temp1 = iter(pos)
            for pos1 in temp1:
                self.db.append(pos1)

    def __iter__(self):
        return self

    def __next__(self):

        if len(self.db) == 0:
            raise StopIteration
        else:
            rnd_number = random.randint(0, len(self.db) - 1)
            return self.db.pop(rnd_number)
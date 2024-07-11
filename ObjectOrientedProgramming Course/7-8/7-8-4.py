class Queue:

    def __init__(self, iterable=None):

        from collections import OrderedDict

        if iterable is None:
            self.db = OrderedDict()
        if isinstance(iterable, dict):
            self.db = {k: v for k, v in iterable.items()}
        if isinstance(iterable, (list, tuple)):
            self.db = {k: v for k, v in iterable}

    def add(self, object):

        if object[0] in self.db.keys():
            del self.db[object[0]]
        self.db.setdefault(object[0], object[1])

    def pop(self):

        if self.db:
            temp_ans = next(iter(self.db.items()))
            self.db.pop(next(iter(self.db)))
            return temp_ans
        else:
            raise KeyError('Очередь пуста')

    def __repr__(self):

        return f'Queue({list((k, v) for k, v in self.db.items())})'

    def __len__(self):
        return len(self.db)
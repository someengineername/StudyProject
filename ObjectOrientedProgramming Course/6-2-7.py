class PermaDict:

    def __init__(self, input_dict=None):
        self.data = dict()
        if input_dict is not None:
            self.data.update(input_dict)

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        yield from self.data.keys()

    def keys(self):
        yield from self.data.keys()

    def values(self):
        yield from self.data.values()

    def items(self):
        yield from self.data.items()

    def __setitem__(self, key, value):

        if key in self.data.keys():
            raise KeyError('Изменение значения по ключу невозможно')
        else:
            self.data.setdefault(key, value)

    def __delitem__(self, key):
        del self.data[key]

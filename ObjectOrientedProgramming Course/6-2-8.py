class HistoryDict:

    def __init__(self, input_dict=None):
        self.data = dict()

        if input_dict is not None:

            for k, v in input_dict.items():
                self.data.setdefault(k, [v])

    def __getitem__(self, item):
        return self.data[item][-1]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        yield from self.data.keys()

    def keys(self):
        yield from self.data.keys()

    def values(self):
        temp_list = [i[-1] for i in self.data.values()]
        yield from temp_list

    def items(self):
        temp_list = [i[-1] for i in self.data.values()]
        yield from zip(self.data.keys(), temp_list)

    def __setitem__(self, key, value):

        if key in self.data.keys():

            self.data[key].append(value)
        else:
            self.data.setdefault(key, [value])

    def __delitem__(self, key):
        del self.data[key]

    def history(self, item):
        if item in self.data.keys():
            return self.data[item]
        return []

    def all_history(self):
        return self.data
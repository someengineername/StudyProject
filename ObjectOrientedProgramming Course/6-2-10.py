from itertools import groupby


class Grouper:

    def __init__(self, iterable, key):
        self.key_storage = key
        self.init_list_sorted_by_key = sorted(list(iterable), key=self.key_storage)
        self.data = {k: list(v) for k, v in groupby(self.init_list_sorted_by_key, self.key_storage)}

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        yield from [(k, v) for k, v in self.data.items()]

    def __contains__(self, item):
        return item in self.data

    def __getitem__(self, item):
        return self.data[item]

    def add(self, other):

        presumed_key = self.key_storage(other)

        if presumed_key in self.data.keys():
            self.data[presumed_key].append(other)
        else:
            self.data.setdefault(presumed_key, [other])

    def group_for(self, some_object):
        return self.key_storage(some_object)

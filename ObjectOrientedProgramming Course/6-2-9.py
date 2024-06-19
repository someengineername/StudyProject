class MutableString:

    def __init__(self, input_string=None):
        if input_string is None:
            self.data = []
        else:
            self.data = [i for i in input_string]

    def lower(self):
        self.data = list(map(str.lower, self.data))

    def upper(self):
        self.data = list(map(str.upper, self.data))

    def __iter__(self):
        yield from self.data

    def __str__(self):
        return ''.join(self.data)

    def __repr__(self):
        return f"MutableString('{''.join(self.data)}')"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.__str__() + other.__str__())
        raise NotImplemented

    def __setitem__(self, key, value):

        if isinstance(key, slice):
            if key.start >= 0:
                first_half = self.data[:key.start]
                self.data = first_half + list(value)
            else:
                first_half = self.data[:key.start + 1]
                self.data = first_half + list(value)
        else:
            self.data[key] = value

    def __getitem__(self, item):
        if isinstance(item, slice):
            return self.__class__(''.join(self.data[item]))
        else:
            return self.__class__(str(self.data[item]))

    def __delitem__(self, key):
        if isinstance(key, slice):
            del self.data[key]
        else:
            del self.data[key]

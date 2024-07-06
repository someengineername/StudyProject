from collections import UserString


class MutableString(UserString):

    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, key=None, reverse=None):
        self.data = ''.join(sorted(self.data, key=key, reverse=reverse))

    def __getitem__(self, item):
        return self.data[~item]

    def __setitem__(self, key, value):
        temp_value = list(self.data)
        temp_value[key] = value
        self.data = ''.join(temp_value)

    def __delitem__(self, key):
        temp_value = list(self.data)
        del temp_value[key]
        self.data = ''.join(temp_value)

class SparseArray:

    def __init__(self, default=0):
        self.default = default
        self.db = dict()

    def __setitem__(self, key, value):
        self.db[key] = value

    def __getitem__(self, item):
        return self.db.get(item, self.default)


array = SparseArray(None)

array[0] = 'Timur'
array[1] = 'Arthur'

print(array[0])
print(array[1])
print(array[2])
class ModularTuple(tuple):

    def __new__(cls, iterable=(), size=100):
        temp_list = [i % size for i in iterable]

        instance = super().__new__(cls, tuple(temp_list))
        return instance

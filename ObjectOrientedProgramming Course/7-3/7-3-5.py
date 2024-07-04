class SuperInt(int):

    def repeat(self, n=2):
        return self.__class__(str(self) * n if self > 0 else str(self) + str(abs(self)) * (n - 1))

    def to_bin(self):
        return format(self, 'b')

    def next(self):
        return self.__class__(self + 1)

    def prev(self):
        return self.__class__(self - 1)

    def __iter__(self):
        temp_list = [self.__class__(i) for i in str(abs(self))]
        yield from temp_list

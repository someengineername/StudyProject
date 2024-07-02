class Peekable:
    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.index = -1

    def peek(self, default=StopIteration):
        try:
            return self.iterable[self.index + 1]
        except:
            if default == StopIteration:
                raise default
            else:
                return default

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.iterable):
            raise StopIteration
        return self.iterable[self.index]
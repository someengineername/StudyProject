class AttrsIterator:
    def __init__(self, obj):
        self.obj = obj
        self.data = [(k, v) for k, v in self.obj.__dict__.items()]
        self.pos = -1

    def __next__(self):
        self.pos += 1
        if self.pos >= len(self.data):
            raise StopIteration
        else:
            return self.data[self.pos]

    def __iter__(self):
        return self


class Kish:
    def __init__(self, song, year):
        self.song = song
        self.year = year


forester = Kish('лесник', 1997)
attrs_iterator = AttrsIterator(forester)

next(attrs_iterator)
next(attrs_iterator)

try:
    next(attrs_iterator)
except StopIteration:
    print('Атрибуты закончились')
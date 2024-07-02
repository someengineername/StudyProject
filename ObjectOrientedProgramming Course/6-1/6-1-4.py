class SkipIterator:

    def __init__(self, iterable, n):
        self.iterable = iter(iterable)
        self.n = n
        self.counter = 0

        if self.n == 0:
            self.temp_bucket1 = self.iterable
        else:
            self.temp_bucket = []
            for pos in self.iterable:

                if self.counter == 0:
                    self.temp_bucket.append(pos)
                    self.counter += 1
                elif self.counter == self.n:
                    self.counter = 0
                elif self.counter < self.n:
                    self.counter += 1

            self.temp_bucket1 = iter(self.temp_bucket)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.temp_bucket1)

class Counter:

    def __init__(self, start=0):
        self.value = start

    def inc(self, n=None):
        if n is None:
            self.value += 1
        else:
            self.value += n

    def dec(self, n=None):
        if n is None:
            self.value -= 1
        else:
            self.value -= n

        if self.value < 0:
            self.value = 0


class NonDecCounter(Counter):

    def dec(self, n=None):
        pass


class LimitedCounter(Counter):

    def __init__(self, start=0, limit=10):
        Counter.__init__(self, start=start)
        self.limit = limit

    def inc(self, n=None):
        if n is None:
            self.value += 1
        else:
            self.value += n

        if self.value > self.limit:
            self.value = self.limit

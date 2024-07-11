class ArithmeticProgression:

    def __init__(self, base=0, step=1):
        self.base = base
        self.step = step

    def __iter__(self):
        yield self.base

        while ...:
            self.base += self.step
            yield self.base


class GeometricProgression:

    def __init__(self, base, step):
        self.base = base
        self.step = step

    def __iter__(self):
        yield self.base

        while ...:
            self.base *= self.step
            yield self.base

class AdvancedTuple(tuple):

    def __add__(self, other):

        if '__iter__' in dir(other):
            return AdvancedTuple(list(self) + list(other))
        return NotImplemented

    def __radd__(self, other):

        if '__iter__' in dir(other):
            return AdvancedTuple(list(other) + list(self))
        return NotImplemented

    def __iadd__(self, other):
        if '__iter__' in dir(other):
            return AdvancedTuple(list(self) + list(other))
        return NotImplemented
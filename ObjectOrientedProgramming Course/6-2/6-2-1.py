class ReversedSequence:

    def __init__(self, sequence):
        self.reversed_sequence = sequence

    def __len__(self):
        return len(self.reversed_sequence)

    def __iter__(self):
        yield from reversed(self.reversed_sequence)

    def __getitem__(self, item):
        return self.reversed_sequence[-item - 1]

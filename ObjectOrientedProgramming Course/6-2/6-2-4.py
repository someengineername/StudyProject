import copy


class SequenceZip:

    def __init__(self, *args):
        self.result_db = copy.deepcopy(args)

    def __iter__(self):
        yield from zip(*((x for x in i) for i in self.result_db))

    def __len__(self):
        final_destination = 0
        for pos in zip(*((x for x in i) for i in self.result_db)):
            final_destination += 1
        return final_destination

    def __getitem__(self, item):
        final_destination = -1

        for pos in zip(*((x for x in i) for i in self.result_db)):
            final_destination += 1
            if final_destination == item:
                return pos

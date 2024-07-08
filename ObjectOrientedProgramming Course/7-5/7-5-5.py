from collections.abc import Sequence


class CustomRange(Sequence):

    def __init__(self, *args):

        self.db = []

        for pos in args:
            if isinstance(pos, int):
                self.db.append(pos)
            if isinstance(pos, str):
                templine = [int(i) for i in pos.split('-')]
                templist = [i for i in range(templine[0], templine[1] + 1)]
                self.db.extend(templist)

    def __getitem__(self, item):
        return self.db[item]

    def __len__(self):
        return len(self.db)
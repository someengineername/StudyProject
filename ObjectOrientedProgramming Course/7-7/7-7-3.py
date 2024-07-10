from abc import ABC, abstractmethod


class Paragraph:

    def __init__(self, par_len):
        self.par_len = par_len
        self.temp_str_storage = []

    def add(self, str_input):
        self.temp_str_storage.append(str_input)

    @abstractmethod
    def end(self):
        pass


class LeftParagraph(Paragraph):

    def end(self):

        final_db = []
        temp_res = []

        for pos in ' '.join(self.temp_str_storage).split(' '):
            temp_res.append(pos)
            if sum(list(map(lambda x: len(x), temp_res))) + len(temp_res) - 1 > self.par_len:
                final_db.append(temp_res[:-1])
                temp_res = [pos]

        final_db.append(temp_res)

        for pos in final_db:
            print(' '.join(pos))

        self.temp_str_storage = []


class RightParagraph(Paragraph):

    def end(self):
        final_db = []
        self.temp_res = []

        for pos in ' '.join(self.temp_str_storage).split(' '):
            self.temp_res.append(pos)
            if sum(list(map(lambda x: len(x), self.temp_res))) + len(self.temp_res) - 1 > self.par_len:
                final_db.append(self.temp_res[:-1])
                self.temp_res = [pos]

        final_db.append(self.temp_res)

        for pos in final_db:
            print(' '.join(pos).rjust(self.par_len))

        self.temp_str_storage = []
        self.temp_res = []


leftparagraph = LeftParagraph(23)

leftparagraph.add('Multiply noise and joy')
leftparagraph.add('Sing songs in a good hour')
leftparagraph.add('Friendship grace and youth')
leftparagraph.add('Our birthday girls')
leftparagraph.end()

leftparagraph.add('Meanwhile the winged child')
leftparagraph.add('friends greeting you')
leftparagraph.add('Secretly thinks sometime')
leftparagraph.add('I will be the birthday boy')
leftparagraph.end()

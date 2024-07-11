class CaesarCipher:

    def __init__(self, shift=1):
        self.shift = shift
        self.dict_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.dict_lower = 'abcdefghijklmnopqrstuvwxyz'

    def encode(self, input_string):

        temp_answer = []

        for pos in [i for i in input_string]:
            if pos in self.dict_lower:
                new_index = (self.dict_lower.index(pos) + self.shift) % 26
                temp_answer.append(self.dict_lower[new_index])
            elif pos in self.dict_upper:
                new_index = (self.dict_upper.index(pos) + self.shift) % 26
                temp_answer.append(self.dict_upper[new_index])
            else:
                temp_answer.append(pos)

        return ''.join(temp_answer)

    def decode(self, input_string):

        temp_answer = []

        for pos in [i for i in input_string]:
            if pos in self.dict_lower:
                new_index = (self.dict_lower.index(pos) - self.shift) % 26
                temp_answer.append(self.dict_lower[new_index])
            elif pos in self.dict_upper:
                new_index = (self.dict_upper.index(pos) - self.shift) % 26
                temp_answer.append(self.dict_upper[new_index])
            else:
                temp_answer.append(pos)

        return ''.join(temp_answer)





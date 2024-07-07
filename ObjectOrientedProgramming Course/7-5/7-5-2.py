from abc import ABC, abstractmethod


class ChessPiece(ABC):

    def __init__(self, hor, ver):
        self.conversion_matrix = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        self.horizontal = hor
        self.vertical = ver

    @abstractmethod
    def can_move(self, to_hor, to_ver):
        pass

    def in_field(self, hor, ver):
        return 1 <= hor <= 8 and 1 <= ver <= 8


class King(ChessPiece):

    def can_move(self, char_hor, destination_ver):
        possible_moves = [
            [self.conversion_matrix[self.horizontal] - 1, self.vertical - 1],
            [self.conversion_matrix[self.horizontal], self.vertical - 1],
            [self.conversion_matrix[self.horizontal] + 1, self.vertical - 1],
            [self.conversion_matrix[self.horizontal] - 1, self.vertical],
            [self.conversion_matrix[self.horizontal] + 1, self.vertical],
            [self.conversion_matrix[self.horizontal] - 1, self.vertical + 1],
            [self.conversion_matrix[self.horizontal], self.vertical + 1],
            [self.conversion_matrix[self.horizontal] + 1, self.vertical + 1]
             ]

        if ([self.conversion_matrix[char_hor], destination_ver] in possible_moves and
                self.in_field(self.conversion_matrix[char_hor], destination_ver)):
            return True
        return False


class Knight(ChessPiece):

    def can_move(self, to_hor, to_ver):
        possible_moves = [
            [self.conversion_matrix[self.horizontal] + 2, self.vertical + 1],
            [self.conversion_matrix[self.horizontal] + 2, self.vertical - 1],
            [self.conversion_matrix[self.horizontal] - 2, self.vertical + 1],
            [self.conversion_matrix[self.horizontal] - 2, self.vertical - 1],
            [self.conversion_matrix[self.horizontal] + 1, self.vertical + 2],
            [self.conversion_matrix[self.horizontal] + 1, self.vertical - 2],
            [self.conversion_matrix[self.horizontal] - 1, self.vertical + 2],
            [self.conversion_matrix[self.horizontal] - 1, self.vertical - 2]
        ]

        if ([self.conversion_matrix[to_hor], to_ver] in possible_moves and
                self.in_field(self.conversion_matrix[to_hor], to_ver)):
            return True
        return False

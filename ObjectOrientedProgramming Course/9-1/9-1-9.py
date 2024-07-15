class TicTacToe:
    def __init__(self):
        self.game_board = [[None for i in range(3)] for j in range(3)]
        self.step = 0
        self.marker = 'O'

    def show(self):
        counter = 0
        for line in self.game_board:
            print('|'.join([str(i) if i != None else ' ' for i in line]))
            if counter < 2:
                print('-----')
            counter += 1

    def mark(self, x, y):

        # check if we have a winner

        if self.is_winner_present() or self.step == 9:
            print('Игра окончена')
        else:

            # check if place is free and place a marker

            if self.game_board[x - 1][y - 1] is None:

                if self.marker == 'O':
                    self.marker = 'X'
                else:
                    self.marker = 'O'

                self.game_board[x - 1][y - 1] = self.marker
                self.step += 1

            # if place is hold - just skip

            else:
                print('Недоступная клетка')

    def is_winner_present(self):

        line1 = self.game_board[0]
        line2 = self.game_board[1]
        line3 = self.game_board[2]
        line4 = [self.game_board[0][0], self.game_board[1][0], self.game_board[2][0]]
        line5 = [self.game_board[0][1], self.game_board[1][1], self.game_board[2][1]]
        line6 = [self.game_board[0][2], self.game_board[1][2], self.game_board[2][2]]
        line7 = [self.game_board[0][0], self.game_board[1][1], self.game_board[2][2]]
        line8 = [self.game_board[2][0], self.game_board[1][1], self.game_board[0][2]]

        lines = [line1, line2, line3, line4, line5, line6, line7, line8]

        for line in lines:
            if self.all_equal(line):
                return line[0]
        return None

    def all_equal(self, iterator):
        iterator = iter(iterator)
        try:
            first = next(iterator)
        except StopIteration:
            return True
        return all(first == x for x in iterator)

    def winner(self):

        result = self.is_winner_present()

        # check if all turn are done

        if self.step == 9:

            if result is not None:
                return result
            else:
                return 'Ничья'

        # if turns lower than 9 (so game likely not finished - to check for winner)
        else:

            # check for winner - if have one - return it
            if result is not None:
                return result
            # if no winner detected - return None
            else:
                return 'None'
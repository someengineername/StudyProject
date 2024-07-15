from random import randint as rnd


class Game:

    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[None for j in range(self.cols)] for i in range(self.rows)]
        self.fill_with_cells()

    def fill_with_cells(self):

        counter_mine = 0

        # fill with basic Cell

        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i][j] = Cell(i, j)

        # ararnge mines (with rnd) and skipping already mined Cells

        while counter_mine < self.mines:
            rnd1 = rnd(0, self.rows - 1)
            rnd2 = rnd(0, self.cols - 1)

            if self.board[rnd1][rnd2].mine:
                pass
            else:
                self.board[rnd1][rnd2].mine = True
                counter_mine += 1

        # self.board[0][0].mine = True

        # filling neighbours attribute

        for i in range(self.rows):
            for j in range(self.cols):

                shifting_list = [[-1, -1], [-1, 0], [-1, 1],
                                 [0, -1], [0, 1],
                                 [1, -1], [1, 0], [1, 1]]
                neighbours_mines = 0

                for pos in shifting_list:
                    x_coor = i + pos[0]
                    y_coor = j + pos[1]

                    if 0 <= x_coor < self.rows and 0 <= y_coor < self.cols:
                        if self.board[x_coor][y_coor].mine:
                            neighbours_mines += 1
                        else:
                            continue

                self.board[i][j].neighbours = neighbours_mines

        # some nested list magic
        # temp_list = [a.mine for x in self.board for a in x]

    def print_field(self):

        for line in self.board:
            print(' '.join(str(i) for i in line))


class Cell:

    def __init__(self, x: int, y: int, mine=False) -> None:
        self.row = x
        self.col = y
        self.mine = mine
        self.neighbours = 0

    def __repr__(self):
        dict1 = {'0': '✳️', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣', '4': '4️⃣', '5': '5️⃣', '6': '6️⃣', '7': '8️⃣'}
        return f'{"🔴" if self.mine else "⚪"}{dict1[str(self.neighbours)]}'
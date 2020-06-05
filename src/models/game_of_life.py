from random import choices


class GameOfLife:
    def __init__(self, size=10, board=None):
        if board:
            self.board = board
            self.size = len(self.board)
        else:
            self.size = size
            self.board = [[False for i in range(self.size)]
                          for j in range(self.size)]

    @property
    def board(self):
        return self.__board

    @board.getter
    def board(self):
        return self.__board

    @board.setter
    def board(self, values):
        self.__board = []
        for i, row in enumerate(values):
            self.__board.append([])
            for j, col in enumerate(row):
                if isinstance(col, dict):
                    self.__board[i].append(col)
                else:
                    self.__board[i].append(dict(i=i, j=j, alive=col))

    def random(self, weights=[.1, .9]):
        self.board = [choices([True, False], weights=weights, k=self.size)
                      for _ in range(self.size)]

    def __getitem__(self, ij):
        i, j = ij
        return self.board[i][j]

    def __setitem__(self, ij, value):
        i, j = ij
        self.board[i][j] = {
            'i': i,
            'j': j,
            'alive': value
        }

    def neighbor_list(self, i, j):
        return (self[i + di, j + dj]
                for di, dj in [(-1, -1), (0, -1), (1, -1), (-1, 0), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
                if i + di in range(self.size) and j + dj in range(self.size))

    def neighbors(self, i, j, alive=None):
        return list(filter(lambda n: alive is None or n['alive'] == alive, self.neighbor_list(i, j)))

    def alive_neighbors(self, i, j):
        return len(self.neighbors(i, j, True))

    def dead_neighbors(self, i, j):
        return len(self.neighbors(i, j, False))

    def alive(self, i, j):
        return self[i, j]['alive']

    def dead(self, i, j):
        return not self[i, j]['alive']

    def lives(self, i, j):
        if self[i, j]:
            if self.alive_neighbors(i, j) in [2, 3]:
                return True
            else:
                return False
        else:
            if self.alive_neighbors(i, j) == 3:
                return True
            else:
                return False

    def evolve(self):
        print(self.size)
        self.board = [[self.lives(i, j) for i in range(self.size)]
                      for j in range(self.size)]

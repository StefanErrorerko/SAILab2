import itertools
import random
import math


class Puzzle:
    def __init__(self, board):
        self.scale = len(board[0])
        self.board = board

    @property
    def if_solved(self):
        n = self.scale * self.scale
        """
        Solved if each chip is placed in increasing row and '0' is at the end 
        """
        return str(self) == ''.join(map(str, range(1, n))) + '0'

    @property 
    def actions(self):
        """
        Return a list of 'move', 'action' pairs. 'move' can be called
        to return a new puzzle that results in sliding the '0' tile in
        the direction of 'action'.
        """
        def create_move(at, to):
            return lambda: self._move(at, to)

        moves = []
        for i, j in itertools.product(range(self.scale),
                                      range(self.scale)):
            dirs = {'R': (i, j-1),
                    'L': (i, j+1),
                    'D': (i-1, j),
                    'U': (i+1, j)}

            for action, (r, c) in dirs.items():
                if 0 <= r < self.scale and 0 <= c < self.scale and \
                   self.board[r][c] == 0:
                    move = create_move((i,j), (r,c)), action
                    moves.append(move)
        return moves

    """
    @property
    def manhattan(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    x, y = divmod(self.board[i][j]-1, 3)
                    distance += abs(x - i) + abs(y - j)
        return distance
    """

    @property
    def false_amount(self):
        amount = 0
        goal_board = [[1,2,3], [4,5,6], [7,8,0]]
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != goal_board[i][j]:
                    amount += 1
        return amount

    def shuffle(self):
        puzzle = self
        for _ in range(1000):
            puzzle = random.choice(self.actions)[0]()
        return puzzle

    def _move(self, at, to):
        """
        Makes move
        """
        new_board = []
        for row in self.board:
            new_board.append([x for x in row])
        puzzle = Puzzle(new_board)
        i, j = at
        r, c = to
        puzzle.board[i][j], puzzle.board[r][c] = puzzle.board[r][c], puzzle.board[i][j]
        return puzzle

    def print_board(self):
        for row in self.board:
            print(row)

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.board:
            yield from row
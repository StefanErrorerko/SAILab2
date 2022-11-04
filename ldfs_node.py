from puzzle import Puzzle

class LDFSNode:
    def __init__(self, board, parent = None,
                 left_node = None, right_node = None, number  = None, full = None):
        self.board = board
        self.parent = parent
        self.left_node = left_node
        self.right_node = right_node
        self.number = number
        self.full = full or False

    def is_full(self):
        return self.left_node is not None and self.right_node is not None

    def if_solved(self):
        puzzle = Puzzle(self.board)
        return puzzle.if_solved


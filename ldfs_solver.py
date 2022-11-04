import copy
from ldfs_node import LDFSNode
from puzzle import Puzzle

class LDFSSolver:
    def __init__(self, init_board):
        self.current_node = LDFSNode(init_board.board)
        self.max_depth = int(10)
        self.width = len(init_board.board[0])
        self.stack = []
        self.visited = []

    # finds position of blank space (number 0)
    def find_pos(self):
        for i in range(self.width):
            for j in range(self.width):
                if self.current_node.board[i][j] == 0:
                    return [i, j]


    # moves blank space up
    def up(self):
        pos = self.find_pos()
        i, j = pos[0],  pos[1]
        if i > 0:
            temp = copy.deepcopy(self.current_node.board)
            temp[i][j] = temp[i - 1][j]
            temp[i - 1][j] = 0
            return temp
        else:
            return self.current_node.board


    # moves blank space down
    def down(self):
        pos = self.find_pos()
        i, j = pos[0],  pos[1]
        if i < self.width - 1:
            temp = copy.deepcopy(self.current_node.board)
            temp[i][j] = temp[i + 1][j]
            temp[i + 1][j] = 0
            return temp
        else:
            return self.current_node.board


    # moves blank space left
    def left(self):
        pos = self.find_pos()
        i, j = pos[0],  pos[1]
        if j > 0:
            temp = copy.deepcopy(self.current_node.board)
            temp[i][j] = temp[i][j - 1]
            temp[i][j - 1] = 0
            return temp
        else:
            return self.current_node.board


    # moves blank space right
    def right(self):
        pos = self.find_pos()
        i, j = pos[0], pos[1]
        if j < self.width - 1:
            temp = copy.deepcopy(self.current_node.board)
            temp[i][j] = temp[i][j + 1]
            temp[i][j + 1] = 0
            return temp
        else:
            return self.current_node.board


    # DLS (LDFS) FUNCTION
    def solve(self):
        self.current_node.number = 1
        self.stack.append(self.current_node)
        self.visited.append(self.current_node.board)

        k = int(1)

        while len(self.stack) != 0:
            self.current_node = self.stack[-1]
            if self.current_node.if_solved():
                return self.visited
            k += 1
            if len(self.stack) <= self.max_depth and not self.current_node.is_full():
                # Realization of informative search to DLS (wrong)
                """
                variants = [9, 9, 9, 9]
                if self.find_pos()[1] != 0 and self.left() not in self.visited:
                    p = self.left()
                    variants[0] = Puzzle(self.left()).false_amount
                if self.find_pos()[0] != 0 and self.up() not in self.visited and not self.current_node.is_full():
                    x = self.up()
                    variants[1] = Puzzle(self.up()).false_amount
                if self.find_pos()[1] != (self.width - 1) and self.right() not in self.visited and not self.current_node.is_full():
                    y = self.right()
                    variants[2] = Puzzle(self.right()).false_amount
                if self.find_pos()[0] != (self.width - 1) and self.down() not in self.visited and not self.current_node.is_full():
                    f = self.down()
                    variants[3] = Puzzle(self.down()).false_amount
        
                min = 0
                for i in range(len(variants)):
                    if variants[i] < variants[min]:
                        min = i
                """
                # if 1) we can move right; 2) move right was not done earlier; 3) we can add a child to a node (<2 moves from node done:
                if (self.find_pos()[1] != (self.width - 1)
                        and self.right() not in self.visited
                        and not self.current_node.is_full()):
                #if min == 2:
                    if self.current_node.left_node is None:
                        self.current_node.left_node = LDFSNode(self.right())
                        self.current_node.left_node.parent = self.current_node
                        self.current_node.left_node.number = k
                        self.stack.append(self.current_node.left_node)
                        self.visited.append(self.current_node.left_node.board)
                    else:
                        self.current_node.right_node = LDFSNode(self.right())
                        self.current_node.right_node.parent = self.current_node
                        self.current_node.right_node.number = k
                        self.stack.append(self.current_node.right_node)
                        self.visited.append(self.current_node.right_node.board)
                # if 1) we can move down; 2) move down was not done earlier; 3) we can add a child to a node (<2 moves from node done:
                elif (self.find_pos()[0] != (self.width - 1)
                        and self.down() not in self.visited
                        and not self.current_node.is_full()):
                #elif min == 3:
                    if self.current_node.left_node is None:
                        self.current_node.left_node = LDFSNode(self.down())
                        self.current_node.left_node.parent = self.current_node
                        self.current_node.left_node.number = k
                        self.stack.append(self.current_node.left_node)
                        self.visited.append(self.current_node.left_node.board)
                    else:
                        self.current_node.right_node = LDFSNode(self.down())
                        self.current_node.right_node.parent = self.current_node
                        self.current_node.right_node.number = k
                        self.stack.append(self.current_node.right_node)
                        self.visited.append(self.current_node.right_node.board)
                # if 1) we can move left; 2) move left was not done earlier; 3) we can add a child to a node (<2 moves from node done:
                elif (self.find_pos()[1] != 0
                    and self.left() not in self.visited
                    and not self.current_node.is_full()):
                    # if min == 0:
                    if self.current_node.left_node is None:
                        self.current_node.left_node = LDFSNode(self.left())
                        self.current_node.left_node.parent = self.current_node
                        self.current_node.left_node.number = k
                        self.stack.append(self.current_node.left_node)
                        self.visited.append(self.current_node.left_node.board)
                    else:
                        self.current_node.right_node = LDFSNode(self.left())
                        self.current_node.right_node.parent = self.current_node
                        self.current_node.right_node.number = k
                        self.stack.append(self.current_node.right_node)
                        self.visited.append(self.current_node.right_node.board)
                # if 1) we can move up; 2) move up was not done earlier; 3) we can add a child to a node (<2 moves from node done:
                elif (self.find_pos()[0] != 0
                      and self.up() not in self.visited
                      and not self.current_node.is_full()):
                    # elif min == 1:
                    if self.current_node.left_node is None:
                        self.current_node.left_node = LDFSNode(self.up())
                        self.current_node.left_node.parent = self.current_node
                        self.current_node.left_node.number = k
                        self.stack.append(self.current_node.left_node)
                        self.visited.append(self.current_node.left_node.board)
                    else:
                        self.current_node.right_node = LDFSNode(self.up())
                        self.current_node.right_node.parent = self.current_node
                        self.current_node.right_node.number = k
                        self.stack.append(self.current_node.right_node)
                        self.visited.append(self.current_node.right_node.board)
                else:
                    self.stack.pop(-1)
            else:
                self.stack.pop(-1)
        return self.visited

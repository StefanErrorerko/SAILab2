import time
import  matplotlib.pyplot as plt

from puzzle import Puzzle
from ldfs_solver import LDFSSolver
from astar_solver import AstarSolver

time1 = []
time2 = []
state1 = []
state2 = []

board = [[0,2,3],[1,8,5],[4,7,6]]
puzzle = Puzzle(board)
for i in range(20):
    puzzle = puzzle.shuffle()
    ast_slv = AstarSolver(puzzle)
    ldfs_slv = LDFSSolver(puzzle)

    tic1 = time.time()
    slv_puzzle1 = ast_slv.solve()
    toc1 = time.time()

    time1.append(toc1 - tic1)
    steps = 0
    for smth in slv_puzzle1:
        steps += 1
    state1.append(steps)

    tic2= time.time()
    slv_puzzle2 = ldfs_slv.solve()
    toc2 = time.time()

    time2.append(toc2 - tic2)
    state2.append(len(slv_puzzle2))

print("Average number of steps for A*: " + str(sum(state1) / 20))
print("Average number of steps for LDFS: " + str(sum(state2) / 20))

plt.plot(range(1, 21), state1)
plt.show()
plt.plot(range(1, 21), state2)
plt.show()

print("Average time for computing: " + str(sum(time1) / 20) + "s")
print("Average time for computing: " + str(sum(time2) / 20) + "s")

plt.plot(range(1, 21), time1)
plt.show()
plt.plot(range(1, 21), time2)
plt.show()

print(state1)
print(state2)
print(time1)
print(time2)
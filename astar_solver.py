import collections
from astar_node import AstarNode


class AstarSolver:
    def __init__(self, init_board):
        self.init_board = init_board

    def solve(self):
        queue = collections.deque([AstarNode(self.init_board)])
        seen = set()
        seen.add(queue[0].state)
        while queue:
            queue = collections.deque(sorted(list(queue), key=lambda node: node.f))
            node = queue.popleft()
            if node.if_solved:
                return node.path

            for move, action in node.actions:
                child = AstarNode(move(), node, action)

                if child.state not in seen:
                    queue.appendleft(child)
                    seen.add(child.state)
from pythonProject.AI.searching_framework.utils import Problem
from pythonProject.AI.searching_framework.informed_search import *


class Ghost_OnSkates(Problem):
    def __init__(self, initial, walls, n, goal=None):
        super(Ghost_OnSkates, self).__init__(initial, goal)
        self.walls = walls
        self.n = n

    @staticmethod
    def check_valid(state, walls, n):
        x_pos = state[0]
        y_pos = state[1]

        if x_pos >= n or y_pos >= n or (x_pos, y_pos) in walls:
            return False
        return True

    def successor(self, state):
        successors = dict()

        x_pos = state[0]
        y_pos = state[1]


        # move up by 1
        if Ghost_OnSkates.check_valid((x_pos, y_pos + 1), self.walls, self.n) == True:
            successors["Gore 1"] = (x_pos, y_pos + 1)

        # move up by 2
        if Ghost_OnSkates.check_valid((x_pos, y_pos + 2), self.walls, self.n) == True:
            successors["Gore 2"] = (x_pos, y_pos + 2)

        # move up by 3
        if Ghost_OnSkates.check_valid((x_pos, y_pos + 3), self.walls, self.n) == True:
            successors["Gore 3"] = (x_pos, y_pos + 3)

        # move right by 1
        if Ghost_OnSkates.check_valid((x_pos + 1, y_pos), self.walls, self.n) == True:
            successors["Desno 1"] = (x_pos + 1, y_pos)

        # move right by 2
        if Ghost_OnSkates.check_valid((x_pos + 2, y_pos), self.walls, self.n) == True:
            successors["Desno 2"] = (x_pos + 2, y_pos)

        # move right by 3
        if Ghost_OnSkates.check_valid((x_pos + 3, y_pos), self.walls, self.n) == True:
            successors["Desno 3"] = (x_pos + 3, y_pos)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        x1_pos, y1_pos = node.state
        x2_pos, y2_pos = self.goal

        dist = abs(x1_pos - x2_pos) + abs(y1_pos - y2_pos)

        return dist/3

    def goal_test(self, state):
        return state[0] == self.goal[0] and state[1] == self.goal[1]


if __name__ == '__main__':
    n = int(input())
    ghost_pos = (0, 0)
    goal_pos = (n - 1, n - 1)

    num_holes = int(input())
    holes = list()
    for _ in range(num_holes):
        holes.append(tuple(map(int, input().split(','))))

    problem = Ghost_OnSkates(ghost_pos, holes, n, goal_pos)

    result = astar_search(problem)

    print(result.solution())

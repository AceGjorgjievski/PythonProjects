from pythonProject.AI.searching_framework.utils import Problem
from pythonProject.AI.searching_framework.uninformed_search import *


def move_right(x, y, o_x, o_y, h2_x, h2_y, obs):
    while x < 8 and [x + 1, y] != [o_x, o_y] and [x + 1, y] != [h2_x, h2_y] and [x + 1, y] not in obs:
        x += 1
    return x


def move_left(x, y, o_x, o_y, h2_x, h2_y, obs):
    while x > 0 and [x - 1, y] != [o_x, o_y] and [x - 1, y] != [h2_x, h2_y] and [x - 1, y] not in obs:
        x -= 1
    return x


def move_up(x, y, o_x, o_y, h2_x, h2_y, obs):
    while y < 6 and [x, y + 1] != [o_x, o_y] and [x, y + 1] != [h2_x, h2_y] and [x, y + 1] not in obs:
        y += 1
    return y


def move_down(x, y, o_x, o_y, h2_x, h2_y, obs):
    while y > 0 and [x, y - 1] != [o_x, o_y] and [x, y - 1] != [h2_x, h2_y] and [x, y - 1] not in obs:
        y -= 1
    return y


class Molecule(Problem):
    def __init__(self, initial, obstacles, goal=None):
        super(Molecule, self).__init__(initial, goal)
        self.grid_size = [8, 7]
        self.obstacles = obstacles

    def successor(self, state):
        successors = {}

        h1_x = state[0]
        h1_y = state[1]

        o_x = state[2]
        o_y = state[3]

        h2_x = state[4]
        h2_y = state[5]

        obstacles = self.obstacles

        # H0
        new_x = move_right(h1_x, h1_y, o_x, o_y, h2_x, h2_y, obstacles)
        # (h1[0], h1[1], o[0], o[1], h2[0], h2[1], obstacles_list)
        if new_x != h1_x:
            successors["H1 - Right"] = (new_x, h1_y, o_x, o_y, h2_x, h2_y)

        new_x = move_left(h1_x, h1_y, o_x, o_y, h2_x, h2_y, obstacles)
        if new_x != h1_x:
            successors["H1 - Left"] = (new_x, h1_y, o_x, o_y, h2_x, h2_y)

        new_y = move_up(h1_x, h1_y, o_x, o_y, h2_x, h2_y, obstacles)
        if new_y != h1_y:
            successors["H1 - Up"] = (h1_x, new_y, o_x, o_y, h2_x, h2_y)

        new_y = move_down(h1_x, h1_y, o_x, o_y, h2_x, h2_y, obstacles)
        if new_y != h1_y:
            successors["H1 - Down"] = (h1_x, new_y, o_x, o_y, h2_x, h2_y)

        # O
        new_x = move_right(o_x, o_y, h1_x, h1_y, h2_x, h2_y, obstacles)
        # (h1[0], h1[1], o[0], o[1], h2[0], h2[1], obstacles_list)
        if new_x != o_x:
            successors["O - Right"] = (h1_x, h1_y, new_x, o_y, h2_x, h2_y)

        new_x = move_left(o_x, o_y, h1_x, h1_y, h2_x, h2_y, obstacles)
        if new_x != o_x:
            successors["O - Left"] = (h1_x, h1_y, new_x, o_y, h2_x, h2_y)

        new_y = move_up(o_x, o_y, h1_x, h1_y, h2_x, h2_y, obstacles)
        if new_y != o_y:
            successors["O - Up"] = (h1_x, h1_y, o_x, new_y, h2_x, h2_y)

        new_y = move_down(o_x, o_y, h1_x, h1_y, h2_x, h2_y, obstacles)
        if new_y != o_y:
            successors["O - Down"] = (h1_x, h1_y, o_x, new_y, h2_x, h2_y)

        # H2
        new_x = move_right(h2_x, h2_y, o_x, o_y, h1_x, h1_y, obstacles)
        # (h1[0], h1[1], o[0], o[1], h2[0], h2[1], obstacles_list)
        if new_x != h2_x:
            successors["H2 - Right"] = (h1_x, h1_y, o_x, o_y, new_x, h2_y)

        new_x = move_left(h2_x, h2_y, o_x, o_y, h1_x, h1_y, obstacles)
        if new_x != h2_x:
            successors["H2 - Left"] = (h1_x, h1_y, o_x, o_y, new_x, h2_y)

        new_y = move_up(h2_x, h2_y, o_x, o_y, h1_x, h1_y, obstacles)
        if new_y != h2_y:
            successors["H2 - Up"] = (h1_x, h1_y, o_x, o_y, h2_x, new_y)

        new_y = move_down(h2_x, h2_y, o_x, o_y, h1_x, h1_y, obstacles)
        if new_y != h2_y:
            successors["H2 - Down"] = (h1_x, h1_y, o_x, o_y, h2_x, new_y)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] == state[3] == state[5] and \
                state[0] + 1 == state[2] and state[2] + 1 == state[4]


if __name__ == '__main__':
    h1 = (2, 1)
    o = (7, 2)
    h2 = (2, 6)
    obstacles_list = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]

    molecule = Molecule((h1[0], h1[1], o[0], o[1], h2[0], h2[1]), obstacles_list)

    result = breadth_first_graph_search(molecule)

    print(result.solution())

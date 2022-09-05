from pythonProject.AI.searching_framework.utils import Problem
from pythonProject.AI.searching_framework.uninformed_search import *


def move_right(x1, y1, x2, y2, x3, y3, obstacles):
    if x1 < 8 and [x1 + 1, y1] not in obstacles and [x1 + 1, y1] != [x2, y2] and [x1 + 1, y1] != [x3, y3]:
        x1 += 1
    return x1


def move_left(x1, y1, x2, y2, x3, y3, obstacles):
    if x1 > 0 and [x1 - 1, y1] not in obstacles and [x1 - 1, y1] != [x2, y2] and [x1 - 1, y1] != [x3, y3]:
        x1 -= 1
    return x1


def move_up(x1, y1, x2, y2, x3, y3, obstacles):
    if y1 < 6 and [x1, y1 + 1] not in obstacles and [x1, y1 + 1] != [x2, y2] and [x1, y1 + 1] != [x3, y3]:
        y1 += 1
    return y1


def move_down(x1, y1, x2, y2, x3, y3, obstacles):
    if y1 > 0 and [x1, y1 - 1] not in obstacles and [x1, y1 - 1] != [x2, y2] and [x1, y1 - 1] != [x3, y3]:
        y1 -= 1
    return y1



class Molecule(Problem):

    def __init__(self, obstacles, initial, goal=None):
        super(Molecule, self).__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        successors = dict()
        # (h1x,h1y,ox,oy,h2x,h2y)

        h1_x = state[0]
        h1_y = state[1]

        o_x = state[2]
        o_y = state[3]

        h2_x = state[4]
        h2_y = state[5]

        # H1 - Right
        if h1_x + 1 < 8 and [h1_x + 1, h1_y] not in self.obstacles and (h1_x + 1, h1_y) != (h2_x, h2_y) and (
                h1_x + 1, h1_y) != (o_x, o_y):
            successors["H1 - Right"] = (h1_x + 1, h1_y, o_x, o_y, h2_x, h2_y)

        # H1 - Left
        if h1_x > 0 and [h1_x - 1, h1_y] not in self.obstacles and (h1_x - 1, h1_y) != (h2_x, h2_y) and (
                h1_x - 1, h1_y) != (o_x, o_y):
            successors["H1 - Left"] = (h1_x - 1, h1_y, o_x, o_y, h2_x, h2_y)

        # H1 - Up
        if h1_y + 1 < 6 and [h1_x, h1_y + 1] not in self.obstacles and (h1_x, h1_y + 1) != (h2_x, h2_y) and (
                h1_x, h1_y + 1) != (o_x, o_y):
            successors["H1 - Up"] = (h1_x, h1_y + 1, o_x, o_y, h2_x, h2_y)

        # H1 - Down
        if h1_y > 0 and [h1_x, h1_y - 1] not in self.obstacles and (h1_x, h1_y - 1) != (h2_x, h2_y) and (
                h1_x, h1_y - 1) != (o_x, o_y):
            successors["H1 - Down"] = (h1_x, h1_y - 1, o_x, o_y, h2_x, h2_y)

        # H2 - Right
        if h2_x + 1 < 8 and [h2_x + 1, h2_y] not in self.obstacles and (h2_x + 1, h2_y) != (h1_x, h1_y) and (
        h2_x + 1, h2_y) != (o_x, o_y):
            successors["H2 - Right"] = (h1_x, h1_y, o_x, o_y, h2_x + 1, h2_y)

        # H2 - Left
        if h2_x > 0 and [h2_x - 1, h2_y] not in self.obstacles and (h2_x - 1, h2_y) != (h1_x, h1_y) and (
        h2_x - 1, h2_y) != (o_x, o_y):
            successors["H2 - Left"] = (h1_x, h1_y, o_x, o_y, h2_x - 1, h2_y)

        # H2 - Up
        if h2_y + 1 < 6 and [h2_x, h2_y + 1] not in self.obstacles and (h2_x, h2_y + 1) != (h1_x, h1_y) and (
        h2_x, h2_y + 1) != (o_x, o_y):
            successors["H2 - Up"] = (h1_x, h1_y, o_x, o_y, h2_x, h2_y + 1)

        # H2 - Down
        if h2_y > 0 and [h2_x, h2_y - 1] not in self.obstacles and (h2_x, h2_y - 1) != (h1_x, h1_y) and (
        h2_x, h2_y - 1) != (o_x, o_y):
            successors["H2 - Down"] = (h1_x, h1_y, o_x, o_y, h2_x, h2_y - 1)

        # O - Right
        if o_x + 1 < 8 and [o_x + 1, o_y] not in self.obstacles and (o_x + 1, o_y) != (h1_x, h1_y) and (
        o_x + 1, o_y) != (h2_x, h2_y):
            successors["O - Right"] = (h1_x, h1_y, o_x + 1, o_y, h2_x, h2_y)

        # O - Left
        if o_x > 0 and [o_x - 1, o_y] not in self.obstacles and (o_x - 1, o_y) != (h1_x, h1_y) and (o_x - 1, o_y) != (
        h2_x, h2_y):
            successors["O - Left"] = (h1_x, h1_y, o_x - 1, o_y, h2_x, h2_y)

        # O - Up
        if o_y + 1 < 6 and [o_x, o_y + 1] not in self.obstacles and (o_x, o_y + 1) != (h1_x, h1_y) and (
        o_x, o_y + 1) != (h2_x, h2_y):
            successors["O - Up"] = (h1_x, h1_y, o_x, o_y + 1, h2_x, h2_y)

        # O - Down
        if o_y > 0 and [o_x, o_y - 1] not in self.obstacles and (o_x, o_y - 1) != (h1_x, h1_y) and (o_x, o_y - 1) != (
        h2_x, h2_y):
            successors["O - Down"] = (h1_x, h1_y, o_x, o_y - 1, h2_x, h2_y)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] == state[3] == state[5] and state[0] + 1 == state[2] and state[2] + 1 == state[4]



if __name__ == '__main__':
    obstacles_list = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]
    h1_pos = [2, 1]
    h2_pos = [2, 6]
    o_pos = [7, 2]

    molecule = Molecule(obstacles_list, (h1_pos[0], h1_pos[1], o_pos[0], o_pos[1], h2_pos[0], h2_pos[1]))
    #
    result = breadth_first_graph_search(molecule)
    #
    print(result.solution())

    # print(obstacles_list)

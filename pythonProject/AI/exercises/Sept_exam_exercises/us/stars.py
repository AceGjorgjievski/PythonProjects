from pythonProject.AI.searching_framework.utils import Problem
from pythonProject.AI.searching_framework.uninformed_search import *


def k1(x, y, bx, by):  # up up left
    if 0 <= x - 1 < 8 and 0 <= y + 2 < 8 and [x - 1, y + 2] != [bx, by]:
        x -= 1
        y += 2
    return x, y


def k2(x, y, bx, by):  # up up right
    if 0 <= x + 1 < 8 and 0 <= y + 2 < 8 and [x + 1, y + 2] != [bx, by]:
        x += 1
        y += 2
    return x, y


def k3(x, y, bx, by):  # right right up
    if 0 <= x + 2 < 8 and 0 <= y + 1 < 8 and [x + 2, y + 1] != [bx, by]:
        x += 2
        y += 1
    return x, y


def k4(x, y, bx, by):  # right right down
    if 0 <= x + 2 < 8 and 0 <= y - 1 < 8 and [x + 2, y - 1] != [bx, by]:
        x += 2
        y -= 1
    return x, y


def k5(x, y, bx, by):  # down down right
    if 0 <= x + 1 < 8 and 0 <= y - 2 < 8 and [x + 1, y - 2] != [bx, by]:
        x += 1
        y -= 2
    return x, y


def k6(x, y, bx, by):  # down down left
    if 0 <= x - 1 < 8 and 0 <= y - 2 < 8 and [x - 1, y - 2] != [bx, by]:
        x -= 1
        y -= 2
    return x, y


def k7(x, y, bx, by):  # left left down
    if 0 <= x - 2 < 8 and 0 <= y - 1 < 8 and [x - 2, y - 1] != [bx, by]:
        x -= 2
        y -= 1
    return x, y


def k8(x, y, bx, by):  # left left up
    if 0 <= x - 2 < 8 and 0 <= y + 1 < 8 and [x - 2, y + 1] != [bx, by]:
        x -= 2
        y += 1
    return x, y


def b1(x, y, kx, ky):  # up left
    if 0 <= x - 1 < 8 and 0 <= y + 1 < 8 and [x - 1, y + 1] != [kx, ky]:
        x -= 1
        y += 1
    return x, y


def b2(x, y, kx, ky):  # up right
    if 0 <= x + 1 < 8 and 0 <= y + 1 < 8 and [x + 1, y + 1] != [kx, ky]:
        x += 1
        y += 1
    return x, y


def b3(x, y, kx, ky):  # down left
    if 0 <= x - 1 < 8 and 0 <= y - 1 < 8 and [x - 1, y - 1] != [kx, ky]:
        x -= 1
        y -= 1
    return x, y


def b4(x, y, kx, ky):  # down right
    if 0 <= x + 1 < 8 and 0 <= y - 1 < 8 and [x + 1, y - 1] != [kx, ky]:
        x += 1
        y -= 1
    return x, y


class Stars(Problem):
    def __init__(self, initial, goal=None):
        super(Stars, self).__init__(initial, goal)
        self.figures_pos = initial[0]

    def successor(self, state):
        successors = dict()

        kx, ky = state[0], state[1]
        bx, by = state[2], state[3]

        stars = state[4]

        kx_new, ky_new = k1(kx, ky, bx, by)
        if [kx_new, ky_new] != [kx, ky]:
            successors["K1"] = (kx_new, ky_new, bx, by,
                                tuple([s for s in stars if [kx_new, ky_new] != [s[0], s[1]]]))

        kx_new, ky_new = k2(kx, ky, bx, by)
        if [kx_new, ky_new] != [kx, ky]:
            successors["K2"] = (kx_new, ky_new, bx, by,
                                tuple([s for s in stars if [kx_new, ky_new] != [s[0], s[1]]]))

        kx_new, ky_new = k3(kx, ky, bx, by)
        if [kx_new, ky_new] != [kx, ky]:
            successors["K3"] = (kx_new, ky_new, bx, by,
                                tuple([s for s in stars if [kx_new, ky_new] != [s[0], s[1]]]))

        kx_new, ky_new = k4(kx, ky, bx, by)
        if [kx_new, ky_new] != [kx, ky]:
            successors["K4"] = (kx_new, ky_new, bx, by,
                                tuple([s for s in stars if [kx_new, ky_new] != [s[0], s[1]]]))

        kx_new, ky_new = k5(kx, ky, bx, by)
        if [kx_new, ky_new] != [kx, ky]:
            successors["K5"] = (kx_new, ky_new, bx, by,
                                tuple([s for s in stars if [kx_new, ky_new] != [s[0], s[1]]]))

        kx_new, ky_new = k6(kx, ky, bx, by)
        if [kx_new, ky_new] != [kx, ky]:
            successors["K6"] = (kx_new, ky_new, bx, by,
                                tuple([s for s in stars if [kx_new, ky_new] != [s[0], s[1]]]))

        kx_new, ky_new = k7(kx, ky, bx, by)
        if [kx_new, ky_new] != [kx, ky]:
            successors["K7"] = (kx_new, ky_new, bx, by,
                                tuple([s for s in stars if [kx_new, ky_new] != [s[0], s[1]]]))

        kx_new, ky_new = k8(kx, ky, bx, by)
        if [kx_new, ky_new] != [kx, ky]:
            successors["K8"] = (kx_new, ky_new, bx, by,
                                tuple([s for s in stars if [kx_new, ky_new] != [s[0], s[1]]]))

        bx_new, by_new = b1(bx, by, kx, ky)
        if [bx_new, by_new] != [bx, by]:
            successors["B1"] = (kx, ky, bx_new, by_new,
                                tuple([s for s in stars if [bx_new, by_new] != [s[0], s[1]]]))

        bx_new, by_new = b2(bx, by, kx, ky)
        if [bx_new, by_new] != [bx, by]:
            successors["B2"] = (kx, ky, bx_new, by_new,
                                tuple([s for s in stars if [bx_new, by_new] != [s[0], s[1]]]))

        bx_new, by_new = b3(bx, by, kx, ky)
        if [bx_new, by_new] != [bx, by]:
            successors["B3"] = (kx, ky, bx_new, by_new,
                                tuple([s for s in stars if [bx_new, by_new] != [s[0], s[1]]]))

        bx_new, by_new = b4(bx, by, kx, ky)
        if [bx_new, by_new] != [bx, by]:
            successors["B4"] = (kx, ky, bx_new, by_new,
                                tuple([s for s in stars if [bx_new, by_new] != [s[0], s[1]]]))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[4]) == 0


if __name__ == '__main__':
    star_pos = ((1, 1), (4, 3), (6, 6))
    knight_pos = [2, 5]
    bishop_pos = [5, 1]

    stars = Stars((knight_pos[0], knight_pos[1], bishop_pos[0], bishop_pos[1], star_pos))

    result = breadth_first_graph_search(stars)

    print(result.solution())

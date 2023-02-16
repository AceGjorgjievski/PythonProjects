from pythonProject.AI.searching_framework.utils import Problem
from pythonProject.AI.searching_framework.uninformed_search import *


# def k1(kx, ky, bx, by):  # up up left - ok
#     if 0 < kx - 1 < 8 and 0 < ky + 2 < 8 and [kx - 1, ky + 2] != [bx, by]:
#         kx -= 1
#         ky += 2
#     return kx, ky
#
#
# def k1_gore_levo(kx, ky, bx, by):
#     if 0 < kx - 1 < 8 and 0 < ky + 2 < 8 and (kx - 1, ky + 2) != (bx, by):
#         kx -= 1
#         ky += 2
#     return kx, ky
#
#
# def k2(kx, ky, bx, by):  # up up right - ok
#     if 0 < kx + 1 < 8 and 0 < ky + 2 < 8 and [kx + 1, ky + 2] != [bx, by]:
#         kx += 1
#         ky += 2
#     return kx, ky
#
#
# def k2_gore_desno(kx, ky, bx, by):
#     if 0 < kx + 1 < 8 and 0 < ky + 2 < 8 and (kx + 1, ky + 2) != (bx, by):
#         kx += 1
#         ky += 2
#     return kx, ky
#
#
# def k3(kx, ky, bx, by):  # right right up - ok
#     if 0 < kx + 2 < 8 and 0 < ky + 1 < 8 and [kx + 2, ky + 1] != [bx, by]:
#         kx += 2
#         ky += 1
#     return kx, ky
#
#
# def k3_desno_gore(kx, ky, bx, by):
#     if  0 < kx + 2 < 8 and 0 < ky + 1 < 8 and (kx + 2, ky + 1) != (bx, by):
#         kx += 2
#         ky += 1
#     return kx, ky
#
#
# def k4(kx, ky, bx, by):  # right right down - ok
#     if 0 < kx + 2 < 8 and 0 < ky - 1 < 8 and [kx + 2, ky - 1] != [bx, by]:
#         kx += 2
#         ky -= 1
#     return kx, ky
#
#
# def k4_desno_dolu(kx, ky, bx, by):
#     if  0 < kx + 2 < 8 and 0 < ky - 1 < 8 and (kx + 2, ky - 1) != (bx, by):
#         kx += 2
#         ky -= 1
#     return kx, ky
#
#
# def k5(kx, ky, bx, by):  # down down right - ok
#     if 0 < kx + 1 < 8 and 0 < ky - 2 < 8 and [kx + 1, ky - 2] != [bx, by]:
#         kx += 1
#         ky -= 2
#     return kx, ky
#
#
# def k5_dolu_desno(kx, ky, bx, by):
#     if  0 < kx + 1 < 8 and 0 < ky - 2 < 8 and (kx + 1, ky - 2) != (bx, by):
#         kx += 1
#         ky -= 2
#     return kx, ky
#
#
# def k6(kx, ky, bx, by):  # down down left - ok
#     if 0 < kx - 1 < 8 and 0 < ky - 2 < 8 and [kx - 1, ky - 2] != [bx, by]:
#         kx -= 1
#         ky -= 2
#     return kx, ky
#
#
# def k6_dolu_levo(kx, ky, bx, by):
#     if 0 < kx - 1 < 8 and 0 < ky - 2 < 8 and (kx - 1, ky - 2) != (bx, by):
#         kx -= 1
#         ky -= 2
#     return kx, ky
#
#
# def k7(kx, ky, bx, by):  # left left down - ok
#     if 0 < kx - 2 < 8 and 0 < ky - 1 < 8 and [kx - 2, ky - 1] != [bx, by]:
#         kx -= 2
#         ky -= 1
#     return kx, ky
#
#
# def k7_levo_dolu(kx, ky, bx, by):
#     if  0 < kx - 2 < 8 and 0 < ky - 1 < 8 and (kx - 2, ky - 1) != (bx, by):
#         kx -= 2
#         ky -= 1
#     return kx, ky
#
#
# def k8(kx, ky, bx, by):  # left left up - ok
#     if 0 < kx - 2 < 8 and 0 < ky + 1 < 8 and [kx - 2, ky + 1] != [bx, by]:
#         kx -= 2
#         ky += 1
#     return kx, ky
#
#
# def k8_levo_gore(kx, ky, bx, by):
#     if  0 < kx - 2 < 8 and 0 < ky + 1 < 8 and (kx - 2, ky + 1) != (bx, by):
#         kx -= 2
#         ky += 1
#     return kx, ky
#
#
# def b1(bx, by, kx, ky):  # up left - ok
#     if 0 < bx - 1 < 8 and 0 < by + 1 < 8 and [bx - 1, by + 1] != [kx, ky]:
#         bx -= 1
#         by += 1
#     return by, by
#
#
# def b1_gore_levo(bx, by, kx, ky):
#     if (bx - 1, by + 1) != (kx, ky) and 0 < bx - 1 < 8 and 0 < by + 1 < 8:
#         bx -= 1
#         by += 1
#     return bx, by
#
#
# def b2(bx, by, kx, ky):  # up right - ok
#     if 0 < bx + 1 < 8 and 0 < by + 1 < 8 and [bx + 1, by + 1] != [kx, ky]:
#         bx += 1
#         by += 1
#     return by, by
#
#
# def b2_gore_desno(bx, by, kx, ky):
#     if (bx + 1, by + 1) != (kx, ky) and 0 < bx + 1 < 8 and 0 < by + 1 < 8:
#         bx += 1
#         by += 1
#     return bx, by
#
#
# def b3(bx, by, kx, ky):  # down left - ok
#     if 0 < bx - 1 < 8 and 0 < by - 1 < 8 and [bx - 1, by - 1] != [kx, ky]:
#         bx -= 1
#         by -= 1
#     return by, by
#
#
# def b3_dolu_levo(bx, by, kx, ky):
#     if (bx - 1, by - 1) != (kx, ky) and 0 < bx - 1 < 8 and 0 < by - 1 < 8:
#         bx -= 1
#         by -= 1
#     return bx, by
#
#
# def b4(bx, by, kx, ky):  # down right - ok
#     if 0 < bx + 1 < 8 and 0 < by - 1 < 8 and [bx + 1, by - 1] != [kx, ky]:
#         bx += 1
#         by -= 1
#     return by, by
#
#
# def b4_dolu_desno(bx, by, kx, ky):
#     if (bx + 1, by - 1) != (kx, ky) and 0 < bx + 1 < 8 and 0 < by - 1 < 8:
#         bx += 1
#         by -= 1
#     return bx, by
def k1(x, y, b_x, b_y):  # up up left
    if 0 < x - 1 < 8 and 0 < y + 2 < 8 and [x - 1, y + 2] != [b_x, b_y]:
        x -= 1
        y += 2
    return x, y


def k2(x, y, b_x, b_y):  # up up right
    if 0 < x + 1 < 8 and 0 < y + 2 < 8 and [x + 1, y + 2] != [b_x, b_y]:
        x += 1
        y += 2
    return x, y


def k3(x, y, b_x, b_y):  # right right up
    if 0 < x + 2 < 8 and 0 < y + 1 < 8 and [x + 2, y + 1] != [b_x, b_y]:
        x += 2
        y += 1
    return x, y


def k4(x, y, b_x, b_y):  # right right down
    if 0 < x + 2 < 8 and 0 < y - 1 < 8 and [x + 2, y - 1] != [b_x, b_y]:
        x += 2
        y -= 1
    return x, y


def k5(x, y, b_x, b_y):  # down down right
    if 0 < x + 1 < 8 and 0 < y - 2 < 8 and [x + 1, y - 2] != [b_x, b_y]:
        x += 1
        y -= 2
    return x, y


def k6(x, y, b_x, b_y):  # down down left
    if 0 < x - 1 < 8 and 0 < y - 2 < 8 and [x - 1, y - 2] != [b_x, b_y]:
        x -= 1
        y -= 2
    return x, y


def k7(x, y, b_x, b_y):  # left left down
    if 0 < x - 2 < 8 and 0 < y - 1 < 8 and [x - 2, y - 1] != [b_x, b_y]:
        x -= 2
        y -= 1
    return x, y


def k8(x, y, b_x, b_y):  # left left up
    if 0 < x - 2 < 8 and 0 < y + 1 < 8 and [x - 2, y + 1] != [b_x, b_y]:
        x -= 2
        y += 1
    return x, y


def b1(x, y, k_x, k_y):  # up left
    if 0 < x - 1 < 8 and 0 < y + 1 < 8 and [x - 1, y + 1] != [k_x, k_y]:
        x -= 1
        y += 1
    return x, y


def b2(x, y, k_x, k_y):  # up right
    if 0 < x + 1 < 8 and 0 < y + 1 < 8 and [x + 1, y + 1] != [k_x, k_y]:
        x += 1
        y += 1
    return x, y


def b3(x, y, k_x, k_y):  # down left
    if 0 < x - 1 < 8 and 0 < y - 1 < 8 and [x - 1, y - 1] != [k_x, k_y]:
        x -= 1
        y -= 1
    return x, y


def b4(x, y, k_x, k_y):  # down right
    if 0 < x + 1 < 8 and 0 < y - 1 < 8 and [x + 1, y - 1] != [k_x, k_y]:
        x += 1
        y -= 1
    return x, y


# ------------------------------------------------------------------------------------


class Stars(Problem):
    def __init__(self, initial, goal=None):
        super(Stars, self).__init__(initial, goal)

    def successor(self, state):
        successors = {}

        kx = state[0]
        ky = state[1]
        bx = state[2]
        by = state[3]

        stars = state[4]

        # k1
        new_x, new_y = k1(kx, ky, bx, by)
        # (knight, bishop, stars_pos)
        if [new_x, new_y] != [kx, ky]:
            successors["K1 - UUL"] = (new_x, new_y, bx, by,
                                      tuple([s for s in stars if [new_x, new_y] != [s[0], s[1]]]))

        # k2
        new_x, new_y = k2(kx, ky, bx, by)
        if [new_x, new_y] != [kx, ky]:
            successors["K2 - UUR"] = (new_x, new_y, bx, by,
                                      tuple([s for s in stars if [new_x, new_y] != [s[0], s[1]]]))

        # k3
        new_x, new_y = k3(kx, ky, bx, by)
        if [new_x, new_y] != [kx, ky]:
            successors["K3 - RRU"] = (new_x, new_y, bx, by,
                                      tuple([s for s in stars if [new_x, new_y] != [s[0], s[1]]]))

        # k4
        new_x, new_y = k4(kx, ky, bx, by)
        if [new_x, new_y] != [kx, ky]:
            successors["K4 - RRD"] = (new_x, new_y, bx, by,
                                      tuple([s for s in stars if [new_x, new_y] != [s[0], s[1]]]))

        # k5
        new_x, new_y = k5(kx, ky, bx, by)
        if [new_x, new_y] != [kx, ky]:
            successors["K5 - DDR"] = (new_x, new_y, bx, by,
                                      tuple([s for s in stars if [new_x, new_y] != [s[0], s[1]]]))

        # k6
        new_x, new_y = k6(kx, ky, bx, by)
        if [new_x, new_y] != [kx, ky]:
            successors["K6 - DDL"] = (new_x, new_y, bx, by,
                                      tuple([s for s in stars if [new_x, new_y] != [s[0], s[1]]]))

        # k7
        new_x, new_y = k7(kx, ky, bx, by)
        if [new_x, new_y] != [kx, ky]:
            successors["K7 - LLD"] = (new_x, new_y, bx, by,
                                      tuple([s for s in stars if [new_x, new_y] != [s[0], s[1]]]))

        # k8
        new_x, new_y = k8(kx, ky, bx, by)
        if [new_x, new_y] != [kx, ky]:
            successors["K8 - LLU"] = (new_x, new_y, bx, by,
                                      tuple([s for s in stars if [new_x, new_y] != [s[0], s[1]]]))

        # b1
        new_x, new_y = b1(bx, by, kx, ky)
        if [new_x, new_y] != [bx, by]:
            successors["B1 - UL"] = (kx, ky, new_x, new_y,
                                     tuple([s for s in stars if [new_x, new_y] != [s[0], s[1]]]))

        # b2
        new_x, new_y = b2(bx, by, kx, ky)
        if [new_x, new_y] != [bx, by]:
            successors["B2 - UR"] = (kx, ky, new_x, new_y,
                                     tuple([s for s in stars if [new_x, new_y] != [s[0], s[1]]]))

        # b3
        new_x, new_y = b3(bx, by, kx, ky)
        if [new_x, new_y] != [bx, by]:
            successors["B3 - DL"] = (kx, ky, new_x, new_y,
                                     tuple([s for s in stars if [new_x, new_y] != [s[0], s[1]]]))

        # b4
        new_x, new_y = b4(bx, by, kx, ky)
        if [new_x, new_y] != [bx, by]:
            successors["B4 - DR"] = (kx, ky, new_x, new_y,
                                     tuple([s for s in stars if [new_x, new_y] != [s[0], s[1]]]))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[4]) == 0


if __name__ == '__main__':
    knight = [2, 5]
    bishop = [5, 1]
    stars_pos = ((1, 1), (4, 3), (6, 6))

    stars = Stars((knight[0], knight[1], bishop[0], bishop[1], stars_pos))

    result = breadth_first_graph_search(stars)

    print(result.solution())

    #ima greshka vo moite f-ii

    # ['K2 - UUR', 'K5 - DDR', 'K3 - RRU', 'K5 - DDR', 'K6 - DDL', 'K8 - LLU', 'B3 - DL']

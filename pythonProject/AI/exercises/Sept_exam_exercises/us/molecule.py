from pythonProject.AI.searching_framework.utils import Problem
from pythonProject.AI.searching_framework.uninformed_search import *
from pythonProject.AI.searching_framework.informed_search import *


def move_right(x1, y1, x2, y2, x3, y3, obstacles):
    while x1 < 8 and [x1 + 1, y1] not in obstacles and [x1 + 1, y1] != [x2, y2] and [x1 - 1, y1] != [x3, y3]:
        x1 += 1
    return x1


def move_left(x1, y1, x2, y2, x3, y3, obstacles):
    while x1 > 0 and [x1 - 1, y1] not in obstacles and [x1 - 1, y1] != [x2, y2] and [x1 - 1, y1] != [x3, y3]:
        x1 -= 1
    return x1


def move_up(x1, y1, x2, y2, x3, y3, obstacles):
    while y1 < 6 and [x1, y1 + 1] not in obstacles and [x1, y1 + 1] != [x2, y2] and [x1, y1 + 1] != [x3, y3]:
        y1 += 1
    return y1


def move_down(x1, y1, x2, y2, x3, y3, obstacles):
    while y1 > 0 and [x1, y1 - 1] not in obstacles and [x1, y1 - 1] != [x2, y2] and [x1, y1 - 1] != [x3, y3]:
        y1 -= 1
    return y1


class Molecule(Problem):
    def __init__(self, obstacles, initial, goal=None):
        super(Molecule, self).__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        successors = dict()

        h1_x, h1_y = state[0], state[1]
        o_x, o_y = state[2], state[3]
        h2_x, h2_y = state[4], state[5]

        x_new = move_right(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if x_new != h1_x:
            successors["Right - H1"] = (x_new, h1_y, o_x, o_y, h2_x, h2_y)
        x_new = move_left(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if x_new != h1_x:
            successors["Left - H1"] = (x_new, h1_y, o_x, o_y, h2_x, h2_y)
        y_new = move_up(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if y_new != h1_y:
            successors["Up - H1"] = (h1_x, y_new, o_x, o_y, h2_x, h2_y)
        y_new = move_down(h1_x, h1_y, o_x, o_y, h2_x, h2_y, self.obstacles)
        if y_new != h1_y:
            successors["Down - H1"] = (h1_x, y_new, o_x, o_y, h2_x, h2_y)

        x_new = move_right(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if x_new != h2_x:
            successors["Right - H2"] = (h1_x, h1_y, o_x, o_y, x_new, h2_y)
        x_new = move_left(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if x_new != h2_x:
            successors["Left - H2"] = (h1_x, h1_y, o_x, o_y, x_new, h2_y)
        y_new = move_up(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if y_new != h2_y:
            successors["Up - H2"] = (h1_x, h1_y, o_x, o_y, h2_x, y_new)
        y_new = move_down(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.obstacles)
        if y_new != h2_y:
            successors["Down - H2"] = (h1_x, h1_y, o_x, o_y, h2_x, y_new)

        x_new = move_right(o_x, o_y, h1_x, h1_y, h2_x, h2_y, self.obstacles)
        if x_new != o_x:
            successors["Right - O"] = (h1_x, h1_y, x_new, o_y, h2_x, h2_y)
        x_new = move_left(o_x, o_y, h1_x, h1_y, h2_x, h2_y, self.obstacles)
        if x_new != o_x:
            successors["Left - O"] = (h1_x, h1_y, x_new, o_y, h2_x, h2_y)
        y_new = move_up(o_x, o_y, h1_x, h1_y, h2_x, h2_y, self.obstacles)
        if y_new != o_y:
            successors["Up - O"] = (h1_x, h1_y, o_x, y_new, h2_x, h2_y)
        y_new = move_down(o_x, o_y, h1_x, h1_y, h2_x, h2_y, self.obstacles)
        if y_new != o_y:
            successors["Down - O"] = (h1_x, h1_y, o_x, y_new, h2_x, h2_y)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] == state[3] == state[5] and state[0] + 1 == state[2] and state[2] + 1 == state[4]

    def h(self, node):
        h1_x, h1_y = node.state[0], node.state[1]
        o_x, o_y = node.state[2], node.state[3]
        h2_x, h2_y = node.state[4], node.state[5]

        value = 0
        if h1_y != o_y:
            if h1_x != (o_x-1):
                value += 2
            else:
                value += 1
        else:
            if h1_x > o_x:
                value+=3
            else:
                value += 1

        if h2_y != o_y:
            if h2_x != (o_x+1):
                value+=2
            else:
                value+=1
        else:
            if h2_x < o_x:
                value+=3
            else:
                value+=1

        if h1_y == h2_y and h2_x != o_x - 1:
            value -= 1

        return value



if __name__ == '__main__':
    obstacles_list = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]
    h1_pos = [2, 1]
    h2_pos = [2, 6]
    o_pos = [7, 2]

    molecule = Molecule(obstacles_list, (h1_pos[0], h1_pos[1], o_pos[0], o_pos[1], h2_pos[0], h2_pos[1]))

    result = breadth_first_graph_search(molecule)

    print(result.solution())

    result2 = astar_search(molecule)
    print(result2.solution())

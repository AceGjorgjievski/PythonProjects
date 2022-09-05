from pythonProject.AI.searching_framework.utils import Problem
from pythonProject.AI.searching_framework.informed_search import *



class Puzzle(Problem):
    def __init__(self, initial, goal=None):
        super(Puzzle, self).__init__(initial, goal)

    def successor(self, state):
        successors = {}



        """
            0 1 2
            3 4 5
            6 7 8
            
        """

        ind = state.index('*')

        #up
        if ind >= 3:
            temp = list(state)
            temp[ind], temp[ind-3] = temp[ind-3], temp[ind]
            new_state = ''.join(temp)
            successors["Up"] = new_state

        #down
        if ind <= 5:
            tmp = list(state)
            tmp[ind], tmp[ind+3] = tmp[ind+3], tmp[ind]
            new_state = ''.join(tmp)
            successors["Down"] = new_state

        #left
        if ind % 3 != 0:
            tmp = list(state)
            tmp[ind], tmp[ind - 1] = tmp[ind - 1], tmp[ind]
            new_state = ''.join(tmp)
            successors["Left"] = new_state

        #right
        if ind % 3 != 2:
            tmp = list(state)
            tmp[ind], tmp[ind + 1] = tmp[ind + 1], tmp[ind]
            new_state = ''.join(tmp)
            successors["Right"] = new_state


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        counter = 0
        for x,y in zip(node.state, self.goal):
            if x != y:
                counter += 1
        return counter

class Puzzle2(Puzzle):
    coordinates = {0:(0, 2), 1: (1, 2), 2: (2, 2),
                   3: (0, 1), 4: (1, 1), 5: (2, 1),
                   6: (0, 0), 7: (1, 0), 8: (2, 0)}


    @staticmethod
    def mhd(n,m):
        x1,y1 = Puzzle2.coordinates[n]
        x2,y2 = Puzzle2.coordinates[m]

        return abs(x1-x2) + abs(y1-y2)

    def h(self, node):
        sum_value=0

        for x in '12345678':
            val = Puzzle2.mhd(node.state.index(x), int(x))
            sum_value += val
        return sum_value


if __name__ == '__main__':
    puzzle = Puzzle2('*32415678','*12345678')
    result = astar_search(puzzle)

    print(result.solve())


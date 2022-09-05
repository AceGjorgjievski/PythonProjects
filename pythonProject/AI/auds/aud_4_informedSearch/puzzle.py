
from pythonProject.AI.searching_framework.informed_search import greedy_best_first_graph_search, astar_search, recursive_best_first_search
from pythonProject.AI.searching_framework.utils import *





class Puzzle(Problem):
    def __init__(self, initial, goal=None):
        super(Puzzle, self).__init__(initial, goal)

    def successor(self, state):

        """
            state='*32415678'
            * 1 2
            4 4 5
            6 7 8

        """

        succ = {}

        ind  = state.index('*')

        #Up
        if ind >= 3:
            tmp = list(state)
            tmp[ind], tmp[ind-3] = tmp[ind-3], tmp[ind]
            new_state = ''.join(tmp)
            succ["Up"] = new_state

        #Down
        if ind <=5:
            tmp = list(state)
            tmp[ind], tmp[ind+3] = tmp[ind+3], tmp[ind]
            new_state = ''.join(tmp)
            succ["Down"] = new_state

        #Left

        if ind%3 != 0:
            tmp = list(state)
            tmp[ind],tmp[ind-1] = tmp[ind-1], tmp[ind]
            new_state = ''.join(tmp)
            succ["Left"] = new_state

        #Right

        if ind%3 != 2:
            tmp=list(state)
            tmp[ind], tmp[ind+1] = tmp[ind+1], tmp[ind]
            new_state = ''.join(tmp)
            succ["Right"] = new_state

        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        counter = 0
        for x,y in zip(self.goal, node.state):
            if x != y:
                counter += 1

        return counter

class Puzzle_h2(Puzzle):
    coordinates = {0: (0,2), 1: (1,2), 2: (2,2),
                   3: (0,1), 4: (1,1), 5: (2,1),
                   6: (0,0), 7: (0,1), 8: (0,2)}
    @staticmethod
    def mhd(n,m):
        x1, y1 = Puzzle_h2.coordinates[n]
        x2, y2 = Puzzle_h2.coordinates[m]
        return abs(x1-x2) + abs(y1-y2)

    def h(self, node):
        sum = 0
        for i in '12345678':
            val = Puzzle_h2.mhd(node.state.index(i), int(i))
            sum += val
        return sum



if __name__ == '__main__':
    pass

    puzzle = Puzzle_h2('*32415678','*12345678')

    rez1 = astar_search(puzzle)
    print(rez1.solve())
    print(rez1.solution())
    rez2 = greedy_best_first_graph_search(puzzle)
    print(rez2.solve())
    print(rez2.solution())
    rez3 = recursive_best_first_search(puzzle)
    print(rez3.solve())
    print(rez3.solution())





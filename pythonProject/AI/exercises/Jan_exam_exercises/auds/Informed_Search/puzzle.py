
from pythonProject.AI.searching_framework.informed_search import greedy_best_first_graph_search, astar_search, recursive_best_first_search
from pythonProject.AI.searching_framework.utils import *



class Puzzle(Problem):
    def __init__(self, initial, goal=None):
        super(Puzzle, self).__init__(initial, goal)

    def successor(self, state):
        succ = {}

        """
            0 1 2
            3 4 5
            6 7 8
            
            * 3 2
            4 1 5 
            6 7 8
            
        """
        ind = state.index('*')

        if ind % 3 != 0:
            temp = list(state)
            temp[ind], temp[ind-1] = temp[ind-1], temp[ind]
            new_state = ''.join(temp)
            succ["Left"] = new_state

        if ind % 3 != 2:
            temp = list(state)
            temp[ind], temp[ind+1] = temp[ind+1], temp[ind]
            new_state = ''.join(temp)
            succ["Right"] = new_state

        if ind <= 5:
            temp = list(state)
            temp[ind], temp[ind+3] = temp[ind+3], temp[ind]
            new_state = ''.join(temp)
            succ["Down"] = new_state

        if ind >= 3:
            temp = list(state)
            temp[ind], temp[ind-3] = temp[ind-3], temp[ind]
            new_state = ''.join(temp)
            succ["Up"] = new_state

        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        counter = 0
        curr = node.state
        final = self.goal

        for x,y in zip(curr, final):
            if x != y:
                counter += 1

        return counter


if __name__ == '__main__':
    initial = '*32415678'


    goal = '*12345678'

    puzzle = Puzzle(initial, goal)

    result = astar_search(puzzle).solution()

    print(result)



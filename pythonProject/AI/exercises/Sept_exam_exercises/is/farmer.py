from pythonProject.AI.searching_framework.utils import Problem
from pythonProject.AI.searching_framework.informed_search import *



def valid(state):
    farmer, volk, jare, zelka = state
    if volk == jare and farmer != volk:
        return False
    if jare == zelka and farmer != jare:
        return False

    return True

class Farmer(Problem):
    def __init__(self, initial, goal=None):
        super(Farmer, self).__init__(initial, goal)


    def successor(self, state):
        successors = {}

        farmer, volk, jare, zelka = state

        farmer_new = 'e' if farmer == 'w' else 'w'
        state_new = farmer_new, volk, jare, zelka

        if valid(state_new):
            successors["Farmer nosi Farmer"] = state_new


        volk_new = 'e' if volk == 'w' else 'w'
        state_new = farmer_new, volk_new, jare, zelka

        if valid(state_new):
            successors["Farmer nosi volk"] = state_new

        jare_new = 'e' if jare == 'w' else 'w'
        state_new = farmer_new, volk, jare_new, zelka
        if valid(state_new):
            successors["Farmer nosi jare"] = state_new

        zelka_new = 'e' if zelka =='w' else 'w'
        state_new = farmer_new, volk, jare, zelka_new
        if valid(state_new):
            successors["Farmer nosi zelka"] = state_new


        return successors


    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):

        value = 0
        for x,y in zip(node.state, self.goal):
            if x != y:
                value+=1
        return value




if __name__ == '__main__':
    initial_state = ('e','e','e','e')
    goal_state = ('w','w','w','w')

    farmer = Farmer(initial_state, goal_state)

    result = astar_search(farmer)
    print(result.solution())


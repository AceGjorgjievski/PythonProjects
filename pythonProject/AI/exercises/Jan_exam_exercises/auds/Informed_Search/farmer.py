from pythonProject.AI.searching_framework.informed_search import greedy_best_first_graph_search, astar_search, \
    recursive_best_first_search
from pythonProject.AI.searching_framework.utils import *


def valid(state):
    farmer, volk, zelka, jare = state

    if volk == jare and farmer != volk:
        return False

    if jare == zelka and farmer != jare:
        return False

    return True

class Farmer(Problem):
    def __init__(self, initial, goal=None):
        super(Farmer, self).__init__(initial, goal)

    def successor(self, state):
        succ = {}

        farmer, volk, zelka, jare = state

        farmer_new = "e" if farmer == "w" else "w"
        state_new = farmer_new, volk, zelka, jare

        if valid(state_new):
            succ["Farmer_nosi_farmer"] = state_new

        volk_new = "e" if volk == "w" else "w"
        state_new = farmer_new, volk_new, zelka, jare
        if valid(state_new):
            succ["Farmer_nosi_volk"] = state_new

        jare_new = "e" if jare == "w" else "w"
        state_new = farmer_new, volk, zelka, jare_new
        if valid(state_new):
            succ["Farmer_nosi_jare"] = state_new

        zelka_new = "e" if zelka == "w" else "w"
        state_new = farmer_new, volk, zelka_new, jare
        if valid(state_new):
            succ["Farmer_nosi_zelka"] = state_new


        return succ

    def result(self, state, action):
        return self.successor(state)[action]

    def actions(self, state):
        return self.successor(state).keys()

    def h(self, node):
        start = node.state
        finish = self.goal

        counter = 0
        for x,y in zip(start, finish):
            if x != y:
                counter += 1

        return counter


if __name__ == '__main__':

    initial = ("e","e","e","e")
    final = ("w","w","w","w")

    farmer = Farmer(initial, final)

    result = astar_search(farmer).solution()

    print(result)

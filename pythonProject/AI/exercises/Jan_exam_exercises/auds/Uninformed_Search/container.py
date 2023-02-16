from pythonProject.AI.searching_framework.utils import Problem
from pythonProject.AI.searching_framework.uninformed_search import *



class Container(Problem):
    def __init__(self,capacities, initial, goal=None):
        super(Container, self).__init__(initial, goal)
        self.capacities = capacities

    def successor(self, state):
        successors = {}

        j0, j1 = state[0], state[1]

        if j0 > 0:
            successors["Isprazni go sadot J0"] = (0, j1)

        if j1 > 0:
            successors["Isprazni go sadot J1"] = (j0, 0)


        c0, c1 = self.capacities

        if j0 > 0 and j1 < c1:
            delta = min(j0, c1- j1)
            successors["Preturi od J0 vo J1"] = (j0 - delta, j1 + delta)

        if j1 > 0 and j0 < c0:
            delta = min(j1, c0 - j0)
            successors["Preturi od J1 vo J0"] = (j0 + delta, j1 - delta)


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.goal[0] and state[1] == self.goal[1]

if __name__ == '__main__' :

    container = Container((15,5),(5,5),(0,0))

    result = depth_first_graph_search(container)

    print(result.solution())
    print(result.solve())


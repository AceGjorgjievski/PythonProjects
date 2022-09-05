from pythonProject.AI.searching_framework import Problem
from pythonProject.AI.searching_framework.informed_search import *


class Ghost_Skates(Problem):
    def __init__(self, initial, walls, n, goal = None):
        super(Ghost_Skates, self).__init__(initial, goal)
        self.walls = walls
        self.n = n

    @staticmethod
    def check_valid(state, walls, n):
        x = state[0]
        y = state[1]

        if state in walls or x > n-1 or y > n-1:
            return False
        return True

    def successor(self, state):
        successors = {}

        x = state[0]
        y = state[1]

        #up
        new_state = (x, y+1)
        if Ghost_Skates.check_valid(new_state, self.walls, self.n) == True:
            successors["Gore 1"] = new_state
        new_state = (x, y + 2)
        if Ghost_Skates.check_valid(new_state, self.walls, self.n) == True:
            successors["Gore 2"] = new_state
        new_state = (x, y + 3)
        if Ghost_Skates.check_valid(new_state, self.walls, self.n) == True:
            successors["Gore 3"] = new_state

        # right
        new_state = (x+1, y)
        if Ghost_Skates.check_valid(new_state, self.walls, self.n) == True:
            successors["Desno 1"] = new_state
        new_state = (x+2, y)
        if Ghost_Skates.check_valid(new_state, self.walls, self.n) == True:
            successors["Desno 2"] = new_state
        new_state = (x+3, y)
        if Ghost_Skates.check_valid(new_state, self.walls, self.n) == True:
            successors["Desno 3"] = new_state

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        x = node.state[0]
        y = node.state[1]

        dist = abs(x - self.goal[0]) + abs(y - self.goal[1])
        return dist / 3



if __name__ == '__main__':
    n = int(input())
    ghost_pos = (0, 0)
    goal_pos = (n - 1, n - 1)

    num_holes = int(input())
    holes = list()
    for _ in range(num_holes):
        holes.append(tuple(map(int, input().split(','))))

    problem = Ghost_Skates(ghost_pos, holes, n, goal_pos)

    result = astar_search(problem)

    print(result.solution())



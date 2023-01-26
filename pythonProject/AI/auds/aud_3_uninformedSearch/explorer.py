from pythonProject.AI.searching_framework.utils import Problem
from pythonProject.AI.searching_framework.uninformed_search import *


class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super(Explorer, self).__init__(initial, goal)
        self.grid_size = [8, 6]

    def successor(self, state):
        successors = dict()

        man_x = state[0]
        man_y = state[1]

        obs1 = list(state[2])
        obs2 = list(state[3])

        if obs1[2] == 1:  # up
            if obs1[1] == self.grid_size[1] - 1:
                obs1[2] = -1
                obs1[1] -= 1
            else:
                obs1[1] += 1
        else:
            if obs1[1] == 0:
                obs1[2] = 1
                obs1[1] += 1
            else:
                obs1[1] -= 1

        if obs2[2] == 1:  # up
            if obs2[1] == self.grid_size[1] - 1:
                obs2[2] = -1
                obs2[1] -= 1
            else:
                obs2[1] += 1
        else:
            if obs2[1] == 0:
                obs2[2] = 1
                obs2[1] += 1
            else:
                obs2[1] -= 1

        obstacles = [(obs1[0], obs1[1]), (obs2[0], obs2[1])]

        # (x,y,(obs1[0],obs1[1],ob1[2]),(obs1[0],obs1[1],obs1[2]))
        if man_x + 1 < self.grid_size[0] and (man_x + 1, man_y) not in obstacles:  # right
            successors["Right"] = (man_x + 1, man_y,
                                   (obs1[0], obs1[1], obs1[2]), (obs2[0], obs2[1], obs2[2]))

        if man_x > 0 and (man_x - 1, man_y) not in obstacles:  # left
            successors["Left"] = (man_x - 1, man_y,
                                  (obs1[0], obs1[1], obs1[2]), (obs2[0], obs2[1], obs2[2]))
        if man_y + 1 < self.grid_size[1] and (man_x, man_y + 1) not in obstacles:
            successors["Up"] = (man_x, man_y + 1,
                                (obs1[0], obs1[1], obs1[2]), (obs2[0], obs2[1], obs2[2]))
        if man_y > 0 and (man_x, man_y - 1) not in obstacles:
            successors["Down"] = (man_x, man_y - 1,
                                  (obs1[0], obs1[1], obs1[2]), (obs2[0], obs2[1], obs2[2]))

        # print(successors)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        # print(f"({state[0],state[1]})",self.goal)
        return state[0] == self.goal[0] and state[1] == self.goal[1]


if __name__ == "__main__":
    goal_state = (7, 4)
    initial_state = (0, 5)
    obs1 = (2, 5, -1)
    obs2 = (5, 0, 1)

    # explorer = Explorer((initial_state[0],initial_state[1],(obs1[0], obs1[1], obs1[2]), (obs2[0],obs2[1],obs2[2])), goal_state)
    exp = Explorer((initial_state[0], initial_state[1], obs1, obs2), goal_state)
    result = breadth_first_graph_search(exp)

    print(result.solution())

    # print(result.solve())



from pythonProject.AI.searching_framework.utils import Problem
from pythonProject.AI.searching_framework.uninformed_search import *
from pythonProject.AI.searching_framework.informed_search import *


class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super(Explorer, self).__init__(initial, goal)
        self.grid_size = [8, 6]

    def successor(self, state):
        successors = dict()

        man_x = state[0][0]
        man_y = state[0][1]

        obs_1 = list(state[1])
        obs_2 = list(state[2])


        # (2,5,-1)
        if obs_1[2] == 1:
            if obs_1[1] == self.grid_size[1] - 1:
                obs_1[2] = -1
                obs_1[1] -= 1
            else:
                obs_1[1] += 1
        else:
            if obs_1[1] == 0:
                obs_1[2] = 1
                obs_1[1] += 1
            else:
                obs_1[1] -= 1

        if obs_2[2] == 1:
            if obs_2[1] == self.grid_size[1] - 1:
                obs_2[2] = -1
                obs_2[1] -= 1
            else:
                obs_2[1] += 1
        else:
            if obs_2[1] == 0:
                obs_2[2] = 1
                obs_2[1] += 1
            else:
                obs_2[1] -= 1


        obstacles = [(obs_1[0], obs_1[1]), (obs_2[0], obs_2[1])]
        # state = ((man_x, man_y), (obs1_x,obs1_y,obs1_dir), (obs2_x,obs2_y,obs2_dir))
        # right
        if man_x + 1 < self.grid_size[0] and (man_x + 1, man_y) not in obstacles:
            successors["Right"] = ((man_x + 1, man_y),
                                   (obs_1[0], obs_1[1], obs_1[2]), (obs_2[0], obs_2[1], obs_2[2]))

        # left
        if man_x  > 0 and (man_x - 1, man_y) not in obstacles:
            successors["Left"] = ((man_x - 1, man_y),
                                  (obs_1[0], obs_1[1], obs_1[2]), (obs_2[0], obs_2[1], obs_2[2]))

        # up
        if man_y + 1 < self.grid_size[1] and (man_x, man_y + 1) not in obstacles:
            successors["Up"] = ((man_x, man_y + 1),
                                (obs_1[0], obs_1[1], obs_1[2]), (obs_2[0], obs_2[1], obs_2[2]))

        # down
        if man_y > 0 and (man_x, man_y - 1) not in obstacles:
            successors["Down"] = ((man_x, man_y - 1),
                                  (obs_1[0], obs_1[1], obs_1[2]), (obs_2[0], obs_2[1], obs_2[2]))

        #print(successors)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0][0] == self.goal[0] and state[0][1] == self.goal[1]

    def h(self, node):
        x_man = node.state[0][0]
        y_man = node.state[0][1]

        house_x = self.goal[0]
        house_y = self.goal[1]

        return abs(x_man-house_x) + abs(y_man-house_y)


if __name__ == '__main__':
    initial_state = (0,2)
    obs1 = (2,5,-1)
    obs2 = (5,0,1)
    goal_state = (6,5)

    explorer = Explorer((initial_state, obs1, obs2), goal_state)

    result = breadth_first_graph_search(explorer)

    print(result.solution())
    result2 = astar_search(explorer)
    print(result2.solution())
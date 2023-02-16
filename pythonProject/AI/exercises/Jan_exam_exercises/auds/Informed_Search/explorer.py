from pythonProject.AI.searching_framework.utils import Problem
from pythonProject.AI.searching_framework.informed_search import astar_search


class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super(Explorer, self).__init__(initial, goal)
        self.grid_size = [8, 6]

    def successor(self, state):
        successors = {}

        obs_1 = list(obstacles[0])
        obs_2 = list(obstacles[1])

        man_x = state[0]
        man_y = state[1]

        if obs_1[2] == -1:
            if obs_1[1] > 0:
                obs_1[1] -= 1
            else:
                obs_1[2] = 1
                obs_1[1] += 1
        else:
            if obs_1[1] < self.grid_size[1]:
                obs_1[1] += 1
            else:
                obs_1[2] = -1
                obs_1[1] -= 1

        if obs_2[2] == 1:
            if obs_2[1] < self.grid_size[1]:
                obs_2[1] += 1
            else:
                obs_2[2] = -1
                obs_2[1] -= 1
        else:
            if obs_2[1] > 0:
                obs_2[1] -= 1
            else:
                obs_2[2] = 1
                obs_2[1] += 1

        if man_x + 1 < self.grid_size[0] and (man_x + 1, man_y) not in obstacles:
            successors["Right"] = (man_x + 1, man_y,
                                   (obs_1[0], obs_1[1], obs_1[2]),
                                   (obs_2[0], obs_2[1], obs_2[2]))

        if man_x > 0 and (man_x - 1, man_y) not in obstacles:
            successors["Left"] = (man_x - 1, man_y, (obs_1[0], obs_1[1], obs_1[2]),
                                  (obs_2[0], obs_2[1], obs_2[2]))

        if man_y + 1 < self.grid_size[1] and (man_x, man_y + 1) not in obstacles:
            successors["Up"] = (man_x, man_y + 1, (obs_1[0], obs_1[1], obs_1[2]),
                                (obs_2[0], obs_2[1], obs_2[2]))

        if man_y > 0 and (man_x, man_y - 1) not in obstacles:
            successors["Down"] = (man_x, man_y - 1, (obs_1[0], obs_1[1], obs_1[2]),
                                  (obs_2[0], obs_2[1], obs_2[2]))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    # def goal_test(self, state):
    #     return state[0] == self.goal[0] and state[1] == self.goal[1]

    def goal_test(self, state):
        g = self.goal
        return state[0] == g[0] and state[1] == g[1]

    def h(self, node):
        mx, my = node.state[0], node.state[1]
        gx, gy = self.goal[0], self.goal[1]

        return abs(mx-gx) + abs(my-gy)


if __name__ == '__main__':
    man = (0, 2)
    goal = (7, 4)
    obstacles = ((2, 5, -1), (5, 0, 1))

    explorer = Explorer(
        (man[0], man[1], obstacles[0], obstacles[1]),
        (goal[0], goal[1])
    )

    result = astar_search(explorer)

    print(result.solution())

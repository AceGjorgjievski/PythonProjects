import numpy as np
from gymnasium import spaces
import gymnasium as gym
# %matplotlib inline


class Snake_game(gym.Env):
    metadata = {'render.modes': ['console', 'rgb_array']}
    n_actions = 3
    LEFT = 0
    STRAIGHT = 0
    RIGHT = 2

    EMPTY = 0
    SNAKE = 1
    WALL = 2
    FOOD = 3

    REWARD_WALL_HIT = -20
    REWARD_PER_STEP_TOWARDS_FOOD = 1
    REWARD_PER_FOOD = 50
    MAX_STEPS_AFTER_FOOD = 200




    def __init__(self, grid_size=20):
        super(Snake_game, self).__init__()
        self.stepnum = 0
        self.last_food_step = 0

        self.grid_size = grid_size
        self.grid=np.zeros((self.grid_size, self.grid_size), dtype=np.uint8) + self.EMPTY
        self.grid[0, :] = self.WALL
        self.grid[:, 0] = self.WALL
        self.grid[self.grid_size-1, :] = self.WALL
        self.grid[:, self.grid_size-1] = self.WALL

        self.snake_coordinates = [(1,1), (2,1)]
        for coord in self.snake_coordinates:
            self.grid[ coord ] = self.SNAKE

        self.grid[3,3] = self.FOOD
        self.head_dist_to_food = self.grid_distance(self.snake_coordinates[-1], np.argwhere(self.grid==self.FOOD)[0])

        self.init_grid = self.grid.copy()
        self.init_snake_coordinates = self.snake_coordinates.copy()

        self.actions_aspace = spaces.Discrete(self.n_actions)

        self.observation_space = spaces.Dict(spaces= {
            "position": spaces.Box(low=0, high=(self.grid_size-1), shape=(2, ), dtype=np.int32),
            "direction": spaces.Box(low=-1, high=1, shape=(2,), dtype=np.int32),
            "grid": spaces.Box(low=0, high=3, shape=(self.grid_size, self.grid_size), dtype=np.uint8),
            "actions": self.actions_aspace,
        })



    def _get_obs(self):
        direction = np.array(self.snake_coordinates[-1]) - np.array(self.snake_coordinates[-2])
        return {
            "position": np.array(self.snake_coordinates[-1], dtype=np.int32),
            "direction": direction.astype(np.int32),
            "grid": self.grid
        }


    def step(self, action):
        direction = np.array(self.snake_coordinates[-1]) - np.array(self.snake_coordinates[-2])
        step = None
        if action == self.STRAIGHT:
            step = direction
        elif action == self.RIGHT:
            step = np.array([direction[1], -direction[0]])
        elif action == self.LEFT:
            step = np.array([-direction[1], direction[0]])

        new_coord = (np.array(self.snake_coordinates[-1]) + step).astype(np.int32)
        self.snake_coordinates.append((new_coord[0], new_coord[1]))

        new_pos = self.snake_coordinates[-1]
        new_pos_type=self.grid[new_pos]
        self.grid[new_pos] = self.SNAKE
        done = False
        reward = 0
        if new_pos_type == self.FOOD:
            reward += self.REWARD_PER_FOOD
            self.last_food_step = self.stepnum
            empty_tiles = np.argwhere(self.grid==self.EMPTY)
            if len(empty_tiles):
                new_food_pos = empty_tiles[np.random.randint(0, len(empty_tiles))]
                self.grid[new_food_pos[0], new_food_pos[1]] = self.FOOD
            else:
                done = True
        else:
            self.grid[self.snake_coordinates[0]] = self.EMPTY
            self.snake_coordinates = self.snake_coordinates[1:]
            if (new_pos_type == self.WALL) or (new_pos_type == self.SNAKE):
                done = True
                reward += self.REWARD_WALL_HIT

        head_dist_to_food_prev = self.head_dist_to_food
        self.head_dist_to_food = self.grid_distance(self.snake_coordinates[-1], np.argwhere(self.grid == self.FOOD)[0])
        if head_dist_to_food_prev > self.head_dist_to_food:
            reward += self.REWARD_PER_STEP_TOWARDS_FOOD
        elif head_dist_to_food_prev < self.head_dist_to_food:
            reward -= self.REWARD_PER_STEP_TOWARDS_FOOD

        if((self.stepnum - self.last_food_step) > self.MAX_STEPS_AFTER_FOOD):
            done = True

        self.stepnum += 1
        return self._get_obs(), reward, done, False, {}


    def reset(self, seed=None):
        self.stepnum = 0
        self.last_food_step = 0
        self.grid = self.init_grid.copy()
        self.snake_coordinates = self.init_snake_coordinates.copy()

        self.head_dist_to_food = self.grid_distance(self.snake_coordinates[-1], np.argwhere(self.grid == self.FOOD)[0])

        if seed is not None:
            np.random.seed(seed)

        obs = self._get_obs()
        info = {}

        return obs, info


    def grid_distance(self, pos1, pos2):
        return np.linalg.norm(np.array(pos1, dtype=np.float32)-np.array(pos2, dtype=np.float32))

    def snake_plot(self, plot_inline=False):
        wall_ind = (self.grid == self.WALL)
        snake_ind = (self.grid == self.SNAKE)
        food_ind = (self.grid == self.FOOD)

        Color_array=np.zeros((self.grid_size, self.grid_size,3), dtype=np.uint8)+255
        Color_array[wall_ind,:]=np.array([0,0,0])
        Color_array[snake_ind, :] = np.array([0,255,0])
        Color_array[food_ind, :] = np.array([255,0,0])
        return Color_array


    def render(self, mode='rgb_array'):
        if mode == 'console':
            print(self.grid)
        elif mode == 'rgb_array':
            return self.snake_plot()


import gym
from gym import spaces
import pygame
import numpy as np
import time
from collections import deque

import gym

from gym import spaces, logger
# from gym.envs.classic_control import renderin
from gym.utils import seeding
# from gym.envs.classic_control import rendering
from gym.wrappers import render_collection
from gymnasium.experimental.wrappers import rendering

from pythonProject.ABS.learning_process_for_final_project.gym_game.snake_game import SnakeGame

# class SnakeGameEnv(gym.Env):
#     def __init__(self):
#         self.snake_game = SnakeGame()
#
#         # Define observation space and action space based on your game requirements
#         self.observation_space = spaces.Box(low=0, high=255, shape=(480, 640, 3), dtype=np.uint8)
#         self.action_space = spaces.Discrete(4)  # Assuming there are 4 possible actions (left, right, up, down)
#
#     def reset(self, seed=None):
#         return self.snake_game.reset(seed=seed)
#
#     def step(self, action):
#         return self.snake_game.play_step(action)
#
#     def render(self, mode='human'):
#         # You can add rendering code here if needed
#         pass
#
#     def close(self):
#         pygame.quit()

class SnakeEnv(gym.Env):
    metadata = {
        "render.modes": ["human", "rgb_array"],
        "video.frames_per_second": "35"
    }

    def __init__(self, height=20, width=20, scaling_factor=6,
                 starting_position=(7, 5), snake_size=3, direction=(0, 1),
                 time_penalty=-0.01, food_reward=1, loss_penalty=-1, win_reward=10):
        self.action_space = spaces.Discrete(3)
        self.ACTIONS = ["STRAIGHT", "LEFT", "RIGHT"]
        self.observation_space = spaces.Box(0, 2, (height + 2, width + 2), dtype="uint8")
        self.viewer = None
        self.seed()

        # rewards and penalties
        self.time_penalty = time_penalty
        self.food_reward = food_reward
        self.loss_penalty = loss_penalty
        self.win_reward = win_reward
        if loss_penalty > 0 or time_penalty > 0:
            logger.warn("Values of penalties should not be positive.")

        # initialize size and position properties
        self.height = height
        self.width = width
        if height + 1 > starting_position[0] > 0 and width + 1 > starting_position[1] > snake_size:
            self.starting_position = starting_position
        else:
            raise ValueError("starting_position of snake should be in range (0 - height + 1, snake_size - width + 1)")
        self.scaling_factor = scaling_factor
        self.initial_size = snake_size
        self.snake_size = snake_size
        self.max_size = height * width
        self.state = np.zeros((height + 2, width + 2), dtype="uint8")
        self.game_over = False

        # set bounds of the environment
        self.state[:, 0] = self.state[:, -1] = 1
        self.state[0, :] = self.state[-1, :] = 1

        # initialize snake properties
        self.initial_direction = direction
        self.direction = direction
        self.snake = deque()

        # initialize position of the snake
        self._init_field(starting_position, snake_size)

        # place food on the field
        self.food = self._generate_food()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _init_field(self, starting_position, snake_size):
        y, x = starting_position
        for i in range(snake_size):
            self.state[y][x] = 1
            self.snake.appendleft((y, x))
            x -= 1

    # def _generate_food(self):
    #     y, x = self.np_random.randint(self.height), self.np_random.randint(self.width)
    #     while self.state[y][x]:
    #         y, x = self.np_random.randint(self.height), self.np_random.randint(self.width)
    #     self.state[y][x] = 2
    #
    #     return y, x

    def _generate_food(self):
        y, x = self.np_random.random(size=2)
        y, x = int(y * self.height), int(x * self.width)

        while self.state[y][x]:
            y, x = self.np_random.random(size=2)
            y, x = int(y * self.height), int(x * self.width)

        self.state[y][x] = 2
        return y, x

    def _check_for_collision(self, y, x):
        done = False
        pop = True
        reward = self.time_penalty

        if self.state[y][x]:
            if self.state[y][x] == 2:
                pop = False
                reward += self.food_reward
                self.snake_size += 1
                if self.snake_size == self.max_size:
                    reward += self.win_reward
                    self.game_over = done = True
                self.food = self._generate_food()
            else:
                reward += self.loss_penalty
                self.game_over = done = True
                pop = False

        self.state[y][x] = 1

        return reward, done, pop

    def step(self, action):
        y, x = self.snake[-1]
        if action == 0:
            y += self.direction[0]
            x += self.direction[1]
        elif action == 1:
            if self.direction[0] == 0:
                self.direction = (-self.direction[1], 0)
                y += self.direction[0]
            else:
                self.direction = (0, self.direction[0])
                x += self.direction[1]
        elif action == 2:
            if self.direction[0] == 0:
                self.direction = (self.direction[1], 0)
                y += self.direction[0]
            else:
                self.direction = (0, -self.direction[0])
                x += self.direction[1]
        else:
            raise ValueError("Action can only be 0, 1 or 2")

        if self.game_over:
            raise RuntimeError("You're calling step() even though the environment has returned done = True."
                               "You should restart the environment after receiving done = True")

        reward, done, pop = self._check_for_collision(y, x)

        if not done:
            self.snake.append((y, x))

        if pop:
            y, x = self.snake.popleft()
            self.state[y][x] = 0

        observation = self.state

        info = {
            "snake": self.snake,
            "snake_size": self.snake_size,
            "direction": self.direction,
            "food": self.food
        }

        return observation, reward, done, info

    def reset(self):
        self.game_over = False
        self.direction = self.initial_direction

        while self.snake:
            y, x = self.snake.pop()
            self.state[y][x] = 0

        self.state[self.food[0]][self.food[1]] = 0

        self._init_field(self.starting_position, self.initial_size)
        self.food = self._generate_food()
        self.snake_size = self.initial_size

        return self.state

    def _to_rgb(self, scaling_factor):
        scaled_grid = np.zeros(((self.height + 2) * scaling_factor, (self.width + 2) * scaling_factor), dtype="uint8")
        scaled_grid[:, :scaling_factor] = scaled_grid[:, -scaling_factor:] = 255
        scaled_grid[:scaling_factor, :] = scaled_grid[-scaling_factor:, :] = 255

        y, x = self.food
        scaled_y, scaled_x = y * scaling_factor, x * scaling_factor
        scaled_grid[scaled_y : scaled_y + scaling_factor, scaled_x : scaled_x + scaling_factor] = 255

        for (y, x) in self.snake:
            scaled_y, scaled_x = y * scaling_factor, x * scaling_factor
            scaled_grid[scaled_y : scaled_y + scaling_factor, scaled_x : scaled_x + scaling_factor] = 255

        img = np.empty(((self.height + 2) * scaling_factor, (self.width + 2) * scaling_factor, 3), dtype="uint8")
        img[:, :, 0] = img[:, :, 1] = img[:, :, 2] = scaled_grid

        return img

    def render(self, mode="human", close=False):
        # img = self._to_rgb(self.scaling_factor)
        # if mode == "rgb_array":
        #     return img
        # elif mode == "human":
        #     if self.viewer is None:
        #         self.viewer = render_collection.SimpleImageViewer()
        #     self.viewer.imshow(img)
        #     time.sleep(0.027)
        #
        #     return self.viewer.isopen
        if mode == "human":
            if self.viewer is None:
                pygame.init()
                self.viewer = pygame.display.set_mode(
                    ((self.width + 2) * self.scaling_factor, (self.height + 2) * self.scaling_factor))
                pygame.display.set_caption("Snake Game")

            self.viewer.fill((0, 0, 0))  # Fill the screen with black

            # Draw snake
            for (y, x) in self.snake:
                pygame.draw.rect(self.viewer, (255, 255, 255), (
                x * self.scaling_factor, y * self.scaling_factor, self.scaling_factor, self.scaling_factor))

            # Draw food
            y, x = self.food
            pygame.draw.rect(self.viewer, (255, 0, 0), (
            x * self.scaling_factor, y * self.scaling_factor, self.scaling_factor, self.scaling_factor))

            pygame.display.flip()
            pygame.time.delay(20)  # Adjust the delay to control the speed of the game

        return self.viewer

    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None


if __name__ == '__main__':
    env = gym.make('')

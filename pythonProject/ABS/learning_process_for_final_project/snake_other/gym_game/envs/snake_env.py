import gym
from gym import error, spaces, utils
from gym.utils import seeding
from pythonProject.ABS.learning_process_for_final_project.snake_other.gym_game.envs.snake import SnakeGame
import pygame
from pygame.locals import *
import numpy as np


class SnakeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.observation_space = spaces.Box(low=0, high=3, shape=[150, 150])
        self._action_set = [x for x in range(4)]
        self.action_space = spaces.Discrete(4)
        self._s = SnakeGame()

    def step(self, action):
        state, reward, done, info = self._s.step(action)
        return state, reward, done, info

    def reset(self):
        self._s = SnakeGame()
        return self._s.reset()

    def render(self, mode='human'):
        if mode == 'human':
            self._render_gui()
        elif mode == 'rgb_array':
            return self._get_image()

    def _render_gui(self):
        # Initialize pygame and set up the display
        pygame.init()
        window_size = (640, 480)
        window_surface = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Snake Game")

        # Your rendering logic goes here
        # Draw the game state using pygame functions

        pygame.display.flip()

        # Event handling, e.g., for closing the window
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

    def _get_image(self):
        # Your logic for obtaining the game state as an RGB array
        # Return the RGB array
        return np.zeros((480, 640, 3), dtype=np.uint8)

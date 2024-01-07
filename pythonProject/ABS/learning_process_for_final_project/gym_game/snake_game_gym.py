import gym
from gym import spaces
from snake_game import SnakeGame  # Update this import based on your file structure
import numpy as np


class SnakeGameEnv(gym.Env):
    def __init__(self):
        self.snake_game = SnakeGame()

        # Define Gym spaces
        self.observation_space = spaces.Box(low=0, high=255, shape=(self.snake_game.w, self.snake_game.h, 3), dtype=np.uint8)
        self.action_space = spaces.Discrete(4)  # Assuming 4 possible directions

    def reset(self):
        obs = self.snake_game._get_observation()
        return obs, {}

    def step(self, action):
        obs, reward, game_over, _ = self.snake_game.play_step(action)
        return obs, reward, game_over, {}
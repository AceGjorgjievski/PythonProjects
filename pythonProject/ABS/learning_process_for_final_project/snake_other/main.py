import gym
import pythonProject.ABS.learning_process_for_final_project.snake_other.gym_game
from pythonProject.ABS.learning_process_for_final_project.snake_other.gym_game.envs.snake import SnakeGame
import warnings
import gym_snake_game


if __name__ == '__main__':
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    env = gym.make('Snake-v0')
    env.reset()



    # env.render()

    print()

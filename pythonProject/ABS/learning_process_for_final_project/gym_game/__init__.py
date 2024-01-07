# main.py
from gym.envs.registration import register

register(
    id='Snake-v55',
    # entry_point='PycharmProjects.pythonProject.ABS.learning_process_for_final_project.gym_game.custom_env:SnakeGameEnv',
    # entry_point='custom_env:SnakeGameEnv',
    entry_point='custom_env:SnakeEnv',
)

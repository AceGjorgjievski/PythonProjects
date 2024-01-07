from stable_baselines3.common.env_checker import check_env
from pythonProject.ABS.learning_process_for_final_project.snake_one.snake_game_env import Snake_game



env = Snake_game()

check_env(env, warn=True)







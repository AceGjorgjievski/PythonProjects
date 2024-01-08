import os
from stable_baselines3 import PPO, A2C
from snakeenv import *


def train_and_save_ppo_model(env, model, save_path, save_intervals):
    env.render_mode = None
    for interval in save_intervals:
        model.learn(total_timesteps=interval)
        model.save(os.path.join(save_path, f'ppo_path_{interval}'))

def test_ppo_model(env, model_path, timestamp):
    model = PPO.load(os.path.join(model_path, f'ppo_path_{timestamp}'), env=env)
    env.render_mode = 'human'
    model.learn(total_timesteps=testing_total_timesteps)

def train_and_save_a2c_model(env, model, save_path, save_intervals):
    env.render_mode = None
    for interval in save_intervals:
        model.learn(total_timesteps=interval)
        model.save(os.path.join(save_path, f'a2c_path_{interval}'))

def test_a2c_model(env, model_path, timestamp):
    model = A2C.load(os.path.join(model_path, f'a2c_path_{timestamp}'), env=env)
    env.render_mode = 'human'
    model.learn(total_timesteps=testing_total_timesteps)


if __name__ == '__main__':
    env = SnakeEnv()

    Log_path = os.path.join('Training', 'Logs')
    A2C_path = os.path.join('Training', 'Saved models')
    PPO_path = os.path.join('Training', 'Saved models')

    print(A2C_path, Log_path)

    training_total_timesteps = 999
    testing_total_timesteps = 200

    model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=Log_path)

    save_intervals = [50000, 100000, 250000, 500000, 1000000]
    save_intervals_2 = [500, 1000, 2500, 5000]

    # choose what to train and what to test :)

    # train_and_save_ppo_model(env, model, A2C_path, save_intervals)
    # train_and_save_a2c_model(env, model, A2C_path, save_intervals)

    # test_ppo_model(env, PPO_path, save_intervals[-1])
    # test_a2c_model(env, PPO_path, save_intervals[-1])

    env.close()

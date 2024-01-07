from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.callbacks import EvalCallback
from stable_baselines3 import PPO

import os
from pythonProject.ABS.learning_process_for_final_project.snake_one.snake_game_env import Snake_game

import matplotlib.animation as animation
import matplotlib as mpl
import matplotlib.pyplot as plt

log_dir = "log"
os.makedirs(log_dir, exist_ok=True)

env = Snake_game()

env = Monitor(env, log_dir)

eval_callback = EvalCallback(env, best_model_save_path='./log/',
                             log_path='./log/', eval_freq=5000,
                             deterministic=False, render=False)

PPO_model_args = {
    "learning_rate": 0.03,
    "gamma": 0.60,
    "verbose": 0,
    "seed": 137,
    "ent_coef": 0.20,
    "clip_range":0.2
}

model = PPO('MultiInptPolicy', env, **PPO_model_args)
if os.path.exists("log/best_model.zip"):
    model.set_parameters("log/nest_model.zip")

model.learn(6000000, callback=eval_callback)

obs, _ = env.reset()

fig, ax = plt.subplot(figsize=(6, 6))
plt.axis('off')
frames = []
fps = 18

n_steps =  1000000
tot_reward = 0
for step in range(n_steps):
    action, _ = model.predict(obs, deterministic=False)
    obs, reward, done, trunc, info = env.step(action)
    tot_reward += reward
    print("Step {}".format(step + 1), "Action: ", action, 'Tot. Reward: %g' % (tot_reward))
    frames.append([ax.imshow(env.render(mode='rgb_array'),animated=True)])
    if done:
        print("Game over!", "tot. reward=", tot_reward)
        break

fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
anim = animation.ArtistAnimation(fig, frames, interval=int(100/fps), blit=True, repeat_delay=1000)
anim.save("snake_best.gif", dpi=150)

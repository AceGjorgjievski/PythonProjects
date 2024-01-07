import gym
# main.py
import gym
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pickle
import warnings
import random
import pythonProject.ABS.learning_process_for_final_project.gym_game

def run(episodes, is_training=True, render=False):

    # env = gym.make('FrozenLake-v1', map_name="4x4", is_slippery=True, render_mode='human' if render else None)
    env = gym.make('Snake-v55')

    num_states = env.observation_space.shape[0]
    num_actions = env.action_space.n
    if(is_training):
        q = np.zeros((num_states, num_actions))
        # q = np.zeros((env.observation_space.n, env.action_space.n)) # init a 64 x 4 array
    else:
        f = open('frozen_lake8x8.pkl', 'rb')
        q = pickle.load(f)
        f.close()

    learning_rate_a = 0.9 # alpha or learning rate
    discount_factor_g = 0.9 # gamma or discount rate. Near 0: more weight/reward placed on immediate state. Near 1: more on future state.
    epsilon = 1         # 1 = 100% random actions
    epsilon_decay_rate = 0.0001        # epsilon decay rate. 1/0.0001 = 10,000
    rng = np.random.default_rng()   # random number generator

    rewards_per_episode = np.zeros(episodes)

    for i in range(episodes):
        state = env.reset()[0]  # states: 0 to 63, 0=top left corner,63=bottom right corner
        terminated = False      # True when fall in hole or reached goal
        truncated = False       # True when actions > 200

        while(not terminated):
            if is_training and random.uniform(0,1) < epsilon:
                action = env.action_space.sample() # actions: 0=left,1=down,2=right,3=up
            else:
                action = np.argmax(q[state]) % env.action_space.n

            new_state,reward,terminated,truncated = env.step(action)

            if is_training:
                q[state,action] = q[state,action] + learning_rate_a * (
                    reward + discount_factor_g * np.max(q[new_state,:]) - q[state,action]
                )

            state = new_state
            # env.render()

            if i > 9995:
                env.render()

        epsilon = max(epsilon - epsilon_decay_rate, 0)

        print(f"Episode: {i}, Reward: {reward}, Size: {truncated['snake_size']}")

        if(epsilon==0):
            learning_rate_a = 0.0001

        if reward == 1:
            rewards_per_episode[i] = 1

    env.close()

    sum_rewards = np.zeros(episodes)
    for t in range(episodes):
        sum_rewards[t] = np.sum(rewards_per_episode[max(0, t-100):(t+1)])
    plt.plot(sum_rewards)
    plt.savefig('frozen_lake8x8.png')

    if is_training:
        f = open("frozen_lake8x8.pkl","wb")
        pickle.dump(q, f)
        f.close()



if __name__ == '__main__':
    # env = gym.make('Snake-v55')
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    print()
    run(100000, is_training=True, render=False)



import sys
import numpy as np
import math
import random
import warnings

import gym
import pythonProject.ABS.learning_process_for_final_project.gym_game

def simulate_before(q_table):
    global epsilon, epsilon_decay
    ok = False
    save_interval = [100000, 200000, 30000, 40000, 50000,
                     60000, 70000, 80000, 90000]
    for episode in range(MAX_EPISODES):

        state = env.reset()
        total_reward = 0

        done = False
        if episode == 5000:
            ok = True

        while not done:

            # In the beginning, do random action to learn
            if random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()
            else:
                action = np.argmax(q_table[state])

            # Do action and get result
            next_state, reward, done, _ = env.step(action)
            total_reward += reward

            # Get correspond q value from state, action pair
            q_value = q_table[state, action]
            best_q = np.max(q_table[next_state, :])

            # Q(state, action) <- (1 - a)Q(state, action) + a(reward + rmaxQ(next state, all actions))
            q_table[state, action] = (1 - learning_rate) * q_value + learning_rate * (reward + gamma * best_q)

            # Set up for the next iteration
            state = next_state

            # Draw games
            # env.render()


            # When episode is done, print reward
            if done :
                    # t >= MAX_TRY - 1:
                print(reward)
                print("Episode %d finished after %i time steps with total reward = %f." % (episode, reward, total_reward))
                if episode in save_interval:
                    np.save(f'q_table_episode_{episode}', q_table)

                break

        # exploring rate decay
        if epsilon >= 0.005:
            epsilon *= epsilon_decay


    return q_table

def simulate_after(q_table):
    for ep in range(MAX_EPISODES):
        state = env.reset()
        done = False
        while not done:
            action = np.argmax(q_table[state])
            next_state, reward, done, _ = env.step(action)
            state = next_state
            env.render()

if __name__ == '__main__':
    env = gym.make('Snake-v55')
    env.reset()
    print(env)
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    MAX_EPISODES = 20000
    MAX_TRY = 1000
    epsilon = 1
    epsilon_decay = 0.999
    learning_rate = 0.1

    gamma = 0.6
    num_box = tuple((env.observation_space.high + np.ones(env.observation_space.shape)).astype(int))

    flattened_arrays = [arr.flatten()[:env.action_space.n] for arr in num_box]

    expected_shape = (env.action_space.n,)
    for arr in flattened_arrays:
        if arr.shape != expected_shape:
            raise ValueError(f"Flattened array has incorrect shape, expected {expected_shape}, got {arr.shape}")

    q_table = np.zeros((len(flattened_arrays), env.action_space.n))

    new_q = np.zeros((env.observation_space.shape[0], env.action_space.n))

    for i, arr in enumerate(flattened_arrays):
        q_table[i, :] = arr

    print("q_table before simulate:", q_table)
    # q_table = simulate_before(q_table)
    print("q_table after simulate:", q_table)
    q_table_path = 'latest_snake_3.npy'

    # np.save(q_table_path, q_table)

    # new_q = np.load('snake.npy')
    latest_q = np.load(q_table_path)



    latest2_q = simulate_before(new_q)
    np.save('new_q_1',latest2_q)



    print()


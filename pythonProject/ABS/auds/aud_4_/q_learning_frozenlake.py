import gym
import time
import os
from q_learning import get_action, get_best_action, random_q_table, calculate_new_q_value

if __name__ == '__main__':
    env = gym.make('FrozenLake-v1')

    num_actions = env.action_space.n
    num_states = env.observation_space.n

    q_table = random_q_table(-1, 0, (num_states, num_actions))

    num_episodes = 10
    num_steps_per_episode = 15
    learning_rate = 0.1
    discount_factor = 0.1
    epsilon = 0.25
    epsilon_min = 0.1
    decay = 0.05

    for episode in range(num_episodes):
        state = env.reset()
        done = False
        while not done:
            if isinstance(state, tuple):
                state = state[0]
            action = get_action(env, q_table, state, epsilon)
            new_state, reward, done, info, _ = env.step(action)
            new_q = calculate_new_q_value(q_table, state, new_state, action, reward, learning_rate, discount_factor)
            q_table[state, action] = new_q
            state = new_state
        if epsilon > epsilon_min:
            epsilon -= decay

    state = env.reset()
    env.render()
    done = False
    while not done:
        new_action = get_best_action(q_table, state)
        state, reward, done, info, _ = env.step(new_action)
        if isinstance(state, tuple):
            state = state[0]
        print(reward)
        env.render()
        time.sleep(0.5)
        os.system('cls')

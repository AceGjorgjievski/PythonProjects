import numpy as np
import gym
from pythonProject.ABS.auds.aud_3_.q_learning import random_q_table, get_best_action, calculate_new_q_value


class QLearningAgent:
    def __init__(self, env, num_episodes=100, num_steps_per_episode=15,
                 learning_rate=0.1, discount_factor=0.1, initial_epsilon=0.25,
                 epsilon_min=0.1, decay_rate=0.995):
        self.env = env
        self.num_episodes = num_episodes
        self.num_steps_per_episode = num_steps_per_episode
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.initial_epsilon = initial_epsilon
        self.epsilon_min = epsilon_min
        self.decay_rate = decay_rate
        self.epsilon = initial_epsilon
        self.num_actions = env.action_space.n
        self.num_states = env.observation_space.n
        self.q_table = random_q_table(-1, 0, (self.num_states, self.num_actions))

    def explore_exploit(self, state):
        if np.random.rand() < self.epsilon:
            return self.env.action_space.sample()
        else:
            return get_best_action(self.q_table, state)

    def train(self):
        for episode in range(self.num_episodes):
            state = self.env.reset()
            done = False
            while not done:
                if isinstance(state, tuple):
                    state = state[0]
                action = self.explore_exploit(state)
                new_state, reward, done, _, _ = self.env.step(action)
                new_q = calculate_new_q_value(self.q_table, state, new_state, action, reward,
                                              self.learning_rate, self.discount_factor)
                self.q_table[state, action] = new_q
                state = new_state

                # print(f"State: {state}")
                # print(f"Action: {action}")
                # print(f"Reward: {reward}")
                # print(f"Done: {done}")
                print()
            print(f"Episode: {episode}")

            # Exponential decay for epsilon
            self.epsilon = max(self.epsilon_min, self.epsilon * self.decay_rate)
            print()

    def play(self):
        state = self.env.reset()
        self.env.render()
        self.env.close()


if __name__ == '__main__':
    env1 = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False, render_mode='human')

    agent = QLearningAgent(env1)
    agent.train()
    agent.play()

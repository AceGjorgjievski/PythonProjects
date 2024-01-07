import gym
import numpy as np
from q_learning import random_q_table


def get_discrete_state(state, low_value, window_size):
    normalized_state = (state[0] - low_value) / window_size
    discrete_state = np.floor(normalized_state).astype(int)
    return tuple(discrete_state)


if __name__ == '__main__':
    env = gym.make('MountainCar-v0', render_mode='human')
    state = env.reset()
    env.render()
    print()

    num_actions = env.action_space.n

    observation_space_size = [5, 5]
    observation_space_low_value = env.observation_space.low
    observation_space_high_value = env.observation_space.high

    observation_window_size = (observation_space_high_value - observation_space_low_value) / observation_space_size

    q_table = random_q_table(-1, 0, (observation_space_size + [num_actions]))

    state = env.reset()

    discrete_state = get_discrete_state(state, observation_space_low_value, observation_window_size)

    env.render()
    print()
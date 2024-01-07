import gymnasium as gym
from pythonProject.ABS.auds.aud_3_.q_learning import *

from pythonProject.ABS.auds.auds_5_dqn.deep_q_learning import DQN, DDPG
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import MeanSquaredError
from tensorflow.keras.optimizers import Adam
import warnings

def build_model(state_space_shape, num_actions, learning_rate):
    model = Sequential()
    model.add(Dense(32, activation='relu', input_dim=state_space_shape))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(num_actions, activation='linear'))

    model.compile(Adam(learning_rate=learning_rate), loss=MeanSquaredError())

    return model


if __name__ == '__main__':

    env1 = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False, render_mode='human')
    # env1 = gym.make('Snake-v55')
    env1.reset()
    env1.render()

    warnings.filterwarnings("ignore", category=DeprecationWarning)

    print(np.__version__)

    # state, reward, done, info, _ = env1.step(0)

    num_actions = env1.action_space.n
    num_states = env1.observation_space.n

    q_table = random_q_table(-1, 0, (num_states, num_actions))

    # num_episodes = 100
    # num_steps_per_episode = 15
    # learning_rate = 0.1
    # discount_factor = 0.1
    # epsilon = 0.25
    # epsilon_min = 0.1
    # decay = 0.05
    #
    #
    # for episode in range(num_episodes):
    #     state = env1.reset()
    #     done = False
    #     while not done:
    #         if isinstance(state, tuple):
    #             state = state[0]
    #         action = get_best_action(q_table, state)
    #         new_state, reward, done, info, _ = env1.step(action)
    #         new_q = calculate_new_q_value(q_table, state, new_state, action, reward, learning_rate, discount_factor)
    #         q_table[state, action] = new_q
    #         state = new_state
    #         print(f"State: {state}")
    #         print(f"Action: {action}")
    #         print(f"Reward: {reward}")
    #         print(f"Done: {done}")
    #         print(f"Q-table: {q_table}")
    #         print()
    #     if epsilon > epsilon_min:
    #         epsilon -= decay
    #         print()

    num_episodes = 100
    num_steps_per_episode = 15
    learning_rate = 0.1
    discount_factor = 0.1
    initial_epsilon = 0.25
    epsilon_min = 0.1
    decay_rate = 0.995  # Adjust this decay rate

    # num_episodes = 50
    # learning_rate = 0.01
    # discount_factor = 0.99
    batch_size = 128
    memory_size = 1024
    # epsilon = 0.1

    epsilon = initial_epsilon

    state_space_size = env1.observation_space.n
    num_actions = env1.action_space.n

    model = build_model(state_space_size, num_actions, learning_rate)
    model.summary()

    target_model = build_model(state_space_size, num_actions, learning_rate)


    agent = DDPG(state_space_size, num_actions, model, target_model,
                learning_rate, discount_factor, batch_size, memory_size)

    agent.build_model()
    for episode in range(num_episodes):
        state = env1.reset()
        done = False
        while not done:
            if isinstance(state, tuple):
                state = state[0]
            action = get_best_action(q_table, state)

            # Exploration-exploitation logic
            if np.random.rand() < epsilon:
                action = env1.action_space.sample()

            new_state, reward, done, info, _ = env1.step(action)
            agent.update_memory(state, action, reward, new_state, done)
            new_q = calculate_new_q_value(q_table, state, new_state, action, reward, learning_rate, discount_factor)
            q_table[state, action] = new_q
            state = new_state

            print(f"State: {state}")
            print(f"Action: {action}")
            print(f"Reward: {reward}")
            print(f"Done: {done}")
            print(f"Q-table: {q_table}")
            print()
        agent.train()
        if episode % 5 == 0:
            agent.update_target_model()
        if episode % 20 == 0:
            agent.save('frozen', episode)

        # Exponential decay for epsilon
        epsilon = max(epsilon_min, epsilon * decay_rate)
        print()

    state = env1.reset()
    env1.render()
    env1.close()

    # for episode in range(num_episodes):
    #     state = env1.reset()
    #     done = False
    #     env1.render()
    #
    #     while not done:
    #         env1.render()
    #         action = agent.get_action(state, epsilon)
    #         new_state, reward, done, info, _ = env1.step(action)
    #         agent.update_memory(state, action, reward, new_state, done)
    #         state = new_state
    #
    #     agent.train()
    #     agent.update_target_model()




"*** TAXIii ***"

# env2 = gym.make('Taxi-v3', render_mode="human")
# env2.reset()
# env2.render()

# state, reward, done, info = env2.step(0)

# action = env2.action_space.sample()
# state, reward, done, info, other = env2.step(action)
#
# print("State:", state)
# print("Reward:", reward)
# print("Done:", done)
# print("Info:", info)
# env2.close()

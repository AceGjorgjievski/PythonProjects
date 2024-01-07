import gym
from pythonProject.ABS.auds.aud_2_MDP.mdp.mdp import policy_iteration
from pythonProject.ABS.auds.aud_2_MDP.mdp.mdp_v2 import policy_iteration
import numpy as np


if __name__ == '__main__':
    env = gym.make('Taxi-v3', render_mode="rgb_array")

    env.reset()
    env.render()

    policy, value = policy_iteration(env, 6, 500, discount_factor=0.9)

    print(f"Policy: {policy}")
    print(f"Value: {value}")

    state = env.reset() # za 1ta iteracija mi dava rechnik, a potoa samo int
    #pravam state[0] i toa pominuva za 1ta iteracija, a potoa ne mozhe na 0 subscriptable
    env.render()
    done = False
    while not done: # ista prikazna i za kaj taxi
        new_action = np.argmax(policy[state])
        state, reward, done, _, _ = env.step(new_action)
        print(f"Reward: {reward}")
        env.render()

    print()





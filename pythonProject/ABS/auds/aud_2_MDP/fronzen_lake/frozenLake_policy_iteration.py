import gym
# from pythonProject.ABS.auds.aud_2_MDP.mdp.mdp import policy_iteration
from pythonProject.ABS.auds.aud_2_MDP.mdp.mdp import policy_iteration


if __name__ == '__main__':
    env = gym.make('FrozenLake-v1', render_mode="rgb_array")

    env.reset()
    env.render()

    print()

    policy, value = policy_iteration(env, 4, 16, discount_factor=0.9)
    print(f"Policy: {policy}")
    print(f"Value: {value}")

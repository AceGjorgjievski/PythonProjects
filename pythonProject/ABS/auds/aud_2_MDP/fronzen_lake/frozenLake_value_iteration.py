import gym
from pythonProject.ABS.auds.aud_2_MDP.mdp.mdp import value_iteration
from pythonProject.ABS.auds.aud_2_MDP.mdp.mdp import value_iteration
import numpy as np

if __name__ == '__main__':

    env = gym.make('FrozenLake-v1')

    env.reset()
    """
    ja vrakja okolinata vo pochetnata sostojba,
    dobro e ova da go napravime na samiot pochetok za 
    da bideme sigurni deka nema da imame nekoi sluchajni vrednosti,
    pr. deka ne bi pochnale na nekoja pozicija vo sredina tuku deka sekogash
    kje pochneme od pochetnata sostojba t.e. 'start'
    """
    env.render()
    """
    vizuelen prikaz na okolinata
    """

    print()

    policy1, value1 = value_iteration(env, discount_factor=0.9)
    policy2, value2 = value_iteration(env, env.action_space.n,
                                      env.observation_space.n, discount_factor=0.9)
    policy2, value2 = value_iteration(env, 4,
                                      16, discount_factor=0.9)

    # discorunt factor?

    print(f"Policy: {policy2}")
    print(f"Value: {value2}")
    """
    error mi dava za nS za policy1
    """

    # pochetna sostojba od ooklinata frozen lake
    state = env.reset() # za 1ta iteracija mi dava rechnik, a potoa samo int
    #pravam state[0] i toa pominuva za 1ta iteracija, a potoa ne mozhe na 0 subscriptable
    env.render()
    done = False
    while not done:
        new_action = np.argmax(policy2[state])
        state, reward, done, _, _ = env.step(new_action)
        print(f"Reward: {reward}")
        env.render()

    print()





import gym

if __name__ == '__main__':
    env = gym.make('MountainCar-v0')
    env.reset()
    env.render()

    print()
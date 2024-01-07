import gymnasium as gym

if __name__ == '__main':
    env = gym.make('MountainCar-v0')
    state = env.reset()

    done = False
    while not done:
        action = env.action_space.sample()  # Replace with your desired action selection logic
        new_state, reward, done, _ = env.step(action)
        env.render()
        print("State:", new_state)
        print("Reward:", reward)

    env.close()  # Close the rendering window when you're done

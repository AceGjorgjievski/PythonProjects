from gym.envs.registration import register

register(
    id='snake-v0',
    entry_point='gym_game.envs.snake_env:SnakeEnv',
)
register(
    id='snake-tiled-v0',
    entry_point='gym_game.envs.tiled:SnakeEnvTiled',
)

import random
import time
import pygame
import gym
from gym import spaces
import numpy as np

WIDTH, HEIGHT = 630, 480
ROW, COLUMN = 30, 40
FPS = 30
GRID_SIZE = 15


def snake_generating(SnakeList, SnakeDir):
    if len(SnakeList) == 0:
        # head
        x = random.randrange(3, COLUMN - 1)
        y = random.randrange(3, ROW - 1)
        SnakeList.append([x, y])

        # body
        SnakeList.append(random.choice([[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]))

        # tail
        x = SnakeList[-1][0]
        y = SnakeList[-1][1]
        temp = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]
        temp.remove([SnakeList[0][0], SnakeList[0][1]])
        SnakeList.append(random.choice(temp))

    if len(SnakeDir) == 0:
        # initail direction
        dir_list = ['right', 'left', 'up', 'down']
        if SnakeList[0][0] > SnakeList[1][0]:
            dir_list.remove('left')
        if SnakeList[0][1] > SnakeList[1][1]:
            dir_list.remove('up')
        if SnakeList[0][0] < SnakeList[1][0]:
            dir_list.remove('right')
        if SnakeList[0][1] < SnakeList[1][1]:
            dir_list.remove('down')
        SnakeDir = random.choice(dir_list)

    return SnakeList, SnakeDir


def apple_generating(SnakeList, ApplePos):
    if len(ApplePos) == 0:
        # apple generating
        x = random.randrange(1, COLUMN + 1)
        y = random.randrange(1, ROW + 1)
        while [x, y] in SnakeList:
            x = random.randrange(1, COLUMN + 1)
            y = random.randrange(1, ROW + 1)
        ApplePos = [x, y]

    return ApplePos


def updating_snake(SnakeDir, SnakeList, SnakeEat, SnakeDead):
    if not SnakeDead:

        if not SnakeEat:
            SnakeList.pop(-1)
        else:
            SnakeEat = False

        if SnakeDir == 'up':
            SnakeList.insert(0, [SnakeList[0][0], SnakeList[0][1] - 1])
        if SnakeDir == 'down':
            SnakeList.insert(0, [SnakeList[0][0], SnakeList[0][1] + 1])
        if SnakeDir == 'right':
            SnakeList.insert(0, [SnakeList[0][0] + 1, SnakeList[0][1]])
        if SnakeDir == 'left':
            SnakeList.insert(0, [SnakeList[0][0] - 1, SnakeList[0][1]])
    return SnakeList, SnakeEat


def collision(SnakeList, ApplePos, SnakeDir, SnakeEat, SnakeDead, Score):
    # apple and snake head
    if SnakeList[0] == ApplePos:
        SnakeEat = True
        Score += 1
        ApplePos = []

    # snake head and wall
    if SnakeList[0][1] == 1 and SnakeDir == 'up':
        SnakeDead = True
    if SnakeList[0][1] == 30 and SnakeDir == 'down':
        SnakeDead = True
    if SnakeList[0][0] == 1 and SnakeDir == 'left':
        SnakeDead = True
    if SnakeList[0][0] == 40 and SnakeDir == 'right':
        SnakeDead = True

    # snake head and snake body
    if SnakeList[0] in SnakeList[1:]:
        SnakeDead = True

    return SnakeEat, SnakeDead, Score, ApplePos


class SnakeEnv(gym.Env):
    def __init__(self):
        self.render_mode = None
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=40, shape=(5,), dtype=np.float32)
        self.display = None

    def step(self, action):
        self.snake_eat, self.snake_dead, self.score, self.apple_pos = collision(self.snake_list, self.apple_pos,
                                                                                self.snake_dir, self.snake_eat,
                                                                                self.snake_dead,
                                                                                self.score)
        self.snake_list, self.snake_eat = updating_snake(self.snake_dir, self.snake_list, self.snake_eat,
                                                         self.snake_dead)
        self.apple_pos = apple_generating(self.snake_list, self.apple_pos)

        # snake direction
        if action == 0:
            self.snake_dir = 'up'
        elif action == 1:
            self.snake_dir = 'down'
        elif action == 2:
            self.snake_dir = 'right'
        elif action == 3:
            self.snake_dir = 'left'

        # observation
        self.observation = [self.snake_list[0][0], self.snake_list[0][1], self.apple_pos[0], self.apple_pos[1], action]
        self.observation = np.array(self.observation)

        if self.snake_dead:
            self.done = True

        # reward
        # A: death punoshment
        if self.done:
            reward_a = -100
        else:
            reward_a = 0

        # B: eating apple
        if self.prev_score < self.score:
            reward_b = 10
            self.prev_score = self.score
            self.timestep_passed_eating = 0
            self.valid_timestep_to_eat += 1
        else:
            reward_b = 0
            self.timestep_passed_eating += 1

        # C: distance reward and punishment
        self.dist = abs(self.snake_list[0][0] - self.apple_pos[0]) + abs(self.snake_list[0][1] - self.apple_pos[1])
        if self.dist > self.prev_dist:
            reward_c = -1
        elif self.dist < self.prev_dist:
            reward_c = 1
        else:
            reward_c = 0
        self.prev_dist = self.dist

        # D: punishment for wasting time
        reward_d = -self.timestep_passed_eating // self.valid_timestep_to_eat

        self.reward = reward_a + reward_b + reward_c + reward_d

        self.info = {}

        if self.render_mode == 'human':
            self.render()

        return self.observation, self.reward, self.done, self.info

    def reset(self):
        self.done = False
        self.snake_dir = ''
        self.snake_list = []
        self.apple_pos = []
        self.snake_eat = False
        self.snake_dead = False

        # snake and apple initialization
        self.snake_list, self.snake_dir = snake_generating(self.snake_list, self.snake_dir)
        self.apple_pos = apple_generating(self.snake_list, self.apple_pos)

        # observation
        if self.snake_dir == 'up':
            self.numerical_dir = 0
        elif self.snake_dir == 'down':
            self.numerical_dir = 1
        elif self.snake_dir == 'right':
            self.numerical_dir = 2
        elif self.snake_dir == 'left':
            self.numerical_dir = 3

        self.observation = [self.snake_list[0][0], self.snake_list[0][1], self.apple_pos[0], self.apple_pos[1],
                            self.numerical_dir]
        self.observation = np.array(self.observation)

        # reward
        self.reward = 0
        self.score = 0
        self.prev_score = 0
        self.dist = abs(self.snake_list[0][0] - self.apple_pos[0]) + abs(self.snake_list[0][1] - self.apple_pos[1])
        self.prev_dist = self.dist
        self.valid_timestep_to_eat = 30 + 40 + 3
        self.timestep_passed_eating = 0

        # Initialize display
        pygame.init()
        pygame.display.set_caption('Snake RL')
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial_bold', 30)

        if self.render_mode == 'human':
            self.render()

        return self.observation  # reward, done, info can't be included

    # def reset(self):
    #     self.done = False
    #     self.snake_dir = ''
    #     self.snake_list = []
    #     self.apple_pos = []
    #     self.snake_eat = False
    #     self.snake_dead = False
    #
    #     # snake and apple initialazation
    #     self.snake_list, self.snake_dir = snake_generating(self.snake_list, self.snake_dir)
    #     self.apple_pos = apple_generating(self.snake_list, self.apple_pos)
    #
    #     # obseration
    #     if self.snake_dir == 'up':
    #         self.numerical_dir = 0
    #     elif self.snake_dir == 'down':
    #         self.numerical_dir = 1
    #     elif self.snake_dir == 'right':
    #         self.numerical_dir = 2
    #     elif self.snake_dir == 'left':
    #         self.numerical_dir = 3
    #
    #     self.observation = [self.snake_list[0][0], self.snake_list[0][1], self.apple_pos[0], self.apple_pos[1],
    #                         self.numerical_dir]
    #     self.observation = np.array(self.observation)
    #
    #     # reward
    #     self.reward = 0
    #     self.score = 0
    #     self.prev_score = 0
    #     self.dist = abs(self.snake_list[0][0] - self.apple_pos[0]) + abs(self.snake_list[0][1] - self.apple_pos[1])
    #     self.prev_dist = self.dist
    #     self.valid_timestep_to_eat = 30 + 40 + 3
    #     self.timestep_passed_eating = 0
    #
    #     if self.render_mode == 'human':
    #         pygame.init()
    #         pygame.display.set_caption('Snake RL')
    #         self.display = pygame.display.set_mode((WIDTH, HEIGHT))
    #         self.clock = pygame.time.Clock()
    #         self.font = pygame.font.SysFont('Arial_bold', 380)
    #
    #         self.render()
    #
    #     return self.observation  # reward, done, info can't be included

    def render(self, render_mode='human'):
        # draw
        self.display.fill((67, 70, 75))

        # borders
        pygame.draw.rect(self.display, 'WHITE', (15, 15, 40 * 15, 1))
        pygame.draw.rect(self.display, 'WHITE', (15, 31 * 15, 40 * 15, 1))
        pygame.draw.rect(self.display, 'WHITE', (41 * 15, 15, 1, 30 * 15))
        pygame.draw.rect(self.display, 'WHITE', (15, 15, 1, 30 * 15))

        # score
        # if self.snake_dead:
        #     img = self.font.render(str(self.score), True, (125, 85, 85))
        # else:
        #     img = self.font.render(str(self.score), True, (57, 60, 65))
        # self.display.blit(img, img.get_rect(center=(20 * 15 + 15, 15 * 15 + 15)).topleft)
        score_text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.display.blit(score_text, (WIDTH - score_text.get_width() - 20, 20))

        # apple
        if len(self.apple_pos) > 0:
            pygame.draw.rect(self.display, 'RED', (self.apple_pos[0] * 15 + 1, self.apple_pos[1] * 15 + 1, 13, 13))

        # snake body
        # for part in self.snake_list[1:]:
        #     pygame.draw.rect(self.display, (180, 180, 180), (part[0] * 15 + 1, part[1] * 15 + 1, 13, 13))
        for part in self.snake_list[1:]:
            pygame.draw.rect(self.display, (0, 255, 127),
                             (part[0] * GRID_SIZE + 1, part[1] * GRID_SIZE + 1, GRID_SIZE - 3, GRID_SIZE - 3))
        # snake head
        # pygame.draw.rect(self.display, 'WHITE',
        #                  (self.snake_list[0][0] * 15 + 1, self.snake_list[0][1] * 15 + 1, 13, 13))
        pygame.draw.rect(self.display, (0, 255, 127),
                         (self.snake_list[0][0] * GRID_SIZE + 1, self.snake_list[0][1] * GRID_SIZE + 1, GRID_SIZE - 2,
                          GRID_SIZE - 2))

        pygame.display.update()
        self.clock.tick(FPS)

        # optional
        if self.done:
            time.sleep(0.5)

    def close(self):
        pygame.quit()
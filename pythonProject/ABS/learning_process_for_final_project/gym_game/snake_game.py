import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()
font = pygame.font.Font('../arial.ttf', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

# rgb colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)
GREEN1 = (0, 102, 0)
GREEN2 = (0, 255, 0)

BLOCK_SIZE = 20
SPEED = 20

class SnakeGame:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h

        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()

        self.direction = Direction.RIGHT

        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.food = None
        self._place_food()

    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def reset(self, seed=None):
        self.direction = Direction.RIGHT

        # Reset the snake to its initial position
        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [
            self.head,
            Point(self.head.x - BLOCK_SIZE, self.head.y),
            Point(self.head.x - (2 * BLOCK_SIZE), self.head.y),
        ]

        self.score = 0
        self._place_food()

        return self._get_observation()

    def play_step(self, action):
        self._handle_events(action)
        self._move(self.direction)
        self.snake.insert(0, self.head)

        game_over = self._is_collision()
        if game_over:
            return self._get_observation(), -1, game_over, {}  # Return -1 as the reward for game over

        if self.head == self.food:
            self.score += 1
            self._place_food()
            reward = 1  # Positive reward for getting the food
        else:
            self.snake.pop()
            reward = 0  # Small positive reward for staying alive

        self._update_ui()
        self.clock.tick(SPEED)

        return self._get_observation(), reward, game_over, {}

    def _handle_events(self, action):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if action == 0 and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
        elif action == 1 and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT
        elif action == 2 and self.direction != Direction.DOWN:
            self.direction = Direction.UP
        elif action == 3 and self.direction != Direction.UP:
            self.direction = Direction.DOWN

    def _is_collision(self):
        if (
            self.head.x > self.w - BLOCK_SIZE
            or self.head.x < 0
            or self.head.y > self.h - BLOCK_SIZE
            or self.head.y < 0
        ):
            return True
        if self.head in self.snake[1:]:
            return True

        return False

    def _update_ui(self):
        self.display.fill(BLACK)

        for pt in self.snake:
            pygame.draw.rect(self.display, GREEN1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, GREEN2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))

        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)

    def _get_observation(self):
        pygame.display.flip()  # Update the display
        observation = pygame.surfarray.array3d(pygame.display.get_surface())
        return observation


class PyGame2D:
    def __init__(self):
        ...

    def action(self, action):
        ...

    def evaluate(self):
        ...

    def is_done(self):
        ...

    def observe(self):
        ...

    def view(self):
        ...


if __name__ == '__main__':
    game = SnakeGame()

    # game loop
    while True:
        #return self._get_observation(), reward, game_over, {}
        # observation, reward, game_over, score = game.play_step(0)
        observation, reward, game_over, _ = game.play_step(0)

        if game_over == True:
            break

    # print('Final Score', score)

    pygame.quit()
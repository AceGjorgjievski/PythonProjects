import pygame
import random

WIDTH, HEIGHT = 630, 480
ROW, COLUMN = 30, 40
FPS = 10
GRID_SIZE = 15

# snake and apple variables
snake_dir = ''
snake_list = []
apple_pos = []
snake_eat = False
snake_dead = False
score = 0

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

pygame.init()
pygame.display.set_caption('Snake Game')
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial_bold', 30)
running = True

while running:

    snake_list, snake_dir = snake_generating(snake_list, snake_dir)
    snake_list, snake_eat = updating_snake(snake_dir, snake_list, snake_eat, snake_dead)
    snake_eat, snake_dead, score, apple_pos = collision(snake_list, apple_pos, snake_dir, snake_eat, snake_dead, score)
    apple_pos = apple_generating(snake_list, apple_pos)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break
            if event.key == pygame.K_RIGHT and not snake_list[0][0] < snake_list[1][0]:
                snake_dir = 'right'
            if event.key == pygame.K_LEFT and not snake_list[0][0] > snake_list[1][0]:
                snake_dir = 'left'
            if event.key == pygame.K_DOWN and not snake_list[0][1] < snake_list[1][1]:
                snake_dir = 'down'
            if event.key == pygame.K_UP and not snake_list[0][1] > snake_list[1][1]:
                snake_dir = 'up'

    # draw
    display.fill((0, 0, 0))

    # borders
    pygame.draw.rect(display, 'WHITE', (15, 15, 40 * 15, 1))
    pygame.draw.rect(display, 'WHITE', (15, 31 * 15, 40 * 15, 1))
    pygame.draw.rect(display, 'WHITE', (41 * 15, 15, 1, 30 * 15))
    pygame.draw.rect(display, 'WHITE', (15, 15, 1, 30 * 15))

    # score
    # if snake_dead:
    #     img = font.render(str(score), True, (125, 85, 85))
    # else:
    #     img = font.render(str(score), True, (57, 60, 65))
    # display.blit(img, img.get_rect(center=(20 * 15 + 15, 15 * 15 + 15)).topleft)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    display.blit(score_text, (WIDTH - score_text.get_width() - 20, 20))

    # apple
    if len(apple_pos) > 0:
        pygame.draw.rect(display, 'RED', (apple_pos[0] * 15 + 1, apple_pos[1] * 15 + 1, 13, 13))

    # snake body
    # for part in snake_list[1:]:
    #     pygame.draw.rect(display, (0, 255, 127), (part[0] * 15 + 1, part[1] * 15 + 1, 13, 13))
    for part in snake_list[1:]:
        pygame.draw.rect(display, (0, 255, 127),
                         (part[0] * GRID_SIZE + 1, part[1] * GRID_SIZE + 1, GRID_SIZE - 3, GRID_SIZE - 3))

    # snake head
    # pygame.draw.rect(display, (0, 255, 127), (snake_list[0][0] * 15 + 1, snake_list[0][1] * 15 + 1, 13, 13))
    pygame.draw.rect(display, (0, 255, 127),
                     (snake_list[0][0] * GRID_SIZE + 1, snake_list[0][1] * GRID_SIZE + 1, GRID_SIZE - 2, GRID_SIZE - 2))

    pygame.display.update()
    clock.tick(FPS)

    if snake_dead:
        running = False

pygame.quit()
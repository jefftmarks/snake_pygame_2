import pygame
from snake import *
from food import Food

pygame.init()

bounds = (600, 600)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Snake")


block_size = 20
snake = Snake(block_size, bounds)
food = Food(block_size, bounds)

font = pygame.font.SysFont('comicsans', 60, True)

running = True
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.steer(Direction.LEFT)
    elif keys[pygame.K_RIGHT]:
        snake.steer(Direction.RIGHT)
    elif keys[pygame.K_UP]:
        snake.steer(Direction.UP)
    elif keys[pygame.K_DOWN]:
        snake.steer(Direction.DOWN)

    snake.move()
    snake.check_for_food(food)

    if snake.check_bounds() or snake.check_tail_collision():
        text = font.render('Game Over', True, (255, 255, 255))
        window.blit(text, (20, 120))
        pygame.display.update()
        pygame.time.delay(1000)
        snake.respawn()
        food.respawn(snake)

    window.fill((0, 0, 0))

    snake.draw(pygame, window)
    food.draw(pygame, window)

    pygame.display.update()
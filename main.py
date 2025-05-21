import pygame
import time
from settings import *
from snake import Snake
from enemy import Enemy
from fruit import Fruit
from invincible import Invincible
from utils import show_score, game_over

pygame.init()
pygame.display.set_caption('PacSnake')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()
space_pressed = False
snake = Snake()

enemy_red = Enemy([400, 400], red, 3, window_x//2, window_x-20, window_y//2, window_y-20)           # Q4
enemy_blue = Enemy([100, 400], (0, 255, 255), 2, 10, window_x//2-10, window_y//2, window_y-20)     # Q3
enemy_orange = Enemy([100, 100], (255, 184, 82), 4, 10, window_x//2-10, 10, window_y//2-10)        # Q1
enemy_pink = Enemy([400, 100], (255, 184, 255), 3, window_x//2, window_x-20, 10, window_y//2-10)   # Q2

fruit = Fruit()
invincible = Invincible()

score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_to = 'UP'
            if event.key == pygame.K_DOWN:
                snake.change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                snake.change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                snake.change_to = 'RIGHT'
            if event.key == pygame.K_SPACE and snake.energy > 0:
                space_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space_pressed = False                
    snake.change_direction(snake.change_to)
    snake.move()

    # Snake eats fruit
    snake.grow()
    if snake.position[0] == fruit.position[0] and snake.position[1] == fruit.position[1] and not snake.color == orange:
        score += 10
        fruit.spawn = False
    else:
        snake.shrink()

    if not fruit.spawn:
        fruit.respawn()

    # Invincible spawn logic
    current_time = time.time()
    if not invincible.visible and current_time - invincible.start_time >= 15:
        invincible.spawn()
    if invincible.visible and current_time - invincible.start_time >= 5:
        invincible.visible = False

    current_time = time.time()
    snake.update_energy(space_pressed, current_time)
    snake.color = orange if space_pressed and snake.energy > 0 else yellow

    # Snake eats invincible
    if (snake.position[0] == invincible.position[0] and 
        snake.position[1] == invincible.position[1] and invincible.visible and not snake.color == orange):
        score += 30
        snake.set_invincible(blue, current_time)
        invincible.visible = False

    # Snake invincible color logic
    if snake.color_visible:
        if current_time - snake.color_start_time >= 4 and current_time - snake.color_start_time < 5:
            snake.color = white if snake.color == blue else blue
        elif current_time - snake.color_start_time >= 5:
            snake.reset_color(yellow)

    # Enemy respawn logic
    for enemy in [enemy_red, enemy_pink, enemy_blue, enemy_orange]:
        enemy.try_respawn()

    # Enemy movement (only if alive)
    if snake.color == blue:
        if enemy_red.alive: enemy_red.move_away(snake.position)
        if enemy_pink.alive: enemy_pink.move_away(snake.position)
        if enemy_blue.alive: enemy_blue.move_away(snake.position)
        if enemy_orange.alive: enemy_orange.move_away(snake.position)
    else:
        if enemy_red.alive: enemy_red.move_towards(snake.position)
        if enemy_pink.alive: enemy_pink.move_towards(snake.position)
        if enemy_blue.alive: enemy_blue.move_towards(snake.position)
        if enemy_orange.alive: enemy_orange.move_towards(snake.position)

    # Draw everything
    game_window.fill(black)
    pygame.draw.rect(game_window, blue, pygame.Rect(0, 0, window_x, window_y), 10)

    for pos in snake.body:
        pygame.draw.rect(game_window, snake.color, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit.position[0], fruit.position[1], 10, 10))
    if enemy_red.alive:
        pygame.draw.rect(game_window, enemy_red.color, pygame.Rect(enemy_red.position[0], enemy_red.position[1], 10, 10))
    if enemy_pink.alive:
        pygame.draw.rect(game_window, enemy_pink.color, pygame.Rect(enemy_pink.position[0], enemy_pink.position[1], 10, 10))
    if enemy_blue.alive:
        pygame.draw.rect(game_window, enemy_blue.color, pygame.Rect(enemy_blue.position[0], enemy_blue.position[1], 10, 10))
    if enemy_orange.alive:
        pygame.draw.rect(game_window, enemy_orange.color, pygame.Rect(enemy_orange.position[0], enemy_orange.position[1], 10, 10))

    # Barra de energia do poder laranja (coloque ANTES do pygame.display.update())
    bar_width = 100
    bar_height = 10
    bar_x = 10
    bar_y = window_y - 25

    # Fundo da barra
    pygame.draw.rect(game_window, (100, 100, 100), (bar_x, bar_y, bar_width, bar_height))
    # Parte laranja proporcional à energia
    if snake.energy > 0:
        pygame.draw.rect(
            game_window,
            orange,
            (bar_x, bar_y, int(bar_width * (snake.energy / snake.energy_max)), bar_height)
        )
    # Contorno branco
    pygame.draw.rect(game_window, white, (bar_x, bar_y, bar_width, bar_height), 2)

    # Atualize a tela depois de desenhar a barra!
    pygame.display.update()    

    # Invincible color logic
    if invincible.visible:
        invincible.update_color()
        pygame.draw.rect(game_window, invincible.color, pygame.Rect(invincible.position[0], invincible.position[1], 10, 10))
    
    # Enemy collision logic
    for enemy in [enemy_red, enemy_pink, enemy_blue, enemy_orange]:
        if enemy.alive and snake.position[0] == enemy.position[0] and snake.position[1] == enemy.position[1] and not snake.color == orange:
            if snake.color == blue:  # só azul pode matar
                enemy.kill()
            else:
                game_over(game_window, score, window_x, window_y)
                
    # Game Over conditions
    if snake.position[0] < 10 or snake.position[0] > window_x - 20:
        game_over(game_window, score, window_x, window_y)
    if snake.position[1] < 10 or snake.position[1] > window_y - 20:
        game_over(game_window, score, window_x, window_y)
    for block in snake.body[1:]:
        if (
            snake.position[0] == block[0]
            and snake.position[1] == block[1]
            and not snake.color_visible
            and not snake.color == orange  
        ):
            game_over(game_window, score, window_x, window_y)            
    show_score(game_window, score, white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(snake_speed)

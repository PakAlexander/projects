import random
import sys

import pygame
import pygame_menu

pygame.init()
timer = pygame.time.Clock()
bg_image = pygame.image.load("Snake.jpg")
HEADER_MARGIN = 100
MARGIN = 1
COUNT_BLOCK = 20
SIZE_BLOCK = 20
WHITE = (255, 255, 255)
FRAME_COLOR = (0, 155, 125)
BLUE = (200, 255, 255)
HEADER_COLOR = (0, 130, 125)
SNAKE_COLOR = (100, 100, 50)
RED = (255, 0, 0)
size = [(COUNT_BLOCK + MARGIN) * (COUNT_BLOCK + 2), HEADER_MARGIN + (COUNT_BLOCK + MARGIN) * (COUNT_BLOCK + 2)]
print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Змейка")


class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and isinstance(other, SnakeBlock)

    def is_inside(self):
        return 0 <= self.x <= COUNT_BLOCK and 0 <= self.y <= COUNT_BLOCK


def draw_block(color, row, colum):
    pygame.draw.rect(screen, color, (SIZE_BLOCK + colum * SIZE_BLOCK + MARGIN * colum,
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * row, SIZE_BLOCK,
                                     SIZE_BLOCK))


def start_the_game():
    def get_empty_block():
        x = random.randint(0, COUNT_BLOCK - 1)
        y = random.randint(0, COUNT_BLOCK - 1)
        empty_block = SnakeBlock(x, y)
        while empty_block in snake:
            empty_block.x = random.randint(0, COUNT_BLOCK - 1)
            empty_block.y = random.randint(0, COUNT_BLOCK - 1)
        return empty_block

    snake = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
    apple = get_empty_block()
    d_row = buf_row = 0
    d_column = buf_col = 1
    total = 0
    speed = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and d_row != 0:
                    buf_row = 0
                    buf_col = -1
                elif event.key == pygame.K_RIGHT and d_row != 0:
                    buf_row = 0
                    buf_col = 1
                elif event.key == pygame.K_UP and d_column != 0:
                    buf_row = -1
                    buf_col = 0
                elif event.key == pygame.K_DOWN and d_column != 0:
                    buf_row = 1
                    buf_col = 0

        d_row = buf_row
        d_column = buf_col
        pygame.draw.rect(screen, HEADER_COLOR, (0, 0, size[0], HEADER_MARGIN))
        screen.fill(FRAME_COLOR)
        font = pygame.font.SysFont("courier", 36)
        text_total = font.render(f"Total: {total}", 0, WHITE)
        text_speed = font.render(f"Speed: {speed}", 0, WHITE)
        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK + 20))
        screen.blit(text_speed, (SIZE_BLOCK + 230, SIZE_BLOCK + 20))

        for row in range(COUNT_BLOCK):
            for column in range(COUNT_BLOCK):
                if (row + column) % 2 == 0:
                    color = WHITE
                else:
                    color = BLUE
                draw_block(color, row, column)
        head = snake[-1]
        if not head.is_inside():
            break
        draw_block(RED, apple.x, apple.y)
        for i in snake:
            draw_block(SNAKE_COLOR, i.x, i.y)
        pygame.display.update()
        if apple == head:
            total += 1
            speed = total // 5 + 1
            snake.append(apple)
            apple = get_empty_block()
        new_head = SnakeBlock(head.x + d_row, head.y + d_column)
        if new_head in snake:
            break
        snake.append(new_head)
        snake.pop(0)
        timer.tick(3 + speed)

main_theme = pygame_menu.themes.THEME_GREEN.copy()
main_theme.set_background_color_opacity(0.8)
menu = pygame_menu.Menu('', 300, 300, theme = main_theme)
menu.add.text_input('Name: ', default = 'Пупкин')
menu.add.button('Играть', start_the_game)
menu.add.button('Выход', pygame_menu.events.EXIT)

while True:
    screen.blit(bg_image,(0,0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)

    pygame.display.update()

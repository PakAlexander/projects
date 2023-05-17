from logics import *
import pygame
import sys
from database import get_best, cur, insert_result
import json
import os

GAMERS_DB = get_best()

def draw_top_gamers():
    font_top = pygame.font.SysFont("Comic Sans MS", 25, bold=True)
    font_gamer = pygame.font.SysFont("Comic Sans MS", 16, bold = True)
    font_head = font_top.render("Лучшие: ", True, COLOR_TEXT)
    screen.blit(font_head, (300, 5))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        informer = f"{index+1}. {name} - {score}"
        text_gamer = font_gamer.render(informer, True, COLOR_TEXT )
        screen.blit(text_gamer, (300, 35 + 20 * index))

def dratw_interface(score, delta=0):
    global USER_NAME
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont("stxingkai", 70)
    font_score = pygame.font.SysFont("Comic Sans MS", 48, bold=True)
    font_delta = pygame.font.SysFont("Comic Sans MS", 30, bold = True)
    font_user_name = pygame.font.SysFont("Comic Sans MS", 16, bold = True)
    font_text_delta = font_delta.render(f"+{delta}", True, COLOR_TEXT)
    font_user_name = font_user_name.render(f"Ваше имя: {USER_NAME}", True, COLOR_TEXT)
    font_text = font_score.render("Счёт: ", True, COLOR_TEXT )
    font_text_value = font_score.render(f"{score}", True, COLOR_TEXT)
    screen.blit(font_user_name, (20, 0))
    screen.blit(font_text, (20, 15))
    screen.blit(font_text_value, (180, 15))
    if delta > 0:
        screen.blit(font_text_delta, (180, 65))
    pretty_print(mas)
    draw_top_gamers()

    for row in range(BLOCKS):
        for col in range(BLOCKS):
            value = mas[row][col]
            text = font.render(f"{value}", True, BLACK)
            w = col * SIZE_BLOCKS + (col + 1) * MARGIN
            h = row * SIZE_BLOCKS + (row + 1) * MARGIN + SIZE_BLOCKS
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCKS, SIZE_BLOCKS))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCKS - font_w) / 2
                text_y = h + (SIZE_BLOCKS - font_h) / 2
                screen.blit(text, (text_x, text_y))

mas = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       ]
COLORS = {
    0: (130,130,130),
    2: (255,255,255),
    4: (255,255,128),
    8: (255,255,0),
    16: (255,235,255),
    32: (255,235,128),
    64: (255, 235, 0),
   128: (255, 210, 255),
   256: (255, 210, 128),
   512: (255, 210, 0),
  1024: (255, 185, 255),
  2048: (255, 185, 128),

}

def _init():
    global mas, score
    mas = [ [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
    ]
    empty = get_empty_list(mas)
    random.shuffle(empty)
    random_num1 = empty.pop()
    random_num2 = empty.pop()
    x1, y1 = get_index_from_number(random_num1)
    x2, y2 = get_index_from_number(random_num2)
    mas = insert_2_or_4(mas, x1, y1)
    mas = insert_2_or_4(mas, x2, y2)
    score = 0

COLOR_TEXT = (255, 125, 10)
WHITE = (255,255,255)
GREY = (130,130,130)
BLACK = (0,0,0)
BLOCKS = 4
SIZE_BLOCKS = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCKS + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + 110
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)

print(get_empty_list(mas))
pretty_print(mas)
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

score = None
mas = None
USER_NAME = None
path = os.getcwd()

if 'data.txt' in os.listdir(path):
    with open('data.txt') as file:
        data = json.load(file)
        USER_NAME = data['user']
        score = data['score']
        mas = data['mas']
    full_path = os.path.join(path, 'data.txt')
    os.remove(full_path)
else:
    _init()

def draw_intro():
    img2048 = pygame.image.load('2048.png')
    font = pygame.font.SysFont("stxingkai", 60)
    font_wellcome = font.render("Wellcome!", True, WHITE)
    screen.blit(font_wellcome, [240, 90])
    name = "Введите текст"
    is_find_name = False

    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                screen.fill(BLACK)
                if event.unicode.isalpha():
                    if name == "Введите текст":
                        name = event.unicode
                    else:
                        name += event.unicode

                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2:
                        global USER_NAME
                        USER_NAME = name
                        is_find_name = True
                        break

        screen.fill(BLACK)
        text_name = font.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(text_name, rect_name)
        screen.blit(pygame.transform.scale(img2048, [200,200]), (10, 10))
        pygame.display.update()
    screen.fill(BLACK)

def draw_game_over():
    global USER_NAME, score, mass, GAMERS_DB
    img2048 = pygame.image.load('2048.png')
    font = pygame.font.SysFont("stxingkai", 60)
    font_game_over = font.render("Game over!", True, WHITE)
    text_scort = font.render(f"Вы набрали: {score} ", True, WHITE)
    best_score = GAMERS_DB[0][1]
    if score > best_score:
        _text = "Рекорд побит!"
    else:
        _text = f"Рекорд: {best_score}"
    text_record = font.render(_text, True, WHITE)
    insert_result(USER_NAME, score)
    GAMERS_DB = get_best()

    make_des = False
    while not make_des:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    USER_NAME = None
                    make_des = True
                    _init()
                elif event.key == pygame.K_RETURN:
                    make_des = True
                    _init()
        screen.fill(BLACK)
        screen.blit(font_game_over, (230, 80))
        screen.blit(text_scort, (30, 250))
        screen.blit(text_record, (30, 300))
        screen.blit(pygame.transform.scale(img2048, [200,200]), (10, 10))
        pygame.display.update()
    screen.fill(BLACK)

def save_game():
    data = {
        'user':USER_NAME,
        'score': score,
        'mas': mas
    }
    with open ('data.txt', 'w') as file:
        json.dump(data, file)

def game_loop():
    global score, mas
    dratw_interface(score)
    pygame.display.update()
    is_mas_move = False
    while is_zero_is_mas(mas) or can_move(mas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game()
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta = 0
                if event.key == pygame.K_LEFT:
                    mas, delta, is_mas_move = move_left(mas)
                elif event.key == pygame.K_RIGHT:
                    mas, delta, is_mas_move = move_right(mas)
                elif event.key == pygame.K_UP:
                    mas, delta, is_mas_move = move_up(mas)
                elif event.key == pygame.K_DOWN:
                    mas, delta, is_mas_move = move_down(mas)
                score += delta
                if is_zero_is_mas(mas) and is_mas_move:
                    empty = get_empty_list(mas)
                    random.shuffle(empty)
                    random_num = empty.pop()
                    x, y = get_index_from_number(random_num)
                    mas = insert_2_or_4(mas, x, y)
                    print(f"Cell:  {random_num}")
                    is_mas_move = False
                dratw_interface(score, delta)
                pygame.display.update()
        # print(USER_NAME)

while True:
    if USER_NAME is None:
        draw_intro()
    game_loop()
    draw_game_over()
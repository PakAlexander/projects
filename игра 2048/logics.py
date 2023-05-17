import copy
import random

def pretty_print(mas):
    print("-" * 10)
    for i in mas:
        print(*i)
    print("-" * 10)

def get_number_index(i, j):
    return i * 4 + j + 1

def get_empty_list(mas):
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_index(i, j)
                empty.append(num)
    return empty

def get_index_from_number(num):
    num -=1
    x, y = num // 4, num % 4
    return x, y

def insert_2_or_4(mas, x, y):
    if random.random() < 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas

def is_zero_is_mas(mas):
    for row in mas:
        if 0 in row:
            return True
    return False

def move_left(mas):
    original = copy.deepcopy(mas)
    delta = 0
    for row in mas:
        while 0  in row:
            row.remove(0)
        while len(row) !=4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if mas[i][j] == mas[i][j + 1] and mas[i][j] != 0:
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j+1)
                mas[i].append(0)
    return mas, delta, not original == mas

def move_right(mas):
    original = copy.deepcopy(mas)
    delta = 0
    for row in mas:
        while 0  in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for i in range(4):
        for j in range(3, 0, -1):
            if mas[i][j] == mas[i][j - 1] and mas[i][j] != 0:
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j-1)
                mas[i].insert(0, 0)
    return mas, delta, not original == mas

def move_up(mas):
    orig = copy.deepcopy(mas)
    mas, delta, _ = move_left(list(map(list, (zip(*mas)))))
    mas = list(map(list, (zip(*mas))))
    return mas, delta, not orig == mas

def move_down(mas):
    orig = copy.deepcopy(mas)
    mas, delta, _ = move_right(list(map(list, (zip(*mas)))))
    mas = list(map(list, (zip(*mas))))
    return mas, delta, not orig == mas

def can_move(mas):
    for i in range(4):
        for j in range(4):
            if (j + 1 != 4 and mas[i][j] == mas[i][j + 1]) or (i + 1 != 4 and mas[i][j] == mas[i + 1][j]):
                return True
    return False

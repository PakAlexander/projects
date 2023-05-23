from random import randint
import re

class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        if self.value == 0:
            return True
        return False

class TicTacToe:

    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False
        self.pole = tuple(tuple(Cell() for _ in range(3))for _ in range(3))

    def __bool__(self):
        if self.is_computer_win or self.is_human_win or self.is_draw:
            return False
        return True

    def __getitem__(self, item):
        self.check_index(item)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, item, value):
        self.check_index(item)
        self.pole[item[0]][item[1]].value = value
        self.check_game()

    def init(self):
        for i in range(3):
            for j in range(3):
                self.pole[i][j].value = 0
        self.is_draw = self.is_human_win = self.is_computer_win = False

    def check_game(self):
        trans = list(zip(*self.pole))
        for i in self.pole:
            if all([j.value == self.COMPUTER_O for j in i]):
                self.is_computer_win = True
                return
            if all([j.value == self.HUMAN_X for j in i]):
                self.is_human_win = True
                return
        for i in trans:
            if all([j.value == self.COMPUTER_O for j in i]):
                self.is_computer_win = True
                return
            if all([j.value == self.HUMAN_X for j in i]):
                self.is_human_win = True
                return

        if self.pole[0][0].value == self.pole[1][1].value == self.pole[2][2].value == self.COMPUTER_O:
            self.is_computer_win = True
        if self.pole[0][2].value == self.pole[1][1].value == self.pole[2][0].value == self.COMPUTER_O:
            self.is_computer_win = True

        if self.pole[0][0].value == self.pole[1][1].value == self.pole[2][2].value == self.HUMAN_X:
            self.is_human_win = True
        if self.pole[0][2].value == self.pole[1][1].value == self.pole[2][0].value == self.HUMAN_X:
            self.is_human_win = True

        if all([j.value != self.FREE_CELL for i in self.pole for j in i ]):
            self.is_draw = True

    def show(self):
        for i in range(3):
            for j in range(3):
                if self.pole[i][j].value == self.FREE_CELL:
                    print(u'\u2b1c', end = ' ')
                elif self.pole[i][j].value == self.HUMAN_X:
                    print(u'\u274c', end = ' ')
                elif self.pole[i][j].value == self.COMPUTER_O:
                    print(u'\u2b55', end = ' ')
            print()

        print('-----------------------------------------------')

    def human_go(self):
        pattern = '[0-2] [0-2]'
        while True:
            st = input("Сделайте ход(индексы сбободной клетки x y через пробел): ")
            if not bool(re.fullmatch(pattern, st)):
                continue
            x, y = list(map(int, st.split()))
            if self.pole[x][y]:
                self.pole[x][y].value = self.HUMAN_X
                break
            # x, y = randint(0, 2), randint(0, 2)
            # if self.pole[x][y]:
            #     self[x, y] = self.HUMAN_X
            #     break

    def computer_go(self):
        while True:
            x, y = randint(0, 2), randint(0, 2)
            if self.pole[x][y]:
                self[x, y] = self.COMPUTER_O
                break

    @staticmethod
    def check_index(index):
        i, j = index
        if type(i) != int or type(j) != int or not(0 <= i < 3) or not(0 <= j < 3):
            raise IndexError('некорректно указанные индексы')




game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1

game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
# m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# # print([[0 for i in range(3)] for j in range(3)])
# print(TicTacToe().show(m))

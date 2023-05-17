from random import randint
import copy

class SetValue:
    # Дескриптор для Ship
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_value(value)
        setattr(instance, self.name, value)

    def check_value(self, value):
        if (self.name == "_x" or self.name == "_y") and value not in range(10) and value != None :
            raise ValueError("Недопустимые значения x, y")
        if self.name == "_length" and value not in (1, 2, 3, 4):
            raise ValueError("Недопустимые значение length - длины корабля")
        if self.name == "_tp" and value not in (1, 2):
            raise ValueError("Недопустимые значение tp - ориентация корабля (1 - горизонтальная; 2 - вертикальная)")
        if self.name == "_is_move" and value not in (True, False):
            raise ValueError("Недопустимые значение is_move -  возможно ли перемещение корабля")
        if self.name == "_cells" and type(value) != list:
            raise TypeError("Недопустимые тип данных _cells - длина корабля")
        if self.name == "_cells" and not (1 <= len(value) <= 4):
            raise ValueError("Недопустимая длина корабля _cells")

class Ship:
    """ Ship - класс кораблей"""
    # Дескрипторы:
    length = SetValue()
    tp = SetValue()
    x = SetValue()
    y = SetValue()
    is_move = SetValue()
    cells = SetValue()

    def __init__(self, length, tp=1, x=None, y=None):
        self.length = length   # length - длина корабля (число палуб: целое значение: 1, 2, 3 или 4)
        self.tp = tp    # tp - ориентация корабля (1 - горизонтальная; 2 - вертикальная).
        self.is_move = True     # возможно ли перемещение корабля
        self.cells = [1] * length   # длина корабля
        self.x = x     # x,  координаты начала расположения корабля (целые числа);
        self.y = y     # y - координаты начала расположения корабля (целые числа);
        self.init_x1_y1()

    def init_x1_y1(self):
        if self.x != None and self.y != None:
            if self.tp == 1:
                self._x1 = self.x + self.length
                self._y1 = self.y + 1
            elif self.tp == 2:
                self._x1 = self.x + 1
                self._y1 = self.y + self.length

    def set_start_coords(self, x, y):
        """ установка начальных координат (запись значений в локальные атрибуты _x, _y);"""
        self.x = x
        self.y = y

    def get_start_coords(self):
        """получение начальных координат корабля в виде кортежа x, y;"""
        return self.x, self.y

    def move(self, go):
        """ перемещение корабля в направлении его ориентации на go клеток (go = 1 - движение в одну сторону на клетку;
         go = -1 - движение в другую сторону на одну клетку); движение возможно только если флаг _is_move = True;"""
        if self.is_move:
            if self.tp == 1:
                self.x = self.x + go
            if self.tp == 2:
                self.y = self.y + go

    def is_collide(self, ship):
        """проверка на столкновение с другим кораблем ship (столкновением считается, если другой корабль или
         пересекается с текущим или просто соприкасается, в том числе и по диагонали); метод возвращает True,
          если столкновение есть и False - в противном случае;"""
        if not (self.y > ship._y1 or self._y1 < ship.y or self._x1 < ship.x or self.x > ship._x1):
              return True
        return False

    def is_out_pole(self, size):
        """проверка на выход корабля за пределы игрового поля (size - размер игрового поля, обычно, size = 10);
        возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае;"""
        if self.tp == 1 and self.x + self.length >= size:
            return True
        if self.tp == 2 and self.y + self.length >= size:
            return True
        return False

    def __getitem__(self, item):
        return self.cells[item]

    def __setitem__(self, item, value):
        self.cells[item] = value

class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []
        self._pole = []
        self._buffer = {}

    def init(self):
        self._pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        ships = []
        ships.append(Ship(4, randint(1, 2)))
        [ships.append(Ship(3, randint(1, 2))) for _ in range(2)]
        [ships.append(Ship(2, randint(1, 2))) for _ in range(3)]
        [ships.append(Ship(1, randint(1, 2))) for _ in range(4)]

        lst_ships = []
        for i in ships:
            while True:
                x, y = randint(0, 9), randint(0, 9)
                i.x, i.y = x, y
                i.init_x1_y1()
                if not i.is_out_pole(10):
                    if len(lst_ships) > 0:
                        if not any([i.is_collide(j) for j in lst_ships]):
                            lst_ships.append(i)
                            break
                    else:
                        lst_ships.append(i)
                        break
        self._ships = lst_ships

    def _get_cells_ships(self, i, j):
        for ship in self._ships:
            if ship.x == i and ship.y == j:
                self._buffer[(i, j)] = ship.cells[0]
                if ship.tp == 1:
                    for it in range(1, ship.length):
                        self._buffer[(i + it, j)] = ship.cells[it]
                elif ship.tp == 2:
                    for it in range(1, ship.length):
                        self._buffer[(i, j + it)] = ship.cells[it]

    def show(self):
        n = len(self._pole)
        for i in range(n):
            for j in range(n):
                self._get_cells_ships(i, j)
                if (i, j) in self._buffer:
                    print(self._buffer[(i, j)], end = "  ")
                else:
                    print(self._pole[i][j], end = "  ")

            print()

    def get_ships(self):
        return tuple(self._ships)

    def get_pole(self):
        return tuple(tuple(i) for i in self._pole)

    def move_ships(self):
        for key, obj in enumerate(self._ships):
            temp1 = copy.copy(obj)
            # print(hash(temp1), hash(obj))
            temp2 = copy.copy(obj)
            if obj.tp == 1:
                try:
                    temp1.x = obj.x + 1
                    temp1.init_x1_y1()
                    temp2.x = obj.x - 1
                    temp2.init_x1_y1()
                except ValueError:
                    continue
                if not temp1.is_out_pole(10) and not any([temp1.is_collide(j) for j in self._ships if self._ships[key] != j]):
                    self._ships[key] = temp1
                elif not temp2.is_out_pole(10) and not any([temp2.is_collide(j) for j in self._ships if self._ships[key] != j]):
                    self._ships[key] = temp2
            elif obj.tp == 2:
                try:
                    temp1.y = obj.y + 1
                    temp1.init_x1_y1()
                    temp2.y = obj.y - 1
                    temp2.init_x1_y1()
                except ValueError:
                    continue
                if not temp1.is_out_pole(10) and not any([temp1.is_collide(j) for j in self._ships if self._ships[key] != j]):
                    self._ships[key] = temp1
                elif not temp2.is_out_pole(10) and not any([temp2.is_collide(j) for j in self._ships if self._ships[key] != j]):
                    self._ships[key] = temp2
            self._buffer = {}
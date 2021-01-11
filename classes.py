import pygame
import random


class Board:
    def __init__(self, col, s):
        self.width = s[0]
        self.height = s[1]
        self.board = self.make_pole(col, s)
        self.random_board = self.random_color_mix(col)
        # for i in self.board:
        # print(i)
        self.top = 10
        self.cell_size = 30

    def set_view(self, top, cell_size):
        self.top = top
        self.cell_size = cell_size
        size = self.width * self.cell_size, self.top * 2 + self.height * self.cell_size
        return pygame.display.set_mode(size)

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, self.board[i][j], ((i * self.cell_size, self.top + j * self.cell_size),
                                                            (self.cell_size, self.cell_size)))
        pygame.draw.circle(screen, (0, 0, 0), (self.cell_size // 2, self.top + self.cell_size // 2), 3)
        pygame.draw.circle(screen, (0, 0, 0),
                           (self.cell_size // 2 + self.cell_size * (self.width - 1), self.top + self.cell_size // 2), 3)
        pygame.draw.circle(screen, (0, 0, 0), (self.cell_size // 2,
                                               self.top + self.cell_size * (self.height - 1) + self.cell_size // 2), 3)
        pygame.draw.circle(screen, (0, 0, 0),
                           (self.cell_size // 2 + self.cell_size * (self.width - 1),
                            self.top + self.cell_size * (self.height - 1) + self.cell_size // 2), 3)

    # создание поля
    def make_pole(self, colors, size):
        sp1 = self.make_sp(colors[0], colors[1], size[0])
        sp2 = self.make_sp(colors[2], colors[3], size[0])
        sp0 = []
        # print(sp1, sp2)
        for i in range(size[0]):
            sp0.append(self.make_sp(sp1[i], sp2[i], size[1]))
        return sp0

    # генерация цветового поля
    def make_sp(self, col1, col2, a1):
        sp = [[0, 0, 0] for i in range(a1)]
        for i in range(3):
            s0 = col1[i]
            s1, s2 = col1[i], col2[i]
            k = (s2 - s1) / (a1 - 1)
            for j in range(1, a1):
                s1 += k
                sp[j][i] = int(s1)
            sp[0][i] = s0
            sp[a1 - 1][i] = s2
        return sp

    def random_color_mix(self, corner_colors):
        random_mix = self.board.copy()
        cells = list()
        for column in self.board:
            for cell in column:
                if tuple(cell) not in corner_colors:
                    cells.append(cell)
        # print(cells)
        for i in range(self.width):
            for j in range(self.height):
                if tuple(random_mix[i][j]) not in corner_colors:
                    random_mix[i][j] = cells.pop(random.randrange(0, len(cells)))
        return random_mix


a = [(255, 165, 0), (50, 205, 50), (255, 248, 220), (128, 0, 0)]  # цвета клеток
b = [10, 15]  # рамеры поля

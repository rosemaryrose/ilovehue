import pygame
import random


class ILoveHueGame:
    def __init__(self, corner_colors, numbers_of_cells):
        self.width = numbers_of_cells[0]
        self.height = numbers_of_cells[1]
        self.board = self.make_board(corner_colors, numbers_of_cells)
        self.random_board = self.random_color_mix(corner_colors)

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
    def make_board(self, corner_colors, numbers_of_cells):
        line1 = self.make_line(corner_colors[0], corner_colors[1], numbers_of_cells[0])
        line2 = self.make_line(corner_colors[2], corner_colors[3], numbers_of_cells[0])
        board = []

        for i in range(self.width):
            board.append(self.make_line(line1[i], line2[i], numbers_of_cells[1]))
        return board

    # генерация цветового поля
    def make_line(self, start_color, end_color, cells_width):
        line = [[0, 0, 0] for _ in range(cells_width)]
        for i in range(3):
            color0 = start_color[i]
            color1, color2 = start_color[i], end_color[i]
            k = (color2 - color1) / (cells_width - 1)
            for j in range(1, cells_width):
                color1 += k
                line[j][i] = int(color1)
            line[0][i] = color0
            line[cells_width - 1][i] = color2
        return line

    def random_color_mix(self, corner_colors):
        random_mix = self.board.copy()
        cells = list()
        for column in self.board:
            for cell in column:
                if tuple(cell) not in corner_colors:
                    cells.append(cell)

        for i in range(self.width):
            for j in range(self.height):
                if tuple(random_mix[i][j]) not in corner_colors:
                    random_mix[i][j] = cells.pop(random.randrange(0, len(cells)))
        return random_mix


class ILoveHueMenu:
    pass

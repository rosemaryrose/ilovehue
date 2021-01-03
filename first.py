import pygame

class Board:
    def __init__(self, col, s):
        self.width = s[0]
        self.height = s[1]
        self.board = self.make_pole(col, s)
        self.top = 10
        self.cs = 30

    def set_view(self, top, cell_size):
        self.top = top
        self.cs = cell_size
        size = self.width * self.cs, self.top * 2 + self.height * self.cs
        return pygame.display.set_mode(size)

    def render(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, tuple(self.board[i][j]), ((i * self.cs, self.top + j * self.cs), (self.cs, self.cs)))

    def make_pole(self, colors, size):
        sp1 = self.make_sp(colors[0], colors[1], size[0])
        sp2 = self.make_sp(colors[2], colors[3], size[0])
        sp0 = []
        print(sp1, sp2)
        for i in range(size[0]):
            sp0.append(self.make_sp(sp1[i], sp2[i], size[1]))
        return sp0

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

a = [(255, 165, 0), (50, 205, 50), (255, 248, 220), (128, 0, 0)]
b = [10, 15]

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Поле')

    board = Board(a, b)
    screen = board.set_view(30, 40)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


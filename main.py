from classes import *

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('ILoveHue')

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

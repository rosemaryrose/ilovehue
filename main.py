from classes import *

corner_colors = [(255, 165, 0), (50, 205, 50), (255, 248, 220), (128, 0, 0)]  # цвета клеток
size = [10, 15]  # размеры поля

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('ILoveHue')

    board = ILoveHueGame(corner_colors, size)
    screen = board.set_view(30, 40)
    running = True
    board.render_start(screen)
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # отрисовка следующего кадра
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()

from classes import *

corner_colors = [(255, 165, 0), (50, 205, 50), (255, 248, 220), (128, 0, 0)]  # цвета клеток
size = [7, 11]  # размеры поля

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('ILoveHue')

    # настройка
    board = ILoveHueGame(corner_colors, size)
    size2 = 315, 545
    screen = pygame.display.set_mode(size2)
    # отрисовка начала игры (это надо будет потом перенести, ибо у нас изначально будет меню)
    board.render_start(screen)
    pygame.display.flip()

    running = True

    now_cell = (None, None)
    cell_color = (None, None, None)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                # начало перетаскивания клетки
                now_cell = board.get_cell(event.pos)
                if now_cell is not None and now_cell not in board.static_cells:
                    cell_color = board.random_board[now_cell[0]][now_cell[1]]

                    click_width = event.pos[0] - board.cell_sizex * (now_cell[0])
                    click_height = event.pos[1] - board.cell_sizey * (now_cell[1]) - board.top

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                # конец перетаскивания клетки
                new_cell = board.get_cell(event.pos)
                if now_cell != (None, None) and cell_color != (None, None, None) and new_cell not in board.static_cells:

                    if new_cell is not None:
                        board.random_board[now_cell[0]][now_cell[1]], board.random_board[new_cell[0]][new_cell[1]] = \
                            board.random_board[new_cell[0]][new_cell[1]], board.random_board[now_cell[0]][now_cell[1]]

                now_cell = (None, None)
                cell_color = (None, None, None)

            if event.type == pygame.QUIT:
                running = False

        # конец игры
        if board.board == board.random_board:
            print('Поздравляем, вы собрали ilovehue!')
            screen.fill((0, 0, 0))
            board.render_start(screen)
            board.render(screen)
            pygame.draw.circle(screen, (255, 245, 250), (100, 220), 52)
            pygame.draw.circle(screen, (255, 245, 250), (200, 220), 52)
            pygame.draw.polygon(screen, (255, 245, 250), [(150, 220), (57, 248), (150, 334), (243, 248)])
            pygame.display.flip()
            pygame.time.delay(3000)
            running = False

        # отрисовка следующего кадра
        screen.fill((0, 0, 0))
        board.render(screen)

        # отрисовка движущейся клетки
        if now_cell != (None, None) and cell_color != (None, None, None):
            pygame.draw.rect(screen, (0, 0, 0), (
                (now_cell[0] * board.cell_sizex, now_cell[1] * board.cell_sizey + board.top),
                (board.cell_sizex, board.cell_sizey)))
            pygame.draw.rect(screen, cell_color, (
                (mouse_pos[0] - click_width, mouse_pos[1] - click_height), (board.cell_sizex, board.cell_sizey)))

        pygame.display.flip()
    pygame.quit()

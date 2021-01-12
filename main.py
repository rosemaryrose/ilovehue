from classes import *

corner_colors = [(255, 165, 0), (50, 205, 50), (255, 248, 220), (128, 0, 0)]  # цвета клеток
size = [10, 15]  # размеры поля

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('ILoveHue')

    # настройка
    board = ILoveHueGame(corner_colors, size)
    screen = board.set_view(30, 40)

    # отрисовка начала игры (это надо будет потом перенести, ибо у нас изначально будет меню)
    board.render_start(screen)
    pygame.display.flip()

    running = True

    dragging_cell = (None, None)
    cell_color = (None, None, None)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                # начало перетаскивания клетки
                if board.get_cell(event.pos) is not None and board.get_cell(event.pos) not in board.static_cells and \
                        board.board[board.get_cell(event.pos)[0]][board.get_cell(event.pos)[1]] != \
                        board.random_board[board.get_cell(event.pos)[0]][board.get_cell(event.pos)[1]]:
                    dragging_cell = board.get_cell(event.pos)
                    cell_color = board.random_board[dragging_cell[0]][dragging_cell[1]]

                    click_width = event.pos[0] - board.cell_size * (dragging_cell[0])
                    click_height = event.pos[1] - board.cell_size * (dragging_cell[1]) - board.top

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:

                # конец перетаскивания клетки
                if dragging_cell is not (None, None) and cell_color is not (None, None, None) and board.get_cell(
                        event.pos) not in board.static_cells and board.board[board.get_cell(event.pos)[0]][
                        board.get_cell(event.pos)[1]] != board.random_board[board.get_cell(event.pos)[0]][
                        board.get_cell(event.pos)[1]]:
                    cell = board.get_cell(event.pos)
                    if cell is not None:
                        board.random_board[dragging_cell[0]][dragging_cell[1]], board.random_board[cell[0]][cell[1]] = \
                            board.random_board[cell[0]][cell[1]], board.random_board[dragging_cell[0]][dragging_cell[1]]

                dragging_cell = (None, None)
                cell_color = (None, None, None)

            if event.type == pygame.QUIT:
                running = False

        # отрисовка следующего кадра
        screen.fill((0, 0, 0))
        board.render(screen)

        # отрисовка движущейся клетки
        if dragging_cell is not (None, None) and cell_color is not (None, None, None):
            pygame.draw.rect(screen, (0, 0, 0), (
                (dragging_cell[0] * board.cell_size, dragging_cell[1] * board.cell_size + board.top),
                (board.cell_size, board.cell_size)))
            pygame.draw.rect(screen, cell_color, (
                (mouse_pos[0] - click_width, mouse_pos[1] - click_height), (board.cell_size, board.cell_size)))

        pygame.display.flip()
    pygame.quit()

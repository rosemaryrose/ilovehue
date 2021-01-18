from classes import *
import sqlite3
import pygame

con = sqlite3.connect("levels_db.db")
cur = con.cursor()
result = list(cur.execute("""SELECT * FROM levels
            WHERE id = """ + input()).fetchone())
con.close()

corner_colors = [tuple([int(k) for k in i.split(', ')]) for i in result[3:7]]  # цвета клеток
size = [result[1], result[2]]  # размеры поля
black_p = result[8]
display_size = 315, 545

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Gradient Puzzle')

    screen = pygame.display.set_mode(display_size)

    running = True
    now_cell = (None, None)
    cell_color = (None, None, None)
    mouse_pos = None
    click_width = None
    click_height = None

    state = 'menu'

    while running:
        if state == 'menu':
            # заготовка под отрисовку меню
            '''
            # настройка
            menu = ILoveHueMenu()
            # отрисовка заставки
            menu.render_start(screen)
            pygame.display.flip()
            '''

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:  # типа начало игры(позже сделаю по кнопке)
                    state = 'game'
                if event.type == pygame.QUIT:
                    running = False

                # отрисовка следующего кадра
                screen.fill((0, 0, 0))
                # menu.render(screen)

                pygame.display.flip()
        elif state == 'game':
            # настройка
            board = ILoveHueGame(corner_colors, size, black_p)

            # отрисовка начала игры (это надо будет потом перенести, ибо у нас изначально будет меню)
            board.render_start(screen)
            pygame.display.flip()

            gaming = True

            while gaming:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:

                        # начало перетаскивания клетки
                        now_cell = board.get_cell(event.pos)
                        if now_cell is not None and now_cell not in board.static_cells:
                            cell_color = board.random_board[now_cell[0]][now_cell[1]]

                            click_width = event.pos[0] - board.cell_size_x * (now_cell[0])
                            click_height = event.pos[1] - board.cell_size_y * (now_cell[1]) - board.top

                    if event.type == pygame.MOUSEMOTION:
                        mouse_pos = event.pos

                    if event.type == pygame.MOUSEBUTTONUP:
                        # конец перетаскивания клетки
                        new_cell = board.get_cell(event.pos)
                        if now_cell != (None, None) and cell_color != (
                                None, None, None) and new_cell not in board.static_cells:

                            if new_cell is not None:
                                board.random_board[now_cell[0]][now_cell[1]], board.random_board[new_cell[0]][
                                    new_cell[1]] = \
                                    board.random_board[new_cell[0]][new_cell[1]], board.random_board[now_cell[0]][
                                        now_cell[1]]

                        now_cell = (None, None)
                        cell_color = (None, None, None)

                    if event.type == pygame.QUIT:
                        gaming = False
                        running = False

                # отрисовка следующего кадра
                screen.fill((0, 0, 0))
                board.render(screen)

                # отрисовка движущейся клетки
                if now_cell != (None, None) and cell_color != (None, None, None):
                    pygame.draw.rect(screen, (0, 0, 0), (
                        (now_cell[0] * board.cell_size_x, now_cell[1] * board.cell_size_y + board.top),
                        (board.cell_size_x, board.cell_size_y)))
                    pygame.draw.rect(screen, cell_color, (
                        (mouse_pos[0] - click_width, mouse_pos[1] - click_height),
                        (board.cell_size_x, board.cell_size_y)))

                pygame.display.flip()

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
                    gaming = False
            else:
                state = 'menu'

        pygame.display.flip()
    pygame.quit()

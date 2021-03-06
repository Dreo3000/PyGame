from random import randint

import pygame as pygame
from pygame.font import Font

BLACK_COLOR = pygame.Color('black')
WHITE_COLOR = pygame.Color('white')
GRAY_COLOR = pygame.Color('dimgray')
BLUE_COLOR = pygame.Color('blue')
DARK_GREEN_COLOR = pygame.Color('forestgreen')
GREEN_COLOR = pygame.Color('green')
RED_COLOR = pygame.Color('red')

FPS = 30

TILE = 30
W_TILES, H_TILES = 19, 19

SCREEN_SIZE = WIDTH, HEIGHT = W_TILES * TILE, H_TILES * TILE

# world state
# 0 - нолик
# 1 - крестик
# -1 - пустота
#cells = [[randint(-1, 1) for i in range(WIDTH // TILE)] for j in range(H_TILES)]
cells = [[-1 for i in range(WIDTH // TILE)] for j in range(H_TILES)]

mouse_x, mouse_y = 0, 0

# control flags
# x, o
turn = "x"

# "x", "o", ""
winner = ""

def check_winner(cells):
    # return "o"
    # return "x"
    # return ""
    pass

def draw(screen):
    screen.fill(BLACK_COLOR)

    # cells
    for x in range(W_TILES):
        for y in range(H_TILES):
            if cells[y][x] == 1:
                # draw x
                x_screen = x * TILE
                y_screen = y * TILE
                x_screen_end = x * TILE + TILE
                y_screen_end = y * TILE + TILE
                pygame.draw.line(
                    screen, GREEN_COLOR,
                    (x_screen, y_screen), (x_screen_end, y_screen_end),
                    3
                )

                x_screen = x * TILE
                y_screen = y * TILE + TILE
                x_screen_end = x * TILE + TILE
                y_screen_end = y * TILE

                pygame.draw.line(
                    screen, GREEN_COLOR,
                    (x_screen, y_screen), (x_screen_end, y_screen_end),
                    3
                )
            elif cells[y][x] == 0:
                # draw o
                x_screen = x * TILE + TILE // 2
                y_screen = y * TILE + TILE // 2
                pygame.draw.circle(screen, BLUE_COLOR, (x_screen, y_screen), TILE // 2 - 2, 3)


    # vertical lines
    for x in range(0, WIDTH, TILE):
        pygame.draw.line(screen, GRAY_COLOR, (x, 0), (x, HEIGHT))

    # horizontal lines
    for y in range(0, HEIGHT, TILE):
        pygame.draw.line(screen, GRAY_COLOR, (0, y), (WIDTH, y))

    # debug text
    text_surface = font.render(
        f"fps: {int(clock.get_fps())}, mouse: {mouse_x}, {mouse_y}, turn: {turn}, winner: {winner}",
        1, WHITE_COLOR
    )
    screen.blit(text_surface, (5, 5))

    if winner == "x" or winner == "o":
        text_surface = font.render(f"Победил {winner}!", 1, RED_COLOR)
        screen.blit(text_surface, (WIDTH // 2, HEIGHT // 2))
    else:
        # cursor
        x = mouse_x // TILE
        y = mouse_y // TILE

        x_screen = x * TILE
        y_screen = y * TILE

        pygame.draw.rect(
            screen, RED_COLOR,
            (x_screen, y_screen, TILE, TILE),
            3
        )

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
font = Font(None, 24)
clock = pygame.time.Clock()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            x = mouse_x // TILE
            y = mouse_y // TILE

            if cells[y][x] == -1:
                if turn == "x":
                    cells[y][x] = 1
                    turn = "o"
                elif turn == "o":
                    cells[y][x] = 0
                    turn = "x"


    draw(screen)
    winner = check_winner(cells)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
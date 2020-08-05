import sys
import pygame

import Grid

pygame.init()

size = width, height = 1024, 720
black = 255, 255, 255
theGrid = Grid.Grid()

screen = pygame.display.set_mode(size)
theGrid.create_grid()

simulate = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                simulate = not simulate

    if pygame.mouse.get_pressed()[0]:
        try:
            pos = pygame.mouse.get_pos()
            theGrid.check_for_cell_click(pos)
        except AttributeError:
            pass

    screen.fill(black)
    theGrid.draw_grid(screen)
    pygame.display.flip()

    if simulate:
        theGrid.update_grid()
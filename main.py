import sys
import pygame
import math

import Grid

pygame.init()

screenSize = screenWidth, screenHeight = 1024, 720
backGroundColour = 255, 255, 255
theGrid = Grid.Grid()

leftOverWidth = screenWidth % theGrid.cellSize[0]
leftOverHeight = screenHeight % theGrid.cellSize[1]

if leftOverWidth > 0:
    theGrid.widthOffset = leftOverWidth / 2
if leftOverHeight > 0:
    theGrid.heightOffset = leftOverHeight / 2

theGrid.width = screenWidth // theGrid.cellSize[0]
theGrid.height = screenHeight // theGrid.cellSize[1]

screen = pygame.display.set_mode(screenSize)
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

    screen.fill(backGroundColour)
    theGrid.draw_grid(screen)
    pygame.display.flip()

    if simulate:
        theGrid.update_grid()

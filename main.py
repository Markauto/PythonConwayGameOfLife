import sys
import pygame

import Grid
import ConwaysGameOfLifeController

pygame.init()

screenSize = screenWidth, screenHeight = 1024, 720
backGroundColour = 255, 255, 255
theGrid = Grid.Grid()
FPS = 60
leftOverWidth = screenWidth % theGrid.cellSize[0]
leftOverHeight = screenHeight % theGrid.cellSize[1]

if leftOverWidth > 0:
    theGrid.widthOffset = leftOverWidth / 2
if leftOverHeight > 0:
    theGrid.heightOffset = leftOverHeight / 2

theGrid.width = screenWidth // theGrid.cellSize[0]
theGrid.height = screenHeight // theGrid.cellSize[1]

screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()
theGrid.create_grid()
conwaysGameOfLifeController = ConwaysGameOfLifeController.ConwaysGameOfLifeController(theGrid)
simulate = False

while 1:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                simulate = not simulate
            if event.key == pygame.K_DELETE:
                theGrid.reset_grid()

    mouse1Pressed = pygame.mouse.get_pressed()[0]
    mouse2Pressed = pygame.mouse.get_pressed()[2]
    try:
        pos = pygame.mouse.get_pos()
        theGrid.cell_interaction(pos, mouse1Pressed, mouse2Pressed)
    except AttributeError:
        pass

    screen.fill(backGroundColour)
    theGrid.draw_grid(screen)
    pygame.display.flip()

    if simulate:
        conwaysGameOfLifeController.step()

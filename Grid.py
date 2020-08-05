import pygame
import time

import Cell


class Grid:
    width = 45
    height = 30
    cells = []
    cellSize = (20, 20)

    def create_grid(self):
        rectPosX = 0
        for x in range(self.width):
            rectPosX += self.cellSize[0]
            rectPosY = 0
            cellColumns = []
            for y in range(self.height):
                rectPosY += self.cellSize[1]
                newCell = Cell.Cell()
                newCell.rectangle = pygame.Rect(rectPosX, rectPosY, self.cellSize[0], self.cellSize[1])
                cellColumns.append(newCell)
            self.cells.append(cellColumns)

    def draw_grid(self, surface):
        for column in self.cells:
            for cell in column:
                cell.draw(surface)

    def check_for_cell_click(self, point):
        # Change this to use maths instead of looping round them all
        for column in self.cells:
            for cell in column:
                cell.clicked(point)

    def update_grid(self):
        time.sleep(.1)
        for x in range(len(self.cells)):
            for y in range(len(self.cells[x])):
                cellNeighbors = self.get_cell_neighbors((x, y))
                cell = self.cells[x][y]
                numberOfAliveNeighbors = len([aliveNeighbor for aliveNeighbor in cellNeighbors if aliveNeighbor.alive])
                if numberOfAliveNeighbors < 2:
                    cell.alive = False
                    continue
                if numberOfAliveNeighbors > 3:
                    cell.alive = False
                    continue
                if not cell.alive and numberOfAliveNeighbors == 3:
                    cell.alive = True
                    continue

    def get_cell_neighbors(self, point):
        x = point[0]
        y = point[1]
        cellNeighbors = []
        self.append_cell_to_list((x - 1, y - 1), cellNeighbors)
        self.append_cell_to_list((x, y - 1), cellNeighbors)
        self.append_cell_to_list((x - 1, y), cellNeighbors)
        self.append_cell_to_list((x + 1, y + 1), cellNeighbors)
        self.append_cell_to_list((x, y + 1), cellNeighbors)
        self.append_cell_to_list((x + 1, y), cellNeighbors)
        self.append_cell_to_list((x + 1, y - 1), cellNeighbors)
        self.append_cell_to_list((x - 1, y + 1), cellNeighbors)
        return cellNeighbors

    def append_cell_to_list(self, point, listToAppendTo):
        cellToAppend = self.get_cell(point)
        if cellToAppend is None:
            return
        listToAppendTo.append(cellToAppend)

    def get_cell(self, point):
        if point[0] < 0 or point[1] < 0:
            return

        if point[0] > (len(self.cells) - 1) or point[1] > (len(self.cells[point[0]]) - 1):
            return

        return self.cells[point[0]][point[1]]

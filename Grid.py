import pygame
import time

import Cell


class Grid:
    width = 45
    height = 30
    cells = []
    cellSize = (20, 20)

    widthOffset = 0
    heightOffset = 0

    def create_grid(self):
        rect_pos_x = self.widthOffset
        for x in range(self.width):
            rect_pos_y = self.heightOffset
            cell_columns = []
            for y in range(self.height):
                new_cell = Cell.Cell()
                new_cell.rectangle = pygame.Rect(rect_pos_x, rect_pos_y, self.cellSize[0], self.cellSize[1])
                cell_columns.append(new_cell)
                rect_pos_y += self.cellSize[1]
            self.cells.append(cell_columns)
            rect_pos_x += self.cellSize[0]

    def draw_grid(self, surface):
        for column in self.cells:
            for cell in column:
                cell.draw(surface)

    previousCellOver = Cell.Cell()

    def cell_interaction(self, point, primary, alt):
        self.previousCellOver.clear_hover()
        cellColumn = point[0] // self.cellSize[0]
        cellRow = point[1] // self.cellSize[1]
        cell = self.get_cell((cellColumn, cellRow))
        if cell is None:
            return

        cell.hover()
        self.previousCellOver = cell
        if alt:
            cell.alt_click()
        elif primary:
            cell.clicked()

    def get_cell_neighbors(self, point):
        x = point[0]
        y = point[1]
        cell_neighbors = []
        self.append_cell_to_list((x - 1, y - 1), cell_neighbors)
        self.append_cell_to_list((x, y - 1), cell_neighbors)
        self.append_cell_to_list((x - 1, y), cell_neighbors)
        self.append_cell_to_list((x + 1, y + 1), cell_neighbors)
        self.append_cell_to_list((x, y + 1), cell_neighbors)
        self.append_cell_to_list((x + 1, y), cell_neighbors)
        self.append_cell_to_list((x + 1, y - 1), cell_neighbors)
        self.append_cell_to_list((x - 1, y + 1), cell_neighbors)
        return cell_neighbors

    def append_cell_to_list(self, point, list_to_append_to):
        cell_to_append = self.get_cell(point)
        if cell_to_append is None:
            return
        list_to_append_to.append(cell_to_append)

    def get_cell(self, point):
        if point[0] < 0 or point[1] < 0:
            return

        if point[0] > (len(self.cells) - 1) or point[1] > (len(self.cells[point[0]]) - 1):
            return

        return self.cells[point[0]][point[1]]

    def reset_grid(self):
        for x in range(len(self.cells)):
            for y in range(len(self.cells[x])):
                self.cells[x][y].alive = False

import Grid


class ConwaysGameOfLifeController:
    grid = None

    def __init__(self, gridToUse):
        self.grid = gridToUse

    def step(self):
        for x in range(len(self.grid.cells)):
            for y in range(len(self.grid.cells[x])):
                cell_neighbors = self.grid.get_cell_neighbors((x, y))
                cell = self.grid.cells[x][y]
                number_of_alive_neighbors = len(
                    [aliveNeighbor for aliveNeighbor in cell_neighbors if aliveNeighbor.alive])
                if number_of_alive_neighbors < 2:
                    cell.alive = False
                    continue
                if number_of_alive_neighbors > 3:
                    cell.alive = False
                    continue
                if not cell.alive and number_of_alive_neighbors == 3:
                    cell.alive = True
                    continue

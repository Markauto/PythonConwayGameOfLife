import pygame


class Cell:
    alive = False
    colour = (0, 0, 0)
    rectWidth = 3
    rectangle = pygame.rect.Rect(0, 0, 0, 0)

    def clicked(self, point):
        if not self.rectangle.collidepoint(point):
            return
        self.alive = True

    def draw(self, surface):
        if self.alive:
            self.rectWidth = 0
        else:
            self.rectWidth = 3

        pygame.draw.rect(surface, self.colour, self.rectangle, self.rectWidth)

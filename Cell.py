import pygame


class Cell:
    alive = False
    colour = (0, 0, 0)
    rectWidth = 1
    rectangle = pygame.rect.Rect(0, 0, 0, 0)

    def hover(self):
        self.colour = (255, 0, 0)

    def clear_hover(self):
        self.colour = (0, 0, 0)

    def clicked(self):
        self.alive = True

    def alt_click(self):
        self.alive = False

    def draw(self, surface):
        if self.alive:
            self.rectWidth = 0
        else:
            self.rectWidth = 1

        pygame.draw.rect(surface, self.colour, self.rectangle, self.rectWidth)

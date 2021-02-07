import pygame
from entity import *

class Paddle(Entity):
    def __init__(self, x, y, *args):
        super().__init__(x,y, args[0], args[1])
        self.color = (0,0,0)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 0.25
        if keys[pygame.K_DOWN]:
            self.y += 0.25

    def update(self):
        self.move()
        self.draw()

    def draw(self):
        pygame.draw.rect(pygame.display.get_surface(),self.color, (self.x, self.y, self.width, self.height))

class Enemy(Paddle):
    def move(self):
        pass




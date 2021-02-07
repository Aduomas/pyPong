import pygame
from entity import *


class Ballzzzz(Entity):
    def __init__(self, x, y, radius=12):
        super().__init__(x, y, radius * 2, radius * 2)
        self.radius = radius
        self.color = (255, 0, 0)
        self.velocityX = 0.2
        self.velocityY = -0.2

    def collision(self):
        for entity in getEntityList():
            if entity != self:
                if (entity.x < self.x + self.width and
                        entity.x + entity.width > self.x and
                        entity.y < self.y + self.height and
                        entity.y + entity.height > self.y):
                    print('COLLIDED')
                    self.velocityX = self.velocityX * -1
                    self.velocityY = self.velocityY * -1
                    # FIX THIS


    def update(self):
        self.collision()
        self.move()
        self.draw()

    def draw(self):
        pygame.draw.circle(pygame.display.get_surface(), self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.velocityX
        self.y += self.velocityY

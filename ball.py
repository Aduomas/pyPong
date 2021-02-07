import pygame
from entity import *
import random


class Ballzzzz(Entity):
    def __init__(self, x, y, radius=12):
        super().__init__(x, y, radius * 2, radius * 2)
        self.radius = radius
        self.color = (255, 0, 0)
        self.velocityX = 0.2
        self.velocityY = 0

    def restart(self):
        # RESTART
        print('you died')



    def collision(self):
        screenWidth = pygame.display.get_surface().get_width()
        screenHeight = pygame.display.get_surface().get_height()

        paddle = getEntityList()[0]
        rightBorder = getEntityList()[1]

        if self.x >= screenWidth - self.width - rightBorder.width/2 or\
                self.x <= self.width + paddle.width/2 + paddle.x and\
                (self.y + self.height > paddle.y and self.y < paddle.y + paddle.height):
            self.velocityX *= -1
            self.velocityY = random.uniform(-0.3, 0.3)

        if self.y > screenHeight - self.height/2 or self.y < self.height/2:
            self.velocityY *= -1

        # if self.y > self.height or self.y < screenHeight - self.height:
        #     self.velocityY *= -1






    def update(self):
        self.collision()
        self.move()
        self.draw()

    def draw(self):
        pygame.draw.circle(pygame.display.get_surface(), self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.velocityX
        self.y += self.velocityY

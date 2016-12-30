from base_shape import BaseShape
import pygame, math
from random import (randint, randrange, random)
from operator import add

black = (0, 0, 0)
white = (255, 255, 255)

class Star():
    def __init__(self, rect):
        direction = randrange(100000)
        velmult = random() + 0.2
        self.vel = [math.sin(direction) * velmult,
                    math.cos(direction) * velmult]
        self.rect = rect

        self.reset()

    def move(self):
        self.pos = map(add, self.pos, self.vel)

    def get_pos(self):
        return self.pos

    def display(self, screen, color):
        pos = [int(self.pos[0]), int(self.pos[1])]
        screen.set_at(pos, color)

    def reset(self):
        self.pos = [randint(self.rect.left, self.rect.right),
                    randint(self.rect.top, self.rect.bottom)]

class StarfieldShape(BaseShape):
    def __init__(self, screen, polygon):
        super(StarfieldShape, self).__init__(screen, polygon)

        self.stars = [Star(self.polygon.get_rect()) for i in range(1000)]
        
    def draw(self):
        for star in self.stars:
            star.display(self.screen, black)
            star.move()
            if not self.polygon.contains_point(star.get_pos()):
                star.reset()
            else:
                star.display(self.screen, white)

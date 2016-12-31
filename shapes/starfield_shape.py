from base_shape import BaseShape
import pygame, math
from random import (randint, randrange, random)
from operator import add

BLACK = (0, 0, 0)
STARCOLOR = (255, 255, 255)

DENSITY = 0.005
SPEED = 1
STARSIZE = 3

class Star():
    def __init__(self, rect):
        direction = randrange(100000)
        velmult = (random() + 0.2) * SPEED
        self.vel = [math.sin(direction) * velmult,
                    math.cos(direction) * velmult]
        self.rect = rect
        self.reset()

        
    def move(self):
        self.pos = map(add, self.pos, self.vel)

        
    def get_pos(self):
        return self.pos

    
    def display(self, screen, color):
        x, y = int(self.pos[0]), int(self.pos[1])
        for i in range(STARSIZE):
            for j in range(STARSIZE):
                pos = (x + i, y + j)
                screen.set_at(pos, color)

        
    def reset(self):
        self.pos = [randint(self.rect.left, self.rect.right),
                    randint(self.rect.top, self.rect.bottom)]

        
class StarfieldShape(BaseShape):
    def __init__(self, screen, polygon):
        super(StarfieldShape, self).__init__(screen, polygon)
        rect_area = polygon.get_rect().width * polygon.get_rect().height
        num_stars = int(rect_area * DENSITY)
        self.stars = [Star(self.polygon.get_rect()) for _ in range(num_stars)]

        
    def draw(self):
        for star in self.stars:
            star.display(self.screen, BLACK)
            star.move()
            if not self.polygon.contains_point(star.get_pos()):
                star.reset()
            else:
                star.display(self.screen, STARCOLOR)

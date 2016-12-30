from base_shape import BaseShape
import pygame
from random import randint
from operator import add

class ColorShiftShape(BaseShape):
    def __init__(self, screen, polygon):
        super(ColorShiftShape, self).__init__(screen, polygon)

        self.min_intensity = 300

        self.rgb = [randint(0, 255) for i in range(0, 3)]
        self.deltas = [randint(-3, 3) for i in range(0, 3)]

    def update_rgb(self):
        rgb_new = map(add, self.rgb, self.deltas)
        
        intensity = sum(rgb_new)
        if intensity < self.min_intensity:
            extra = int((self.min_intensity - intensity) / 3)
            rgb_new = [x + extra for x in rgb_new]

        rgb_new = [max(0, min(x, 255)) for x in rgb_new]

        self.rgb = rgb_new

    def update_deltas(self):
        deltas_new = [d + randint(-1, 1) for d in self.deltas]
        deltas_new = [max(-4, min(d, 4)) for d in deltas_new]
        self.deltas = deltas_new
        
    def draw(self):
        self.update_rgb()
        self.update_deltas()
        pygame.draw.polygon(self.screen, self.rgb, self.polygon.get_points())
        

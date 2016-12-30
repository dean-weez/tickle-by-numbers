from base_shape import BaseShape
import pygame

class SolidShape(BaseShape):
    def set_color(self, color):
        self.color = color
        
    def draw(self):
        pygame.draw.polygon(self.screen, self.color, self.polygon.get_points())

import pygame


class Drawer():
    def __init__(self, screen):
        self.points = []
        self.screen = screen
        self.last_mouse_pos = (0,0)

        
    def add_point(self, pt):
        self.points.append(pt)


    def remove_point(self):
        self.points.pop()

        
    def clear_points(self):
        black = (0, 0, 0)
        if len(self.points) > 1:
            pygame.draw.lines(self.screen, black, False, self.points)
        
        self.points = []

        
    def get_points(self):
        return self.points

    
    def draw(self):
        white = (255, 255, 255)        
        black = (0, 0, 0)
        if len(self.points) > 0:
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.line(self.screen, black, self.points[-1], self.last_mouse_pos)
            pygame.draw.line(self.screen, white, self.points[-1], mouse_pos)
            self.last_mouse_pos = mouse_pos
        if len(self.points) > 1:
            pygame.draw.lines(self.screen, white, False, self.points)
        

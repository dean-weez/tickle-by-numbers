import sys, pygame
from pygame.locals import *
from shapes.starfield_shape import StarfieldShape
from polygon import Polygon

class Drawer():
    def __init__(self, screen):
        self.points = []
        self.screen = screen
        self.last_mouse_pos = (0,0)
        
    def add_point(self, pt):
        self.points.append(pt)

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
        
            

def main():
    pygame.init()

    size = width, height = 800, 600
    black = (0, 0, 0)
    #screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode(size)
    screen.fill(black)
    drawer = Drawer(screen)
    clock = pygame.time.Clock()
    shapes = []
    going = True
    drawing, clicking = False, False
    
    while going:
        clock.tick(30)

        # Handle any user input
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            if event.type == KEYDOWN:
                if event.key == K_q:
                    going = False
                if event.key == K_d:
                    print ('starting draw')
                    drawing = True
                if event.key == K_f and drawing:
                    print ('finishing draw')
                    pts = drawer.get_points()
                    polygon = Polygon(pts)
                    
                    shapes.append(StarfieldShape(screen, polygon))
                    drawer.clear_points()
                    drawing = False
            if event.type == MOUSEBUTTONDOWN and not clicking:
                x, y = pygame.mouse.get_pos()
                if drawing:
                    drawer.add_point((x, y))
                clicking = True
            if event.type == MOUSEBUTTONUP:
                clicking = False

        # Refresh all shapes
        for shape in shapes:
            shape.draw()

        # If drawing, show lines
        if drawing:
            drawer.draw()
            
        pygame.display.flip()
        
    pygame.quit()

if __name__ == '__main__':
    main()
    

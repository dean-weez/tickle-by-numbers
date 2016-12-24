import sys, pygame
from pygame.locals import *

class Drawer():
    def __init__(self):
        self.points = []
        
    def add_point(self, pt):
        self.points.append(pt)

    def clear_points(self):
        self.points = []

    def get_points(self):
        return self.points

def main():
    pygame.init()

    size = width, height = 600, 400

    black = (0, 0, 0)
    red = (255, 0, 0)
    white = (255, 255, 255)

    screen = pygame.display.set_mode(size)
    screen.fill(black)

    clock = pygame.time.Clock()

    drawing, clicking = False, False

    drawer = Drawer()
    
    while True:
        clock.tick(40)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_d:
                    print ('starting draw')
                    drawing = True
                if event.key == K_q and drawing:
                    print ('finishing draw')
                    pts = drawer.get_points()
                    pygame.draw.aalines(screen, red, True, pts)
                    pygame.draw.polygon(screen, red, pts)
                    drawer.clear_points()
                    drawing = False
            if event.type == MOUSEBUTTONDOWN and not clicking:
                x, y = pygame.mouse.get_pos()
                if drawing:
                    drawer.add_point((x, y))
                clicking = True
            if event.type == MOUSEBUTTONUP:
                clicking = False

        pygame.display.flip()
        
    pygame.quit()

if __name__ == '__main__':
    main()
    

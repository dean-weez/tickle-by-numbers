import pygame
from pygame.locals import *
from shapes.starfield_shape import StarfieldShape
from shapes.color_shift_shape import ColorShiftShape
from drawer import Drawer
from polygon import Polygon


def main():
    pygame.init()

    size = width, height = 800, 600
    black = (0, 0, 0)
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    #screen = pygame.display.set_mode(size)
    screen.fill(black)
    drawer = Drawer(screen)
    clock = pygame.time.Clock()
    shapes = []
    going = True
    drawing, clicking = False, False
    
    while going:
        clock.tick(30)

        screen.fill(black)

        # Handle any user input
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            if event.type == KEYDOWN:
                if event.key == K_q:
                    going = False
                if event.key == K_d:
                    drawing = True
                if event.key == K_s and drawing:
                    pts = drawer.get_points()
                    polygon = Polygon(pts)
                    shapes.append(StarfieldShape(screen, polygon))
                    drawer.clear_points()
                    drawing = False
                if event.key == K_c and drawing:
                    pts = drawer.get_points()
                    polygon = Polygon(pts)
                    shapes.append(ColorShiftShape(screen, polygon))
                    drawer.clear_points()
                    drawing = False
                if event.key == K_b:
                    if drawing:
                        drawer.remove_point()
                    elif len(shapes) > 0:
                        shapes.pop()
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
    

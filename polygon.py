from __future__ import division
import pygame

class Polygon():
    """Defines a polygon"""
    def __init__(self, points):
        self.points = points

        left = min([p[0] for p in points])
        right = max([p[0] for p in points])
        top = min([p[1] for p in points])
        bottom = max([p[1] for p in points])        
        self.rect = pygame.Rect(left, top, right - left, bottom - top)

        self.lines = []
        for i in range(len(points) - 1):
            self.lines.append((points[i], points[i+1]))
        self.lines.append((points[-1], points[0]))

        
    def get_rect(self):
        return self.rect

    
    def get_points(self):
        return self.points

    
    def contains_point(self, pt):
        """Uses ray casting algorithm https://en.wikipedia.org/wiki/Point_in_polygon#Ray_casting_algorithm"""
        if not self.rect.collidepoint:
            # Outside of bounding rectangle, can quickly exclude
            return False

        def ray_intersect(pt, l):
            "Checks if a ray extending right from pt intersects segment l"
            #print(l)
            a = l[0]
            b = l[1]

            # pt must be vertically between endpoints
            if pt[1] <= min(a[1], b[1]):
                return False
            if pt[1] > max(a[1], b[1]):
                return False
            # if line is horizontal, return false:
            if a[1] == b[1]:
                return False

            slope = (b[0] - a[0]) / (b[1] - a[1])
            #print('{0} * ({1} - {2}) + {3} > {4}'.format(slope, pt[1], a[1], a[0], pt[0]))
            y = slope * (pt[1] - a[1]) + a[0]
            return y > pt[0]

        crossings = sum([ray_intersect(pt, l) for l in self.lines])
        return crossings % 2 == 1

    
if __name__ == '__main__':
    points = [(20,20), (20,80), (40, 60), (70,80), (70, 50)]
    poly = Polygon(points)

    print poly.get_rect()

    pt_inside_poly = (25, 62)
    print (pt_inside_poly, poly.contains_point(pt_inside_poly))

    pt_outside_poly = (60, 78)
    print (pt_outside_poly, poly.contains_point(pt_outside_poly))

    pt_aligned = (30, 60)
    print (pt_aligned, poly.contains_point(pt_aligned))

    pt_aligned2 = (40, 50)
    print (pt_aligned2, poly.contains_point(pt_aligned2))


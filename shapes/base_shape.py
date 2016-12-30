class BaseShape(object):
    """Extend this class by implementing a new draw method"""
    def __init__(self, screen, polygon):
        self.screen = screen
        self.polygon = polygon

    def draw(self):
        pass

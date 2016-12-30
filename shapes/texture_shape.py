import pygame

# This is incomplete and non-functional

class TextureShape():
    def __init__(self):
        pass

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill((255,255,255))
    texture = tile_texture(pygame.image.load("texture.png"), SIZE)
    mask = pygame.Surface(SIZE, depth=8)
    # Create sample mask:
    pygame.draw.polygon(mask, 255, 
                        [(random.randrange(SIZE[0]), random.randrange(SIZE[1]) )
                         for _ in range(5)] , 0)

    stamp(screen, texture, mask)
    pygame.display.flip()
    while not any(pygame.key.get_pressed()):
        pygame.event.pump()
        pygame.time.delay(30)

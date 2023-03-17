import pygame

FPS = 60
fpsClock = pygame.time.Clock()


while True:
   pygame.init()
   pygame.display.set_caption("Mario Maker")
   Window = pygame.display.set_mode((1280, 720))
   Window.fill((0, 0, 0))
   pygame.display.update()


   Window.blit(Image, (x, y))
   pygame.display.update()
   fpsClock.tick(FPS)

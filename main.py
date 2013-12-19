import pygame
from Other import color
 
#----Engine and Base Code----
pygame.init()
size = [700,500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")


#----Define----
gaphic_frames = 60


#----Ready----
done = False
clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(color.white)
    pygame.display.flip()
    clock.tick(gaphic_frames)
     
pygame.quit()

import pygame
from Other import color
from Module.Logic_Gates import*
from Module.Gate import Wire
 
#----Engine and Base Code----
pygame.init()
size = [700,500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")


#----Define----
gaphic_frames = 60
gates_list = pygame.sprite.LayeredUpdates()
g = AND_Gate()
w = Wire(g,0)
gates_list.add(g,w)


#----Ready----
done = False
clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(color.white)
    w.draw_image()
    g.rect.x = 100
    g.rect.y = 100
    gates_list.draw(screen)
    pygame.display.flip()
    clock.tick(gaphic_frames)
     
pygame.quit()

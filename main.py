import pygame
from Other import color
from Module.Logic_Gates import*
from Module.Gate import Wire
from Module.lib import snap_to_port
 
#----Engine and Base Code----
pygame.init()
size = [900,600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")


#----Define----
gaphic_frames = 60
gates_list = pygame.sprite.Group()
wires_list = pygame.sprite.Group()
g = AND_Gate()
o = OR_Gate()
n = NOT_Gate()
w = Wire(n,0)
gates_list.add(g,o,n)
wires_list.add(w)
h_wire = w
holding = True

#----Ready----
done = False
clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            if holding:
                holding = False
                snap_to_port(gates_list,h_wire,pygame.mouse.get_pos())
            
    if holding:
        h_wire.update()
    
    screen.fill(color.white)
    g.rect.x = 100
    g.rect.y = 100
    
    o.rect.x = 300
    o.rect.y = 300

    n.rect.x = 200
    n.rect.y = 300
    
    gates_list.draw(screen)
    wires_list.draw(screen)
    pygame.display.flip()
    clock.tick(gaphic_frames)
     
pygame.quit()

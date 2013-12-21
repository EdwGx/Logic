import pygame
from UI import color,controller
from Module.Logic_Gates import*
from Module.Gate import Wire
from UI.lib import snap_to_port

def add_sprite(controller):
    for i in range()
 
#----Engine and Base Code----
pygame.init()
size = [900,600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")


#----Define----
gaphic_frames = 60
gaphic_controller = controller.Graphic()
gates_list = pygame.sprite.LayeredUpdates()
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
            mouse_pos = pygame.mouse.get_pos()
            gaphic_controller.mouse_up(mouse_pos,gates_list,wires_list)
    
    screen.fill(color.white)
    g.rect.x = 100
    g.rect.y = 100
    
    o.rect.x = 300
    o.rect.y = 300

    n.rect.x = 200
    n.rect.y = 300
        
    wires_list.draw(screen)
    gates_list.draw(screen)
    gaphic_controller.draw(screen)
    
    pygame.display.flip()
    clock.tick(gaphic_frames)
     
pygame.quit()

import pygame
from UI import color,controller,sidebar
from Module.Logic_Gates import*
from Module.Gate import Wire
from Module.input import Input
from UI.lib import snap_to_port

#----Engine and Base Code----
pygame.init()
size = [900,600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")


#----Define----
gaphic_frames = 60
gates_group = pygame.sprite.LayeredUpdates()
wires_group = pygame.sprite.Group()
gaphic_controller = controller.Graphic(gates_group,wires_group)
selection_controller = sidebar.SideBar()
g = AND_Gate()
o = OR_Gate()
n = NOT_Gate()
i = Input()
g.rect.x = 100
g.rect.y = 100
    
o.rect.x = 400
o.rect.y = 300

i.rect.x = 500
i.rect.y = 300

n.rect.x = 200
n.rect.y = 300
gates_group.add(g,o,n,i)

#----Ready----
done = False
clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:
                gaphic_controller.mouse_down(mouse_pos)
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:
                gaphic_controller.mouse_up(mouse_pos)
    #Game&Graphic Logic
    gaphic_controller.graphic_logic()
    #Draw
    screen.fill((180,180,180))
    gaphic_controller.draw_buttom_layer(screen)
    screen.blit(pygame.image.load(os.path.join('UI','Resources','selection_bar.png')),(0,0))
    wires_group.draw(screen)
    gates_group.draw(screen)
    gaphic_controller.draw_top_layer(screen)
    selection_controller.draw(screen)
    pygame.display.flip()
    clock.tick(gaphic_frames)
     
pygame.quit()

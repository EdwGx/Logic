import pygame
from UI import color,controller,sidebar
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
selection_controller = sidebar.SideBar(gaphic_controller)
#----Ready----
done = False
clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1 and mouse_pos[0] > 140:
                gaphic_controller.mouse_down(mouse_pos)
            elif event.button == 1:
                selection_controller.mouse_down(mouse_pos)
            elif event.button == 4 and mouse_pos[0] < 140:
                selection_controller.scroll_up()
            elif event.button == 5 and mouse_pos[0] < 140:
                selection_controller.scroll_down()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:
                gaphic_controller.mouse_up(mouse_pos)
    #Game&Graphic Logic
    gaphic_controller.graphic_logic()
    #Draw
    screen.fill((180,180,180))
    gaphic_controller.draw_buttom_layer(screen)
    selection_controller.draw(screen)
    wires_group.draw(screen)
    gates_group.draw(screen)
    gaphic_controller.draw_top_layer(screen)
    pygame.display.flip()
    clock.tick(gaphic_frames)
     
pygame.quit()

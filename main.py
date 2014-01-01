import pygame
from UI import color,controller,sidebar,fileIO,filemenu
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

fileIO.check_file()

gaphic_controller = controller.Graphic(gates_group,wires_group)
selection_controller = sidebar.SideBar(gaphic_controller)
file_controller = filemenu.FileMenu()
#----Ready----
done = False
clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                fileIO.save(gates_group,wires_group)
            elif event.key == pygame.K_l:
                fileIO.load(gates_group,wires_group)
            elif event.key == pygame.K_k:
                gates_group.empty()
                wires_group.empty()
            elif event.key == pygame.K_c:
                screenshot = pygame.Surface((760,600))
                screenshot.blit(screen,(0,0),(140,0,760,600))
                screenshot = pygame.transform.smoothscale(screenshot,(152,120))
                pygame.image.save(screenshot,'shot.png')
                
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if not(file_controller.block_mouse):
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
                if file_controller.block_mouse:
                    ops = file_controller.mouse_up(mouse_pos)
                    if ops[0] == 2:
                        fileIO.save(ops[1],gates_group,wires_group)
                    elif ops[0] == 3:
                        fileIO.load(ops[1],gates_group,wires_group)
                else:
                    if gaphic_controller.event == 0:
                        if(mouse_pos[0] > 760) and (mouse_pos[1] < 36):
                           file_controller.open_menu(mouse_pos)
                    else:
                        gaphic_controller.mouse_up(mouse_pos)
    #Game&Graphic Logic
    if file_controller.draw_menu:
        file_controller.graphic_logic()
    gaphic_controller.graphic_logic()
    #Draw
    screen.fill((149,165,166))
    gaphic_controller.draw_buttom_layer(screen)
    selection_controller.draw(screen)
    wires_group.draw(screen)
    gates_group.draw(screen)
    gaphic_controller.draw_top_layer(screen)
    file_controller.draw(screen)
    pygame.display.flip()
    clock.tick(gaphic_frames)
     
pygame.quit()

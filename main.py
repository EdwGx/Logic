import pygame,os.path
from UI import color,controller,sidebar,fileIO,filemenu
from UI.lib import snap_to_port

#----Engine and Base Code----
pygame.init()
size = [900,600]
screen = pygame.display.set_mode(size,pygame.DOUBLEBUF)
pygame.display.set_caption("Logic")
pygame.event.set_allowed([pygame.QUIT,pygame.KEYDOWN,
                          pygame.MOUSEBUTTONDOWN,pygame.MOUSEBUTTONUP])



#----Define----
gaphic_frames = 60
gates_group = pygame.sprite.LayeredUpdates()
wires_group = pygame.sprite.Group()
background = pygame.image.load(os.path.join('UI','Resources','background.png')).convert()
background.set_alpha(None)
disply_fps = False
log_fps = False
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                disply_fps = not(disply_fps)
            if event.key == pygame.K_l:
                log_fps = not(log_fps)
                
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
    if log_fps:
        f = open('log.txt','a')
        f.write('%.2f\n'%(clock.get_fps()))
        f.close()
    if file_controller.draw_menu:
        file_controller.graphic_logic()
    gaphic_controller.graphic_logic()
    #Draw
    screen.blit(background,(0,0))
    gaphic_controller.draw_buttom_layer(screen)
    selection_controller.draw(screen)
    wires_group.draw(screen)
    gates_group.draw(screen)
    gaphic_controller.draw_top_layer(screen)
    file_controller.draw(screen)
    if disply_fps:
        font = pygame.font.SysFont("Helvetica",20,False)
        label = font.render('%.2f'%(clock.get_fps()),False,(0,0,0))
        screen.blit(label,(830,560))
        
    pygame.display.flip()
    clock.tick(gaphic_frames)
     
pygame.quit()

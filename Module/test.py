import pygame,math
 
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
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(0,0,0),(300,300), 10)
    pos = pygame.mouse.get_pos()
    d = math.sqrt((pos[0]-300)**2 + (pos[1]-300)**2)
    c = pygame.mouse.get_rel()
    if abs(c[0]) >= abs(c[1]):
        ch = c[0]
    else:
        ch = c[1]
    if d < 10 and ch < 1:
        pygame.mouse.set_pos(300,300)

        
    pygame.display.flip()
    clock.tick(gaphic_frames)
     
pygame.quit()

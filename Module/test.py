import pygame,math
def get_angle(pos1,pos2):
    run = float(pos1[0] - pos2[0])
    rai = float(pos1[1] - pos2[1])
    if run == 0:
        rai = 0
        run = 1
    return (math.degrees(math.atan(rai/run)))

def get_rel(degree):
    small = math.radians(90- degree)
    #print math.degrees(small)
    run = 3*math.cos(small)
    rai = 3*math.sin(small)
    print (run,rai)
    return (run,rai)
    
def get_distance(pos1,pos2):
    return int(math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2))
    
def line(surface,pos1,pos2):
    ang = get_angle(pos1,pos2)
    rel = get_rel(ang)
    point1 = (pos1[0]+rel[0],pos1[1]-rel[1])
    point2 = (pos1[0]-rel[0],pos1[1]+rel[1])
    point3 = (pos2[0]-rel[0],pos2[1]+rel[1])
    point4 = (pos2[0]+rel[0],pos2[1]-rel[1])
    if self.status:
       pygame.draw.polygon(surface, color.green, (point1,point2,point3,point4))
    
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
    pos = pygame.mouse.get_pos()
    
    pygame.draw.circle(screen,(0,0,0),(300,300), 10)
    line(screen,(300,300),(pos[0],pos[1]))
    
    
    pygame.display.flip()
    clock.tick(gaphic_frames)
     
pygame.quit()

import pygame,color,os.path,math
class Port:
    def __init__ (self,position=(0,0),multi_connection=False):
        self.multi = False #Multilple connection
        self.position = position
        self.status = False
        self.conn_wire = True
        self.conn_list = []
    def update_status(self,new_status):
        if new_status != self.status:
            self.status = new_status
            self.update_req()

    def update_req(self):
        for wire in self.conn_list:
            wire.update()

        

class logicGate(pygame.sprite.DirtySprite):
    def __init__ (self,gate_type):
        pygame.sprite.DirtySprite.__init__(self)
        #--Base Define--
        self.layer = 5
        self.port = []
        self.port.append(Port((74,20),True))
        self.state = False #output
        
        #--Define--
        self.gate_type = gate_type
        #1.AND 2.OR 3.XOR 4.NAND 5.NOR 6.XNOR 7.NOT
        if gate_type == 7:
            self.port.append(Port((6,20)))
            self.dual_in = False
        else:
            self.port.append(Port((6,12)))
            self.port.append(Port((6,28)))
            self.dual_in = True

        self.image = pygame.image.load(os.path.join('Module','Resources','testGate.png'))
        self.rect = self.image.get_rect()
        self.update()

    def port_pos(self,port_id):
        return((self.rect.x + self.port[port_id].position[0]),
               (self.rect.y + self.port[port_id].position[1]))

class Wire(pygame.sprite.DirtySprite):
    def __init__ (self,module,port):
        pygame.sprite.DirtySprite.__init__(self)
        if port == 0:
            self.start_module = module
            self.start_port = 0
            
            self.end_module = None
            self.end_port = None
        else:
            self.start_module = None
            self.start_port = None
            
            self.end_module = module
            self.end_port = port
        self.status = False
        self.draw_image()

    def update_status(self,new_status):
        if new_status != self.status:
            self.status = new_status
            self.update_req()


    def update_req(self):
        if self.end_module != None:
            self.end_module.port[end_port].status = self.status
            self.end_module.update()
            
    def update(self):
        self.update_status(self.start_module.port[0].status)
        self.draw_image()
        

    def connect_module(self,module,port):
        print(port)
        if port == 0:
            self.start_module = module
            self.start_port = port
        else:
            self.end_module = module
            self.end_port = port
        self.update()
        
        
    def draw_image(self):
        if (self.start_module == None) and (self.end_module == None):
            print('b')
            self.kill()
        else:
            if(self.start_module != None) and (self.end_module != None):
                point1 = self.start_module.port_pos(self.start_port)
                point2 = self.end_module.port_pos(self.end_port)
            elif self.start_module == None:
                point1 = pygame.mouse.get_pos()
                point2 = self.end_module.port_pos(self.end_port)
            elif self.end_module == None:
                point1 = self.start_module.port_pos(self.start_port)
                point2 = pygame.mouse.get_pos()
            #Get some info for graphic
            if point1[0] == point2[0]:
                run = 3
                rai = 0
                if point1[1] < point2[1]:
                    top = (point1[0]-3,point1[1])
                else:
                    top = (point1[0]-3,point2[1])
                    
            else:
                slope = float(point1[1] - point2[1])/float(point1[0] - point2[0])
                angle = 1.57079633 - math.atan(slope)
                run = int(3*math.cos(angle))
                rai = int(3*math.sin(angle))
                if slope > 0:
                    if point1[0] < point2[0]:
                        top = (point1[0]-abs(run),point1[1]-abs(rai))
                    else:
                        top = (point2[0]-abs(run),point2[1]-abs(rai))
                else:
                    if point1[0] < point2[0]:
                        top = (point1[0]-abs(run),point2[1]-abs(rai))
                    else:
                        top = (point2[0]-abs(run),point1[1]-abs(rai))

            poi1 = (point1[0]+run-top[0],point1[1]-rai-top[1])
            poi2 = (point1[0]-run-top[0],point1[1]+rai-top[1])
            poi3 = (point2[0]-run-top[0],point2[1]+rai-top[1])
            poi4 = (point2[0]+run-top[0],point2[1]-rai-top[1])
                    
            length = abs(point1[0] - point2[0])+ abs(run)*2
            width = abs(point1[1] - point2[1])+ abs(rai)*2

            #Getting canves
            self.image = pygame.Surface((length,width),flags=pygame.SRCALPHA)
            self.image.convert_alpha()
            self.rect = self.image.get_rect()
            if self.status:
                pygame.draw.polygon(self.image,color.green, (poi1,poi2,poi3,poi4))
            else:
                pygame.draw.polygon(self.image,color.black, (poi1,poi2,poi3,poi4))
            self.rect.x = top[0]
            self.rect.y = top[1]
 

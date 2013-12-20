import pygame,color,os.path
class Port:
    def __init__ (self,position=(0,0),multi_connection=False):
        self.multi = False #Multilple connection
        self.position = position
        self.status = False
        self.conn_wire = True
        self.conn_list = []
    def update_status(self,new_status):
        if new_status == self.status:
            self.status = new_status
        else:
            self.update_req()

    def update_req():
        for wire in self.conn_list:
            wire.update()
        

class logicGate(pygame.sprite.DirtySprite):
    def __init__ (self,gate_type):
        pygame.sprite.DirtySprite.__init__(self)
        #--Base Define--
        self.layer = 5
        self.port = []
        self.port.append(Port((96,30),True))
        self.state = False #output
        
        #--Define--
        self.gate_type = gate_type
        #1.AND 2.OR 3.XOR 4.NAND 5.NOR 6.XNOR 7.NOT
        if gate_type == 7:
            self.port.append(Port((4,30)))
            self.dual_in = False
        else:
            self.port.append(Port((4,20)))
            self.port.append(Port((4,40)))
            self.dual_in = True

        self.image = pygame.image.load(os.path.join('Module','Resources','testGate.png'))
        #os.path.join('Resources',
        self.rect = self.image.get_rect()

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

    def get_size(self,x1,y1,x2,y2):
        length = abs(x1-x2)+6
        width = abs(y1-y2)+6
        return [length,width]
        
        
    def draw_image(self):
        if (self.start_module == None) and (self.end_module == None):
            self.kill()
        else:
            if(self.start_module != None) and (self.end_module != None):
                point1 = self.start_module.port_pos(self.start_port)
                point2 = self.end_module.port_pos(self.start_port)
            elif self.start_module == None:
                point1 = pygame.mouse.get_pos()
                point2 = self.end_module.port_pos(self.start_port)
            elif self.end_module == None:
                point1 = self.start_module.port_pos(self.start_port)
                point2 = pygame.mouse.get_pos()
            
            image_size = self.get_size(point1[0],point1[1],point2[0],point2[1])
            if image_size[0] < 4:
                image_size[0] = 4
            if image_size[1] < 4:
                image_size[1] = 4
            
            self.image = pygame.Surface(image_size,flags=pygame.SRCALPHA)
            self.image.convert_alpha()
            self.rect = self.image.get_rect()

            if (point1[0] < point2[0]) and (point1[1] < point2[1]):
                self.rect.x = point1[0]
                self.rect.y = point1[1]-3
                line_start = [0,0]
                line_end = image_size
                
            elif (point1[0] > point2[0]) and (point1[1] > point2[1]):
                self.rect.x = point2[0]
                self.rect.y = point2[1]-3
                line_start = [0,0]
                line_end = image_size

            elif (point1[0] < point2[0]) and (point1[1] > point2[1]):
                self.rect.x = point1[0]
                self.rect.y = point2[1]
                line_start = [0,image_size[1]-6]
                line_end = [image_size[0],0]
                
            elif (point1[0] > point2[0]) and (point1[1] < point2[1]):
                self.rect.x = point2[0]
                self.rect.y = point1[1]
                line_start = [0,image_size[1]-6]
                line_end = [image_size[0],0]

            elif point1[0] == point2[0]:
                if point1[1] <= point2[1]:
                    self.rect.x = point1[0]
                    self.rect.y = point1[1]
                    line_start = [0,0]
                    line_end = [image_size[0],0]
                else:
                    self.rect.x = point2[0]
                    self.rect.y = point2[1]
                    line_start = [0,0]
                    line_end = [image_size[0],0]

            elif point1[1] == point2[1]:
                if point1[0] <= point2[0]:
                    self.rect.x = point1[0]
                    self.rect.y = point1[1]
                    line_start = [0,0]
                    line_end = [image_size[0],0]
                else:
                    self.rect.x = point2[0]
                    self.rect.y = point2[1]
                    line_start = [0,0]
                    line_end = [image_size[0],0]
                    
                    
            if self.status:
                pygame.draw.line(self.image,color.green,line_start,line_end,6)
            else:
                pygame.draw.line(self.image,color.black,line_start,line_end,6)
            

            
                
                
                
            
        
        
        

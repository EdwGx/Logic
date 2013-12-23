import pygame,color,os.path,math
class Port:
    def __init__ (self,position=(0,0),multi_connection=False):
        self.multi = multi_connection #Multilple connection
        self.position = position
        self.status = False
        self.conn_wire = True
        self.conn_list = []
    def set_default_status(self):
        self.update_status(False)
    
    def update_status(self,new_status):
        if new_status != self.status:
            self.status = new_status
            self.update_req()

    def update(self):
        if self.multi == False:
            if len(self.conn_list) == 1:
                self.status = self.conn_list[0].status

    def update_req(self):
        for wire in self.conn_list:
            wire.update()

    def connect_wire(self,wire):
        self.conn_list.append(wire)

    def kill_wire(self):
        for wire in self.conn_list:
            wire.kill()
        #Unknow bug,it can't kill all wire
        for wire in self.conn_list:
            wire.kill()
        self.conn_list = []
            

    def is_enough_wire(self):
        if self.conn_wire:
            if self.multi:
                return True
            elif len(self.conn_list) == 0:
                return True
            else:
                return False
        else:
            return False

        

class logicGate(pygame.sprite.DirtySprite):
    def __init__ (self,gate_type):
        pygame.sprite.DirtySprite.__init__(self)
        #--Base Define--
        self.layer = 5
        self.port = []
        self.state = False #output
        self.deleting = False 
        
        #--Define--
        self.gate_type = gate_type
        #1.AND 2.OR 3.XOR 4.NAND 5.NOR 6.XNOR 7.NOT 8.INPUT
        if gate_type == 7:
            self.port.append(Port((74,20),True))
            self.port.append(Port((6,20)))
            self.dual_in = False
        elif gate_type < 7 :
            self.port.append(Port((74,20),True))
            self.port.append(Port((6,12)))
            self.port.append(Port((6,28)))
            self.dual_in = True

    def update(self):
        for port in self.port:
            port.update()

    def click_res(self,rel_pos):
        return True

    def kill(self):
        self.deleting = True
        for port in self.port:
            port.kill_wire()
        pygame.sprite.DirtySprite.kill(self)

    def port_pos(self,port_id):
        return((self.rect.x + self.port[port_id].position[0]),
               (self.rect.y + self.port[port_id].position[1]))

    def number_of_ports(self):
        return len(self.port)

    def move_update(self):
        for port in self.port:
            port.update_req()
            

class Wire(pygame.sprite.DirtySprite):
    def __init__ (self,module,port):
        pygame.sprite.DirtySprite.__init__(self)
        if port == 0:
            self.start_module = module
            self.start_port = 0
            self.start_module.port[self.start_port].connect_wire(self)
            
            self.end_module = None
            self.end_port = None
        else:
            self.start_module = None
            self.start_port = None
            
            self.end_module = module
            self.end_port = port
            self.end_module.port[self.end_port].connect_wire(self)
        self.status = False
        self.draw_image()

    def update_status(self,new_status):
        if new_status != self.status:
            self.status = new_status
            self.update_req()


    def update_req(self):
        if self.end_module != None:
            self.end_module.port[self.end_port].status = self.status
            self.end_module.update()
            
    def update(self):
        if self.start_module == None:
            self.update_status(False)
        else:
            self.update_status(self.start_module.port[0].status)
        self.draw_image()

    def kill(self):
        if self.start_module != None:
            if self in self.start_module.port[self.start_port].conn_list: 
                self.start_module.port[self.start_port].conn_list.remove(self)
        if self.end_module != None:
            if self.end_module.deleting == False:
                if self in self.end_module.port[self.end_port].conn_list: 
                    self.end_module.port[self.end_port].set_default_status()
                    self.end_module.port[self.end_port].conn_list.remove(self)
        pygame.sprite.DirtySprite.kill(self)
        

    def connect_module(self,module,port):
        if port == 0:
            self.start_module = module
            self.start_port = port
        else:
            self.end_module = module
            self.end_port = port
        module.port[port].connect_wire(self)
        module.update()
        self.update()
        
        
    def draw_image(self):
        if (self.start_module == None) and (self.end_module == None):
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
 

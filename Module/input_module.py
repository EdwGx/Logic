from Gate import logicGate,Port
import pygame.image,os.path
class Input(logicGate):
    def __init__(self):
        logicGate.__init__(self,8)
        self.port.append(Port((32,30),True)) #OUTPUT
        self.port.append(Port((40,30),False))
        self.port[1].conn_wire = False
        self.margin = 10
        self.draw_image()
        self.rect = self.image.get_rect()

    def update(self):
        self.port[0].update()
        self.draw_image()


    def port_pos(self,port_id):
        return((self.rect.x + self.port[port_id].position[0]),
               (self.rect.y + self.port[port_id].position[1]))

    def number_of_ports(self):
        return 1

    def change_status(self):
        self.status = not(self.status)
        for port in self.port:
            port.update_status(self.status)
        self.update()
    
    def click_res(self,rel_pos):
        if rel_pos[0] > self.margin and rel_pos[0] < (self.rect.width - self.margin):
            if rel_pos[1] > self.margin and rel_pos[0] < (self.rect.height - self.margin):
                self.change_status()
                return True
            else:
                return True
        else:
            return True
                
    def move_update(self):
        for port in self.port:
            port.update_req()

    def draw_image(self):
        if self.status:
            self.image = pygame.image.load(os.path.join('Module','Resources','switch_on.png'))
        else:
            self.image = pygame.image.load(os.path.join('Module','Resources','switch_off.png'))

class Button(Input):
    def __init__(self):
        logicGate.__init__(self,9)
        self.port.append(Port((44,20),True)) #OUTPUT
        self.port.append(Port((20,20),False))
        self.port[1].conn_wire = False
        self.margin = 10
        self.draw_image()
        self.rect = self.image.get_rect()

    def click_res(self,rel_pos):
        if rel_pos[0] > self.margin and rel_pos[0] < (self.rect.width - self.margin):
            if rel_pos[1] > self.margin and rel_pos[0] < (self.rect.height - self.margin):
                self.status = True
                for port in self.port:
                    port.update_status(True)
                self.update()
                return True
            else:
                return True
        else:
            return True

    def mouse_up(self):
        self.status = False
        for port in self.port:
            port.update_status(False)
        self.update()
        
    def draw_image(self):
        if self.status:
            self.image = pygame.image.load(os.path.join('Module','Resources','button_on.png'))
        else:
            self.image = pygame.image.load(os.path.join('Module','Resources','button_off.png'))
        

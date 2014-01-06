from Module.Gate import logicGate,Port
import pygame.image,os.path
class Output(logicGate):
    def __init__(self):
        logicGate.__init__(self,10)
        self.port.append(Port((20,10),True)) #OUTPUT
        self.port.append(Port((20,54),False))
        self.port[0].conn_wire = False
        self.reqr_real = True
        self.real_input = False
        self.draw_image()
        self.rect = self.image.get_rect()

    def update(self):
        self.status = self.port[1].status
        self.port[0].status = self.port[1].status
        self.draw_image()

    def number_of_ports(self):
        return 2

    def click_res(self,rel_pos):
        return True
                
    def move_update(self):
        for port in self.port:
            port.update_req(True)

    def draw_image(self):
        if self.status and self.port[0].real_input:
            self.image = pygame.image.load(os.path.join('Module','Resources','bulb_on.png')).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join('Module','Resources','bulb_off.png')).convert_alpha()

    def update_real_input(self):
        logicGate.update_real_input(self)
        self.draw_image()

class Hexdisplay(Output):
    def __init__(self):
        logicGate.__init__(self,10)
        self.port.append(Port((20,10),True)) #OUTPUT
        #INPUT
        self.port.append(Port((6,16),False))
        self.port.append(Port((6,32),False))
        self.port.append(Port((6,48),False))
        self.port.append(Port((6,64),False))
        
        self.port[0].conn_wire = False
        self.reqr_real = True
        self.real_input = False
        self.dual_in = True
        self.multi_in = True
        self.hex = ''
        self.draw_image()
        self.rect = self.image.get_rect()
        
    def update(self):
        self.update_value()
        self.draw_image()
        
    def number_of_ports(self):
        return 5

    def update_real_input(self):
        self.port[0].new_real_input(self.port[1].real_input and self.port[2].real_input and self.port[3].real_input and self.port[4].real_input)

    def update_value(self):
        dec = 0
        if self.port[0].real_input:
            if self.port[1].status:
                dec += 8
            if self.port[2].status:
                dec += 4
            if self.port[3].status:
                dec += 2
            if self.port[4].status:
                dec += 1
            self.hex = hex(dec)
        
    def draw_image(self):
        if self.port[0].real_input == False :
            self.image = self.image = pygame.image.load(os.path.join('Module','Resources','hexdisplay_off.png')).convert_alpha()
        else:
            image_name = 'display' + self.hex + '.png'
            self.image = self.image = pygame.image.load(os.path.join('Module','Resources',image_name)).convert_alpha()

        


from Gate import logicGate,Port
import pygame.image,os.path
class Output(logicGate):
    def __init__(self):
        logicGate.__init__(self,10)
        self.port.append(Port((20,10),True)) #OUTPUT
        self.port.append(Port((20,54),False))
        self.port[0].conn_wire = False
        self.reqr_real = False
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
        


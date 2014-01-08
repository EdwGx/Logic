from Module.Gate import logicGate
import pygame.image,os.path
from Module import Logic

class AND_Gate(logicGate):
    def __init__(self):
        logicGate.__init__(self,1)
        self.reqr_real = True
        self.image = pygame.image.load(os.path.join('Module','Resources','and_gate.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):
        logicGate.update(self)
        if not(self.reqr_real) or (self.port[1].real_input and self.port[2].real_input):
            self.port[0].update_status(Logic.ANDG(self.port[1].status,self.port[2].status))

class OR_Gate(logicGate):
    def __init__(self):
        logicGate.__init__(self,2)
        self.reqr_real = True
        self.image = pygame.image.load(os.path.join('Module','Resources','or_gate.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):
        logicGate.update(self)
        if not(self.reqr_real) or (self.port[1].real_input and self.port[2].real_input):
            self.port[0].update_status(Logic.ORG(self.port[1].status,self.port[2].status))

class NOT_Gate(logicGate):
    def __init__(self):
        logicGate.__init__(self,7)
        self.reqr_real = True
        self.image = pygame.image.load(os.path.join('Module','Resources','not_gate.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):
        logicGate.update(self)
        if not(self.reqr_real) or (self.port[1].real_input):
            self.port[0].update_status(Logic.NOTG(self.port[1].status))

class XOR_Gate(logicGate):
    def __init__(self):
        logicGate.__init__(self,3)
        self.reqr_real = True
        self.image = pygame.image.load(os.path.join('Module','Resources','xor_gate.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):
        logicGate.update(self)
        if not(self.reqr_real) or (self.port[1].real_input and self.port[2].real_input):
            self.port[0].update_status(Logic.XORG(self.port[1].status,self.port[2].status))

class NAND_Gate(logicGate):
    def __init__(self):
        logicGate.__init__(self,4)
        self.reqr_real = True
        self.image = pygame.image.load(os.path.join('Module','Resources','nand_gate.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):
        logicGate.update(self)
        if not(self.reqr_real) or (self.port[1].real_input and self.port[2].real_input):
            self.port[0].update_status(Logic.NANDG(self.port[1].status,self.port[2].status))

class NOR_Gate(logicGate):
    def __init__(self):
        logicGate.__init__(self,5)
        self.reqr_real = True
        self.image = pygame.image.load(os.path.join('Module','Resources','nor_gate.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):
        logicGate.update(self)
        if not(self.reqr_real) or (self.port[1].real_input and self.port[2].real_input):
            self.port[0].update_status(Logic.NORG(self.port[1].status,self.port[2].status))

class XNOR_Gate(logicGate):
    def __init__(self):
        logicGate.__init__(self,6)
        self.reqr_real = True
        self.image = pygame.image.load(os.path.join('Module','Resources','xnor_gate.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):
        logicGate.update(self)
        if not(self.reqr_real) or (self.port[1].real_input and self.port[2].real_input):
            self.port[0].update_status(Logic.XNORG(self.port[1].status,self.port[2].status))



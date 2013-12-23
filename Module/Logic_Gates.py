from Gate import logicGate
import Logic,pygame.image,os.path

class AND_Gate(logicGate):
    def __init__(self):
        logicGate.__init__(self,1)
        self.image = pygame.image.load(os.path.join('Module','Resources','and_gate.png'))
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):
        logicGate.update(self)
        self.port[0].update_status(Logic.ANDG(self.port[1].status,self.port[2].status))

class OR_Gate(logicGate):
    def __init__(self):
        logicGate.__init__(self,2)
        self.image = pygame.image.load(os.path.join('Module','Resources','or_gate.png'))
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):
        logicGate.update(self)
        self.port[0].update_status(Logic.ORG(self.port[1].status,self.port[2].status))

class NOT_Gate(logicGate):
    def __init__(self):
        logicGate.__init__(self,7)
        self.image = pygame.image.load(os.path.join('Module','Resources','not_gate.png'))
        self.rect = self.image.get_rect()
        self.update()
        
    def update(self):
        logicGate.update(self)
        self.port[0].update_status(Logic.NOTG(self.port[1].status))



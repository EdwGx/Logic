import pygame
class Port(self):
    def __init__ (self,position=(0,0),multi_connection=False):
        self.multi = False #Multilple connection
        self.position = position
        self.status = False
        self.conn_list = []


class logicGate(pygame.sprite.DirtySprite):
    def __init__ (self,gate_type):
        pygame.sprite.DirtySprite.__init__(self)
        #--Base Define--
        self.layer = 5
        self.gid = 0 #unique id in the game
        self.porto_1 = Port(96,30,True)
        self.state = False #output
        
        #--Define--
        self.gate_type = gate_type
        #1.AND 2.OR 3.XOR 4.NAND 5.NOR 6.XNOR 7.NOT
        if gate_type == 7:
            self.porti_1 = Port(4,30)
            self.port_in = 1
        else:
            self.porti_1 = Port(4,20)
            self.porti_2 = Port(4,40)
            self.port_in = 2

        #--image--
        self.image = pygame.image.load(os.path.join('Resources','testGate.png'))
        
        

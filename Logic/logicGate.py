import pygame

class logicGate(pygame.sprite.DirtySprite):
    def __init__ (self,gate_type):
        pygame.sprite.DirtySprite.__init__(self)
        self.layer = 5
        self.gate_type = gate_type
        #1.AND 2.OR 3.XOR 4.NAND 5.NOR 6.XNOR 7.NOT
        

from lib import select_sprite,snap_to_port
class Controller:
    def __init__(self):
        pass

class Graphic(Controller):
    def __init__(self,gates_group,wire_group):
        Controller.__init__(self)
        self.event = 0
        self.c_wire = None
        self.delete_timer = 0
        self.delete_module = None
        self.delete_port = None
        self.delete_icon = pygame.image.load(os.path.join('UI','Resources','delete_icon.png'))
        #0:Nothing ; 1:Controlling wire
        #2:Draging module; 3:Draging new module;
        #pygame.image.load(os.path.join('Module','Resources','testGate.png'))
        self.gates_group = gates_group
        self.wire_group = wire_group
    def mouse_up(self,pos):
        if self.event == 0:
            select_sprite (self.gates_group,pos,self)
        elif self.event == 1:
            self.event = 0
            snap_to_port(self.gates_group,self.new_wire,pos)
            self.new_wire = None
            
    def click_on_port(self,module,port_id):
        if module.port[port_id].is_enough_wire:
            self.new_wire = Wire(module,port_id)
            self.wire_group.add(self.new_wire)
        self.delete_timer = 300
        self.delete_module = module
        self.delete_port = port_id
            

    def click_on_module(self,module):
        self.delete_timer = 300
        self.delete_module = module
        self.delete_port = None


    def draw(surface):
        wires_list.draw(surface)
        gates_list.draw(surface)
        #Delete Icon
        if self.delete_timer > 0:
            self.delete_timer -= 1
            if self.delete_port == None:
                icon_pos = self.delete_module.rect.center
                icon_pos[0] -= 10
                icon_pos[1] -= 10
                surface.blit(self.delete_icon ,icon_pos)
            else:
                

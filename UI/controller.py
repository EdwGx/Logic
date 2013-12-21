from lib import select_sprite,snap_to_port
class Controller:
    def __init__(self):
        pass

class Graphic(Controller):
    def __init__(self):
        Controller.__init__(self)
        self.event = 0
        self.c_wire = None
        self.delete_timer = 0
        self.delete_module = None
        self.delete_port = None

        self.add_list=[0]
        #0:Nothing ; 1:Controlling wire
        #2:Draging module; 3:Draging new module;
        #pygame.image.load(os.path.join('Module','Resources','testGate.png'))
    def mouse_up(self,pos,gates_group):
        if self.event == 0:
            self.wire_group = wire_group
            select_sprite (gates_group,pos,self)
        elif self.event == 1:
            self.event = 0
            snap_to_port(gates_group,c_wire,pos)
            
    def click_on_port(self,module,port_id):
        if 

    def click_on_module(self,module):


    def draw(surface)

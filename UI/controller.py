from lib import select_sprite,snap_to_port,get_dis_nsqrt
import pygame.image,os.path,sys
sys.path.append("..")
from Module.Gate import Wire
from Module import Logic_Gates,input_module
class Controller:
    def __init__(self):
        pass

class Graphic(Controller):
    def __init__(self,gates_group,wires_group):
        Controller.__init__(self)
        self.event = 0
        self.new_wire = None
        self.side_bar = None
        #Delete
        self.delete_timer = 0
        self.delete_draw = False
        self.delete_module = None
        self.delete_port = None
        self.deleting = False
        self.delete_icon = pygame.image.load(os.path.join('UI','Resources','delete_icon.png'))
        self.delete_rect = self.delete_icon.get_rect()
        #Delete Corner
        self.draw_delc = False
        self.draw_delc2 = False
        self.draw_delc_delay = 0
        self.draw_delc_p = 0
        self.delc_pic =[pygame.image.load(os.path.join('UI','Resources','delete_corner1.png')),
                    pygame.image.load(os.path.join('UI','Resources','delete_corner2.png'))]
        self.delc_pic2 = pygame.image.load(os.path.join('UI','Resources','Selection_bar_del.png'))
                    
        #Drag
        self.drag_module = None
        self.drag_mPos = (0,0)
        self.double_click = False
        #Group
        self.gates_group = gates_group
        self.wires_group = wires_group
        #0:Nothing ; 1:Controlling wire
        #2:Draging module; 3:Draging new module;
    def mouse_down(self,pos):
        if self.event == 0:
            select_sprite (self.gates_group,pos,self)

            
    def mouse_up(self,pos):
        if self.delete_timer > 0:
            dis = get_dis_nsqrt(self.delete_rect.center,pos)
            if dis <= 110:
                self.click_on_delete()
                self.deleting = False

        if self.event == 1:
            if self.double_click:
                self.double_click = False
                self.event = 0
                if self.deleting == False:
                    snap_to_port(self.gates_group,self.new_wire,pos)
                    self.new_wire = None
                    self.delete_timer = 0
                
                    self.delete_module = None
                    self.delete_port = None
            else:
                self.double_click = True
                
        elif self.event == 2:
            if get_dis_nsqrt(self.drag_module.rect.center,(900,600)) < 10000:
                self.drag_module.kill()
            elif self.drag_module.rect.left <= 140:
                self.drag_module.kill()
            self.event = 0
            self.drag_module = None
            self.drag_mPos = (0,0)
        elif self.event == 3:
            if get_dis_nsqrt(self.drag_module.rect.center,(900,600)) < 10000:
                self.drag_module.kill()
            elif self.drag_module.rect.left <= 140:
                self.drag_module.kill()
            self.side_bar.new_module_stop(self.new_type)
            self.event = 0
            self.drag_module = None
            self.drag_mPos = (0,0)

    def click_on_delete(self):
        self.delete_timer = 0
        self.deleting = True
        self.delete_module.port[self.delete_port].kill_wire()
        self.delete_module = None
        self.delete_port = None
        
            
    def click_on_port(self,module,port_id):
        print ("Module:%s; Port:%s; Status:%s"%(module.__class__.__name__ ,str(port_id),module.port[port_id].status))
        if module.port[port_id].is_enough_wire():
            self.new_wire = Wire(module,port_id)
            self.wires_group.add(self.new_wire)
            self.event = 1
        self.delete_timer = 300
        self.delete_module = module
        self.delete_port = port_id
            

    def click_on_module(self,module,rel_pos):
        if module.click_res(rel_pos):
            self.event = 2
            self.drag_module = module
            self.drag_mPos = pygame.mouse.get_pos()
            self.draw_delc_delay = 10

    def add_module(self,module_type,pos,side_bar):
        #1-7:Gates,8:Switch
        self.side_bar = side_bar
        if module_type == 1:
            new_module = Logic_Gates.AND_Gate()
        elif module_type == 2:
            new_module = Logic_Gates.OR_Gate()
        elif module_type == 3:
            new_module = Logic_Gates.XOR_Gate()
        elif module_type == 4:
            new_module = Logic_Gates.NOT_Gate()
        elif module_type == 5:
            new_module = Logic_Gates.NAND_Gate()
        elif module_type == 6:
            new_module = Logic_Gates.NOR_Gate()
        elif module_type == 7:
            new_module = Logic_Gates.XNOR_Gate()
        elif module_type == 8:
            new_module = input_module.Input()

        new_module.rect.center = pos
        self.new_type = module_type
        self.drag_module = new_module
        self.drag_mPos = pygame.mouse.get_pos()
        self.event = 3
        self.draw_delc_delay = 10
        self.gates_group.add(new_module)

    def graphic_logic(self):
        if self.new_wire != None and self.event == 1:
            self.new_wire.update()
            
        if self.delete_timer > 0:
            self.delete_timer -= 1
            self.delete_rect.center = self.delete_module.port_pos(self.delete_port)
            if self.delete_port == 1:
                self.delete_rect.centery -= 20
            else:
                self.delete_rect.centery += 20
            self.delete_rect.centerx -= 5
            self.delete_draw = True
            
        if self.event == 2 or self.event == 3:
            mouse_pos = pygame.mouse.get_pos()
            if get_dis_nsqrt(self.drag_module.rect.center,(900,600)) < 10000:
                self.draw_delc_p = 1
            else:
                self.draw_delc_p = 0

            if self.drag_module.rect.left < 140 and self.event == 2:
                self.draw_delc2 = True
                
            relx = mouse_pos[0] - self.drag_mPos[0]
            rely = mouse_pos[1] - self.drag_mPos[1]
            self.drag_mPos = mouse_pos
            self.drag_module.rect.x += relx
            self.drag_module.rect.y += rely
            self.drag_module.move_update()
            if self.draw_delc_delay <= 0:
                self.draw_delc = True
            else:
                self.draw_delc_delay -= 1
            

    def draw_buttom_layer(self,surface):
        if self.draw_delc:
            self.draw_delc = False
            surface.blit(self.delc_pic[self.draw_delc_p] ,(800,500))
            
        if self.draw_delc2:
            self.draw_delc2 = False
            surface.blit(self.delc_pic2,(0,0))
            
    def draw_top_layer(self,surface):
        #Delete Icon
        if self.delete_draw:
            self.delete_draw = False
            surface.blit(self.delete_icon ,self.delete_rect)

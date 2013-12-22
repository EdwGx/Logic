from lib import select_sprite,snap_to_port,get_dis_nsqrt
import pygame.image,os.path,sys
sys.path.append("..")
from Module.Gate import Wire
class Controller:
    def __init__(self):
        pass

class Graphic(Controller):
    def __init__(self,gates_group,wires_group):
        Controller.__init__(self)
        self.event = 0
        self.new_wire = None
        #Delete
        self.delete_timer = 0
        self.delete_module = None
        self.delete_port = None
        self.deleting = False
        self.delete_icon = pygame.image.load(os.path.join('UI','Resources','delete_icon.png'))
        self.delete_rect = self.delete_icon.get_rect()
        #Drag
        self.drag_timer = 0
        self.drag_module = None
        self.drag_mPos = (0,0)
        #Group
        self.gates_group = gates_group
        self.wires_group = wires_group
        #0:Nothing ; 1:Controlling wire
        #2:Draging module; 3:Draging new module;
    def mouse_down(self,pos):
        if self.event == 0:
            select_sprites = self.gates_group.get_sprites_at(pos)
            number = len(select_sprites)-1
            if number >= 0:
                if abs(select_sprites[number].rect.centerx - pos[0]) <= 30:
                    self.event = 0
                    self.drag_timer = 18 #18 frames;0.3sec delay
                    self.drag_module = select_sprites[number]
                    self.drag_mPos = pos
            
    def mouse_up(self,pos):
        if self.delete_timer > 0:
            dis = get_dis_nsqrt(self.delete_rect.center,pos)
            if dis <= 110:
                self.click_on_delete()
                self.deleting = False
        if self.event == 0:
            self.drag_timer = 0
            select_sprite (self.gates_group,pos,self)
        elif self.event == 1:
            self.event = 0
            if self.deleting == False:
                snap_to_port(self.gates_group,self.new_wire,pos)
                self.new_wire = None
        elif self.event == 2:
            self.drag_timer = 0
            self.event = 0
            self.drag_module = None
            self.drag_mPos = (0,0)

    def click_on_delete(self):
        self.delete_timer = 0
        if self.delete_port == None:
            self.delete_module.kill()
            self.delete_module = None
            self.delete_port = None
            self.deleting = True
        else:
            self.delete_module.port[self.delete_port].kill_wire()
            self.delete_module = None
            self.delete_port = None
            self.deleting = True
            
    def click_on_port(self,module,port_id):
        if module.port[port_id].is_enough_wire:
            self.new_wire = Wire(module,port_id)
            self.wires_group.add(self.new_wire)
            self.event = 1
        self.delete_timer = 300
        self.delete_module = module
        self.delete_port = port_id
            

    def click_on_module(self,module):
        self.delete_timer = 300
        self.delete_module = module
        self.delete_port = None

    def draw_buttom_layer(self,surface):
        pass


    def draw_top_layer(self,surface):
        #self.gates_group.draw(surface)
        #self.wires_group.draw(surface)
        #New_wire
        if self.new_wire != None and self.event == 1:
            self.new_wire.update()
        #Delete Icon
        if self.delete_timer > 0:
            self.delete_timer -= 1
            if self.delete_port == None:
                self.delete_rect.center = self.delete_module.rect.center
                self.delete_rect.centery += 15
                surface.blit(self.delete_icon ,self.delete_rect)
            else:
                self.delete_rect.center = self.delete_module.port_pos(self.delete_port)
                self.delete_rect.centerx += 5
                self.delete_rect.centery += 20
                surface.blit(self.delete_icon ,self.delete_rect)

        if self.event == 2:
            mouse_pos = pygame.mouse.get_pos()
            relx = mouse_pos[0] - self.drag_mPos[0]
            rely = mouse_pos[1] - self.drag_mPos[1]
            self.drag_mPos = mouse_pos
            self.drag_module.rect.x += relx
            self.drag_module.rect.y += rely
            self.drag_module.move_update()

        if self.drag_timer > 0:
            self.drag_timer -= 1
            if self.drag_timer == 0:
                self.event = 2
            
            
            
                

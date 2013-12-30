import pygame.image,os.path,sys
sys.path.append("..")
#from Module.Gate import Wire

class SideBar:
    def __init__(self,graphic_controller):
        #Define
        self.space = 50
        self.speed = 8
        self.height = 600
        self.disply_list = []
        self.waiting_list = []
        self.graphic_controller = graphic_controller
        self.bar_image = pygame.image.load(os.path.join('UI','Resources','selection_bar.png'))
        #Add game elements/module
        #1-7:Gates,8:Switch
        self.waiting_list.append([1,load_image('and_gate.png')])
        self.waiting_list.append([5,load_image('nand_gate.png')])
        self.waiting_list.append([2,load_image('or_gate.png')])
        self.waiting_list.append([6,load_image('nor_gate.png')])
        self.waiting_list.append([3,load_image('xor_gate.png')])
        self.waiting_list.append([7,load_image('xnor_gate.png')])
        self.waiting_list.append([4,load_image('not_gate.png')])
        self.waiting_list.append([8,load_image('switch_off.png')])
        self.waiting_list.append([9,load_image('button_off.png')])
        self.waiting_list.append([10,load_image('bulb_off.png')])
        self.waiting_list.reverse()
        #Add some elements info
        for element in self.waiting_list:
            element.append(element[1].get_width()/2)
            element.append(element[1].get_height()/2)
            element.append(0)
            element.append(0)
            element.append(True)
        self.full_disply()

    
        

    def full_disply(self):
        element = self.waiting_list.pop()#[len(self.waiting_list)-1]
        element[5] = self.space + element[3]
        element[4] = get_centerx(element[5])
        total = element[5] + element[3]
        self.disply_list.append(element)
        while (total < self.height) and (len(self.waiting_list) > 0):
            total += self.space
            element = self.waiting_list.pop()
            element[5] = total + element[3]
            element[4] = get_centerx(element[5])
            total = element[5] + element[3]
            self.disply_list.append(element)
            
            
    def scroll_up(self):
        for element in self.disply_list:
            element[5] += self.speed
            element[4] = get_centerx(element[5])
            
        #Move the data from top of waiting_list to the top of disply_list
        if len(self.waiting_list) > 0:
            top_dis = self.disply_list[0][5] - self.disply_list[0][3]
            if top_dis > self.space:
                element = self.waiting_list.pop(0)
                element[5] = top_dis - self.space - element[3]
                element[4] = get_centerx(element[5])
                self.disply_list.insert(0,element)
            
        #Move the data from bottom of disply_list to the bottom of waiting_list
        last = len(self.disply_list) - 1
        if (self.disply_list[last][5] - self.disply_list[last][3]) > self.height:
            element = self.disply_list.pop()
            element[4] = 0
            element[5] = 0
            self.waiting_list.append(element)

    def scroll_down(self):
        for element in self.disply_list:
            element[5] -= self.speed
            element[4] = get_centerx(element[5])

        if len(self.waiting_list) > 0:
            last = len(self.disply_list) - 1
            bottom_dis = self.height - self.disply_list[last][5]
            bottom_dis -= self.disply_list[last][3]
            if bottom_dis > self.space:
                element = self.waiting_list.pop()
                element[5] = self.height - bottom_dis + self.space + element[3]
                element[4] = get_centerx(element[5])
                self.disply_list.append(element)

        if (self.disply_list[0][5] + self.disply_list[0][3]) < 0:
            element = self.disply_list.pop(0)
            element[4] = 0
            element[5] = 0
            self.waiting_list.insert(0,element)

    def mouse_down(self,pos):
        for element in self.disply_list:
            if element[6]:
                if element[5] + element[3] > pos[1]:
                    if element[5] - element[3] < pos[1]:
                        if element[4] - element[2] < pos[0]:
                            if element[4] + element[2] > pos[0]:
                                element[6] = False
                                self.graphic_controller.add_module(element[0],(element[4],element[5]),self)
                                break
    def new_module_stop(self,mod_type):
        stop = False
        for element in self.disply_list:
            if element[0] == mod_type:
                element[6] = True
                stop = True
                break
        if not(stop):
            for element in self.waiting_list:
                if element[0] == mod_type:
                    element[6] = True
                    stop = True
                    break
        

    def draw(self,surface):
        surface.blit(self.bar_image,(0,0))
        for element in self.disply_list:
            if element[6]:
                surface.blit(element[1],((element[4]-element[2]),(element[5]-element[3])))

def load_image(fname):
    path = os.path.join('Module','Resources',fname)
    return pygame.image.load(path)

def get_centerx(centery):
    y = abs(300 - centery)
    return int(-0.000442*y*y + 90)
            

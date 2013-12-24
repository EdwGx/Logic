import pygame.image,os.path,sys
sys.path.append("..")
#from Module.Gate import Wire

class SideBar:
    def __init__(self):
        #Define
        self.space = 10
        self.height = 600
        self.disply_list = []
        self.waiting_list = []
        #Add game elements/module
        #1-7:Gates,8:Switch
        self.waiting_list.append([1,load_image('and_gate.png')])
        self.waiting_list.append([2,load_image('or_gate.png')])
        self.waiting_list.append([3,load_image('xor_gate.png')])
        self.waiting_list.append([4,load_image('nand_gate.png')])
        self.waiting_list.append([5,load_image('nor_gate.png')])
        self.waiting_list.append([6,load_image('xnor_gate.png')])
        self.waiting_list.append([7,load_image('not_gate.png')])
        self.waiting_list.append([8,load_image('switch_off.png')])
        self.waiting_list.reverse()
        #Add some elements info
        for element in self.waiting_list:
            element.append(element[1].get_width()/2)
            element.append(element[1].get_height()/2)
            element.append(0)
            element.append(0)
            

    def add_top(listA,listB):):
        listB.insert(0,listA.pop(0))

    def add_buttom(listA,listB):
        listB.append(listA.pop())

    def get_centerx(centery):
        y = abs(300 - centery)
        return int(-0.000442*y*y + 90)
        

    def full_display(self):
        element = self.waiting_list.pop()
        element[5] = self.space + element[3]
        element[4] = get_centerx(element[5])
        total = element[5] + element[3]
        self.disply_list.append(element)
        while total < self.height:
            total += self.space
            element = self.waiting_list.pop()
            element[5] = total + element[3]
            element[4] = get_centerx(element[5])
            total = element[5] + element[3]
            self.disply_list.append(element)
            
            
    def scroll_down(self):
        
        
        

    def load_image(fname):
        path = os.path.join('Module','Resources',fname)
        return pygame.image.load(path)

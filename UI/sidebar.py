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
            height = element[1].get_height()
            element.append(height)
            

    def add_top(listA,listB):
        listB.insert(0,listA.pop(0))

    def add_buttom(listA,listB):
        listB.append(listA.pop())

    def upadte(self):
        total = self.space
        for e in self.disply
        
        
        

    def load_image(fname):
        path = os.path.join('Module','Resources',fname)
        return pygame.image.load(path)

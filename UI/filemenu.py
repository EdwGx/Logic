import pygame,os,shutil
from UI import fileIO
class FileMenu:
    def __init__(self):
        self.draw_menu = False
        self.screen_shot = False
        self.block_mouse = False
        self.files_status = []
        for i in range(9):
            self.files_status.append(False)
        font = pygame.font.SysFont("Helvetica",20,True)
        self.button_image = font.render('Save & Load',True,(255,255,255))
        self.button_width = self.button_image.get_width()
        self.current = None
        self.hover = None
        #Graphic
        self.alpha = 180
        self.space = 20
        self.b_height = 40

        self.top = (202,50)
        self.image_pos = []
        
        self.image_pos.append(pygame.Rect(0,0,152,120))
        self.image_pos.append(pygame.Rect(self.space+152,0,152,120))
        self.image_pos.append(pygame.Rect(self.space*2+304,0,152,120))
        
        self.image_pos.append(pygame.Rect(0,self.space+120,152,120))
        self.image_pos.append(pygame.Rect(self.space+152,self.space+120,152,120))
        self.image_pos.append(pygame.Rect(self.space*2+304,self.space+120,152,120))
        
        self.image_pos.append(pygame.Rect(0,self.space*2+240,152,120))
        self.image_pos.append(pygame.Rect(self.space+152,self.space*2+240,152,120))
        self.image_pos.append(pygame.Rect(self.space*2+304,self.space*2+240,152,120))

        self.image_pos.append(pygame.Rect(0,self.space*3+360,152,40))
        self.image_pos.append(pygame.Rect(self.space+152,self.space*3+360,152,40))
        self.image_pos.append(pygame.Rect(self.space*2+304,self.space*3+360,152,40))

        for image_rect in self.image_pos:
            image_rect.move_ip(20,20)
        
    def open_menu(self,pos):
        self.current = None
        self.hover = None
        self.block_mouse = True
        fileIO.check_file
        self.update_file()
        self.redraw_menu()
        self.screen_shot = True

    def mouse_up(self,pos):
        rel = (pos[0] - self.top[0],pos[1] - self.top[1])
        for i in range(12):
            if self.image_pos[i].collidepoint(rel):
                if i < 9:
                    if self.current != i:
                        self.current = i
                        self.redraw_menu()
                    else:
                        self.current = None
                        self.redraw_menu()
                    return (0,None)
                    
                elif i == 9 and self.current != None:
                    path = os.path.join('UI','Save',('logic%d.save'% self.current))
                    shutil.move(os.path.join('UI','Temp','screen_shot.png'),
                                os.path.join('UI','Save',('shot%d.png'% self.current)))
                    self.draw_menu = False
                    self.block_mouse = False
                    return (2,path)
                
                elif i == 10:
                    path = os.path.join('UI','Temp','screen_shot.png')
                    if os.path.exists(path):
                        os.remove(path)
                    self.draw_menu = False
                    self.block_mouse = False
                    return (1,None)
                
                elif i == 11 and self.current != None and  self.files_status[self.current]:
                    path = os.path.join('UI','Temp','screen_shot.png')
                    if os.path.exists(path):
                        os.remove(path)
                    path = os.path.join('UI','Save',('logic%d.save'% self.current))
                    self.draw_menu = False
                    self.block_mouse = False
                    return (3,path)
        return (0,None)
                    

    def update_file(self):
        for i in range(9):
            path = os.path.join('UI','Save',('logic%d.save'% i))
            f = open(path,'r')
            s = f.read(1)
            if s == 'E':
                self.files_status[i] = False
            else:
                self.files_status[i] = True
                
    def redraw_menu(self):
        self.draw_surface = pygame.Surface((496+self.space*3,400+self.space*3+self.b_height),
                                           flags=pygame.SRCALPHA)
        self.draw_surface.convert_alpha()
        selected_image = pygame.image.load(os.path.join('UI','Resources','selected.png')).convert_alpha()
        selected_rect = selected_image.get_rect()
        
        shadow_image = pygame.image.load(os.path.join('UI','Resources','shadow.png')).convert_alpha()
        shadow_rect = shadow_image.get_rect()

        dark = pygame.Surface((152,120))
        dark.fill((255,255,255))
        dark.set_alpha(200)
        for i in range(9):
            if self.files_status[i]:
                path = os.path.join('UI','Save',('shot%d.png'% i))
                self.draw_surface.blit(dark,self.image_pos[i])
            else:
                path = os.path.join('UI','Resources','unknow.png')
                
            image = pygame.image.load(path).convert()
            shadow_rect.center = self.image_pos[i].center
            self.draw_surface.blit(shadow_image,shadow_rect)
            if i == self.hover:
                image.set_alpha(255)
            else:
                image.set_alpha(self.alpha)
                
            self.draw_surface.blit(image,self.image_pos[i])
            if i == self.current:
                selected_rect.center = self.image_pos[i].center
                self.draw_surface.blit(selected_image,selected_rect)
                
                
        image = pygame.image.load(os.path.join('UI','Resources','button_save.png')).convert()
        if 9 != self.hover or self.current == None:
            image.set_alpha(self.alpha)
        self.draw_surface.blit(image,self.image_pos[9])
        
        image = pygame.image.load(os.path.join('UI','Resources','button_cancel.png')).convert()
        if 10 != self.hover:
            image.set_alpha(self.alpha)
        self.draw_surface.blit(image,self.image_pos[10])

        image = pygame.image.load(os.path.join('UI','Resources','button_load.png')).convert()
        if 11 != self.hover or self.current == None or not(self.files_status[self.current]):
            image.set_alpha(self.alpha)
        self.draw_surface.blit(image,self.image_pos[11])

    def graphic_logic(self):
        if self.draw_menu:
            pos = pygame.mouse.get_pos()
            rel = (pos[0] - self.top[0],pos[1] - self.top[1])
            collide = False
            for i in range(12):
                if self.image_pos[i].collidepoint(rel):
                    if i != self.hover:
                        self.hover = i
                        self.redraw_menu()
                        collide = True
                        break
                    else:
                        collide = True
                        break
            if collide == False:
                if self.hover != None:
                    self.hover = None
                    self.redraw_menu()
            
        
                

    def draw(self,surface):
        if self.draw_menu:
            surface.blit(self.draw_surface,self.top)
            mouse_pos = pygame.mouse.get_pos()

        if self.screen_shot:
            self.screen_shot = False
            self.draw_menu = True
            screenshot = pygame.Surface((760,600))
            screenshot.blit(surface,(0,0),(140,0,760,600))
            screenshot = pygame.transform.smoothscale(screenshot,(152,120))
            path = os.path.join('UI','Temp','screen_shot.png')
            pygame.image.save(screenshot,path)
        else:
            surface.blit(self.button_image,(880-self.button_width,10))
            
        

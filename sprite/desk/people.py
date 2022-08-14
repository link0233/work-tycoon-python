import pygame
from config import *

class Desk_people(pygame.sprite.Sprite):
    def __init__(self,baba):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((DESK_PEOPLERADIUS,DESK_PEOPLERADIUS))
        self.image.fill(SKYBLUE)
        self.rect  = self.image.get_rect()
        self.rect.center = (baba.rect.centerx,baba.rect.y+80)
        self.group = pygame.sprite.Group()
        self.baba = baba
        self.pos = [self.rect.centerx-self.baba.rect.centerx,self.rect.centery-self.baba.rect.centery]

        self.baba = baba
        self.type = None
        self.move = []
        self.movespeed = 5

        self.group.add(self)
        self.exit_desk()
        self.goGetTeskDesk()

    def draw(self,screen):
        self.group.draw(screen)

        return screen

    def update(self,baba):
        self.baba = baba
        if self.move!=[]:
            self.pos[0] += self.move[0][0]
            self.pos[1] += self.move[0][1]
            del self.move[0]
        self.rect.centerx = self.pos[0]+self.baba.rect.centerx
        self.rect.centery = self.pos[1]+self.baba.rect.centery

    def exit_desk(self):
        x1 = self.pos[0]
        x2 = self.pos[0]+DESKSIZE[0]//2
        self.addmove(x1,x2,'x')

    def addmove(self,x,x2,type):
        a=x
        if x2>x:
            while a+self.movespeed < x2:
                a+= self.movespeed
                if type == 'x':
                    self.move.append([self.movespeed,0])
                elif type == "y":
                    self.move.append([0,self.movespeed])
            if type == 'x':
                self.move.append([self.movespeed,0])
            elif type == "y":
                self.move.append([0,self.movespeed])

        else:
            while a+self.movespeed > x2:
                a-= self.movespeed
                if type == 'x':
                    self.move.append([-self.movespeed,0])
                elif type == "y":
                    self.move.append([0,-self.movespeed])
            if type == 'x':
                self.move.append([-self.movespeed,0])
            elif type == "y":
                self.move.append([0,-self.movespeed])
        
    def goGetTeskDesk(self):
        y1 = self.pos[1]
        y2 = 120-int(self.baba.rect.y)
        self.addmove(y1,y2,"y")
import pygame
from config import * 

from sprite.desk.people import *

class desk(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.size = (SCREENSIZE[0]//4-120,60)
        self.image = pygame.Surface(self.size)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.pos = ((pos[0]-1)*DESKSIZE[0]+self.size[0]//2+30,(pos[1]-1)*DESKSIZE[1]+200+self.size[1]//2)
        # self.pos = ((pos[0])*DESKSIZE[0]-15,(pos[1])*DESKSIZE[1]+200+self.size[1]//2)
        self.rect.center = self.pos
        self.group = pygame.sprite.Group()

        self.people = Desk_people(self)
        self.deskPos = pos

        self.group.add(self)

    def update(self,posy):
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]+posy

    def draw(self,screen):
        self.group.draw(screen)
        return screen
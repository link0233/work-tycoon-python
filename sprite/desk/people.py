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
        self.pos = (self.rect.centerx-self.baba.rect.centerx,self.rect.centery-self.baba.rect.centery)

        self.baba = baba
        self.type = None

        self.group.add(self)

    def draw(self,screen):
        self.group.draw(screen)

        return screen

    def update(self,baba):
        self.baba = baba
        self.rect.centerx = self.pos[0]+self.baba.rect.centerx
        self.rect.centery = self.pos[1]+self.baba.rect.centery
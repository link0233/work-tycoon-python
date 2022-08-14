import pygame
from config import *

class getTeskDeskDesk(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2000,120))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREENSIZE[0]//2
        self.rect.y = 0
        self.group = pygame.sprite.Group()

        self.posy = 0
        self.mousespeed=10

        self.group.add(self)

    def update(self,mouse):
        if mouse[4]:
            if self.posy <self.mousespeed*-1:
                self.posy+=self.mousespeed
            elif self.posy<0:
                self.posy = 0
        if mouse[3]:
            self.posy-=self.mousespeed

        self.rect.y = self.posy

    def draw(self,screen):
        self.group.draw(screen)
        return screen
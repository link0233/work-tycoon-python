import pygame
from config import *

class TaskBackGround(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,150))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.centery = SCREENSIZE[1]//2
        self.group = pygame.sprite.Group()
        self.number = 1

        self.group.add(self)
    
    def draw(self,screen):
        self.group.draw(screen)
        font = pygame.font.Font(FONT,20)
        fonttext = font.render(str(self.number),True,BLOCK)
        fontrect = fonttext.get_rect()
        fontrect.center = self.rect.center
        screen.blit(fonttext,fontrect)

        return screen
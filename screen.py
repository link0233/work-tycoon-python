import pygame
from gui.Task.Task import *
from sprite.getTaskDesk.script import *

class screen:
    def __init__(self,width=1280,height=960):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))

        self.task = task()
        self.getTaskDesk = getTeskDesk()

        self.gameloop()
        
    def gameloop(self):
        while True:
            self.update()
            self.draw()
            pygame.display.update()

    def update(self):
        self.mousebutton = [False,False,False,False,False]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                import sys;sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button<6:
                    self.mousebutton[event.button-1] = True
                    print(self.mousebutton)

        self.getTaskDesk.update(self.mousebutton)

    def draw(self):
        self.screen.fill((42, 19, 0))
        self.screen = self.getTaskDesk.draw(self.screen)
        self.screen = self.task.draw(self.screen)
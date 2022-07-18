from gui.Task.task import *

class task:
    def __init__(self):
        self.bg = TaskBackGround()

    def draw(self,screen):
        screen = self.bg.draw(screen)
        return screen
from sprite.getTaskDesk.desk import *

class getTeskDesk:
    def __init__(self):
        self.desk = getTeskDeskDesk()

    def draw(self,screen):
        screen = self.desk.draw(screen)
        return screen

    def update(self,mouse):
        self.desk.update(mouse)
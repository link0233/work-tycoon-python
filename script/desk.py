from config import *
from sprite.desk.desk import desk

class Desk:
    def __init__(self):
        self.desk = []
        self.andpos = [1,1]
        self.create_desk()
        self.create_desk()
        self.create_desk()
        self.create_desk()
        self.create_desk()

    def create_desk(self):
        newdesk = desk(self.andpos)
        self.andpos[0]+=1
        if self.andpos[0]>5:
            self.andpos[0]=1
            self.andpos[1]+=1

        self.desk.append(newdesk)

        print(self.andpos)

    def draw(self,screen):
        for d in self.desk:
            screen = d.draw(screen)

        return screen

    def update(self,posy):
        for d in self.desk:
            screen = d.update(posy)
import pygame

class screen:
    def __init__(self,width=1280,height=960):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        self.gameloop()
        
    def gameloop(self):
        while True:
            self.update()
            self.draw()
            pygame.display.update()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                import sys;sys.exit()

    def draw(self):
        self.screen.fill((42, 19, 0))
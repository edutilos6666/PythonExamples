import pygame
from pygame.locals import *





def example2():
    class App:
        def __init__(self):
            self._running = True
            self._display_surf = None
            self._image_surf = None
            self.size = self.weight , self.height = 640 , 640

        def on_init(self):
            pygame.init()
            self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
            self._running = True
            self._image_surf = pygame.image.load("../assets/pygame_img1.jpg").convert()

        def on_event(self, event):
            if event.type == pygame.QUIT:
                self._running = False

        def on_loop(self):
            pass

        def on_render(self):
            self._display_surf.blit(self._image_surf, (0,0))
            pygame.display.flip()

        def on_cleanup(self):
            pygame.quit()

        def on_execute(self):
            if self.on_init() == False:
                self._running = False

            while(self._running):
                for event in pygame.event.get():
                    self.on_event(event)
                self.on_loop()
                self.on_render()
            self.on_cleanup()

    theApp = App()
    theApp.on_execute()







#######################################################


def example1():
    class App:
        def __init__(self):
            self._running = True
            self._display_surf = None
            self.size = self.weight , self.height = 640 , 640

        def on_init(self):
            pygame.init()
            self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
            self._running = True

        def on_event(self, event):
            if event.type == pygame.QUIT:
                self._running = False

        def on_loop(self):
            pass

        def on_render(self):
            pass

        def on_cleanup(self):
            pygame.quit()

        def on_execute(self):
            if self.on_init() == False:
                self._running = False

            while(self._running):
                for event in pygame.event.get():
                    self.on_event(event)
                self.on_loop()
                self.on_render()
            self.on_cleanup()

    theApp = App()
    theApp.on_execute()

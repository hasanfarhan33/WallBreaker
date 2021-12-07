import pygame

class mainMenu:
    def __init__(self, caption, windowWidth, windowHeight):
        self.caption = caption
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

    def menuWindow(self):
        pygame.display.set_caption(self.caption)
        pygame.display.set_mode((self.windowWidth, self.windowHeight))
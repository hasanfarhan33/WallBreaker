import pygame
import sys

class mainMenu:
    def __init__(self, caption, windowWidth, windowHeight):
        self.caption = caption
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

    def menuWindow(self):
        pygame.display.set_caption(self.caption)
        menuFrame = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        return menuFrame

    def addButtons(self, window, buttonWidth, buttonHeight):
        #Button variables
        buttonColor = (143, 241, 242)
        buttonHoverColor = (93, 119, 143)

        #fontVariables
        fontColor = (0, 0, 0)
        buttonFont = pygame.font.SysFont("Consolas", 10)
        startText = "Start"
        quitText = "Quit"

        #Start button variables
        startButtonX = self.windowWidth/2 - buttonWidth / 2
        startButtonY = 300
        pygame.draw.rect(window, buttonColor, (startButtonX, startButtonY, buttonWidth, buttonHeight), border_radius= 20)

        #Quit button variables
        quitButtonX = self.windowWidth / 2 - buttonWidth / 2
        quitButtonY = 370
        pygame.draw.rect(window, buttonColor, (quitButtonX, quitButtonY, buttonWidth, buttonHeight), border_radius = 20)


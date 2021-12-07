import pygame
from mainMenu import mainMenu

#Setting up the display
FPS = 60
clock = pygame.time.Clock()

#INSTANTIATING CLASSES HERE
menu = mainMenu("Main Menu", 500, 500)

def main():
    pygame.init()
    # pygame.display.set_caption("Wallbreaker")
    # WINDOW =pygame.display.set_mode((windowWidth, windowHeight))
    menu.menuWindow()

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False




if __name__ == "__main__":
    main()
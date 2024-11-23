import pygame
from constants import *




def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting...")
                return
        pygame.Surface.fill(screen, color=0)
        pygame.display.flip()

    

if __name__ == "__main__":
    main()
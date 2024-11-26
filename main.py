import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    print("Starting asteroids!")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (bullets, updateable, drawable)

    AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting...")
                return
            
        pygame.Surface.fill(screen, color=0)
        clock.tick(60)
        dt = clock.tick(60) / 1000

        for obj in updateable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.collision(asteroid) == True:
                    asteroid.split()
                    bullet.kill()
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
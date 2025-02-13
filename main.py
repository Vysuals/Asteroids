# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    clock = pygame.time.Clock()
    dt = 0
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots,)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill((0, 0, 0))
        updatable.update(dt)
        shots.update(dt)
        for rock in asteroids:
            if player.collision(rock):
                print("Game over!")
                sys.exit()
        for drawn in drawable:
            drawn.draw(screen)
        for shot in shots:
            shot.draw(screen)
        for rock in asteroids:
            for shot in shots:
                if rock.collision(shot):
                    rock.split()
                    shot.kill()
        pygame.display.flip()
if __name__ == "__main__":
    main()

import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    asteroid_field = AsteroidField()
    updatable_group.add(player, asteroid_field)
    drawable_group.add(player)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updatable_obj in updatable_group:
            updatable_obj.update(dt)
        screen.fill((0, 0, 0))
        for drawable_obj in drawable_group:
            drawable_obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()

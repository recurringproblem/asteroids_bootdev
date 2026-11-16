import pygame
import sys
from logger import log_state, log_event
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player_start_x = SCREEN_WIDTH / 2
    player_start_y = SCREEN_HEIGHT / 2
    player = Player(player_start_x, player_start_y)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()


if __name__ == "__main__":
    main()

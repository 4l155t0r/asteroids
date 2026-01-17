import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize pygame and create the main window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Game time management
    game_time = pygame.time.Clock()
    dt = 0

    # Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # Create game objects
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()


    # Main game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # background color
        screen.fill((0, 0, 0))

        # Draw all drawable sprites
        for sprite in drawable:
            sprite.draw(screen)

        # Update all updatable sprites
        updatable.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event(f"player_hit")
                print("Game over!")
                sys.exit()
        
        # Check for collisions between shots and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event(f"asteroid_shot")
                    asteroid.kill()
                    shot.kill()

        # Update the display - actually show the new frame
        pygame.display.flip()

        # Time and frame rate control
        dt = game_time.tick(60) / 1000.0  # Limit to 60 FPS and convert to seconds

if __name__ == "__main__":
    main()

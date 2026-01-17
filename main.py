import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

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

    # Create a player instance
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)


    # Main game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # background color
        screen.fill((0, 0, 0))

        # Draw the player
        player.draw(screen)

        # Update the display - actually show the new frame
        pygame.display.flip()

        # Time and frame rate control
        dt = game_time.tick(60) / 1000.0  # Limit to 60 FPS and convert to seconds

if __name__ == "__main__":
    main()

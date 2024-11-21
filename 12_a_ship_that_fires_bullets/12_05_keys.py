# 12-5. Keys
# Make a Pygame file that creates an empty screen.

import sys

import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Unitialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # In the event loop, print the event.key attribute whenever a pygame.KEYDOWN event is detected.
            elif event.type == pygame.KEYDOWN:
                print(event.key)    

if __name__ == '__main__':
    # Make a game instance, and run the game.
    # Run the program and press various keys to see how Pygame responds.
    ai = AlienInvasion()
    ai.run_game()
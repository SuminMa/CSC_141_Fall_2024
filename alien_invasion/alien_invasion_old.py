# 12-1. Blue Sky
# Make a Pygame window with a blue background.

# 12-2. Game Character (character.py)

# 12-3. Pygame Documentation
"""https://pygame.org/docs"""

# 12-4. Rocket
"""Had an issue to fix an error: self.character.blitme() --> self.rocket.blitme()"""

import sys

import pygame

from settings import Settings

# from character import Character

from rocket import Rocket

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

        # self.character = Character(self)
        self.rocket = Rocket(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.rocket.blitme() # Draw the rocket at its current location.

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
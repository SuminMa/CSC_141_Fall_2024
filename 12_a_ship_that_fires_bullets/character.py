# 12-2. Game Character
import pygame

class Character:
    """A class to manage the character."""

    def __init__(self, ai_game):
        """Initianlize the character and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the character image and get its rect.
        self.image = pygame.image.load('images/character.bmp') # No need to change the background color.

        # Resize the image to (5, 5) if that's what you're aiming for
        self.image = pygame.transform.scale(self.image, (50, 50))
        
        self.rect = self.image.get_rect()

        # Start each new character at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)
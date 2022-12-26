import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to show only one alien"""
    def __init__(self, ai_settings, screen):
        """Start the alien and setting your initial location"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load an alien picture and set your rect atribute
        self.image = pygame.image.load('alien_invasion/ship.pbm')
        self.rect = self.image.get_rect()
        # Start an alien next to the edge on left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the exacly location of the alien
        self.x = float(self.rect.x)
        self.alien_speed_factor = 1
    
    def check_edges(self):
        """Return true if the alien will on the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to right"""
        self.x += (self.ai_settings.alien_speed_factor *
                    self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien in your actual location"""
        self.screen.blit(self.image, self.rect)
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
        
    def blitme(self):
        """Draw the alien in your actual location"""
        self.screen.blit(self.image, self.rect)
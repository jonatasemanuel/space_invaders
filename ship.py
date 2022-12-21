import pygame


class Ship():
    """Start the spacecraft and set you initial position"""
    def __init__(self, screen) -> None:
        self.screen = screen
        self.image = pygame.image.load('alien_invasion/ship.pbm')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blitme(self):
        """Draw the spacecraft in local point"""
        self.screen.blit(self.image, self.rect)
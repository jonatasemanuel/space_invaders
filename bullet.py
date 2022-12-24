import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ A class that bullets manager shoot from spacecraft"""
    def __init__(self, ai_settings, screen, ship):
        """Make an object for the bullet in actual location of spacecraft"""
        super(Bullet, self).__init__()
        self.screen = screen
        # Create a rect for the bullet em (0, 0)
        self.rect = pygame.Rect(0, 0,
                    ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Stored the position of bullet with a float value
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """Move the bullet to the screen top"""
        # Refresh the decimal location of bullet
        self.y -= self.speed_factor
        # Refresh the rect location
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the bullet on display"""
        pygame.draw.rect(self.screen, self.color, self.rect)

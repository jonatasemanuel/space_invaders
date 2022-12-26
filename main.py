import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # Cria o botão play
    play_button = Button(ai_settings, screen, "Play")
    # Create a spacecraft
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    # Create a group for store the bullets
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    stats = GameStats(ai_settings)
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        if stats.game_active:
                ship.update()
                bullets.update()
                # Unview bullets
                gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
                gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
                gf.update_screen(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        gf.update_screen(ai_settings, stats, screen, ship, aliens, bullets, play_button)


run_game()

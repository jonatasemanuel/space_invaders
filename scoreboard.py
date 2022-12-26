import pygame.font
from pygame.sprite import Group
from ship import Ship


class ScoreBoard():
    """Uma classe para mostrar informações sobre pontuação."""
    def __init__(self, ai_settings, screen, stats) -> None:
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    
    def prep_ships(self):
        """Mostra quantas espaçonaves restam."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_level(self):
        """Transforma o nivel em uma imagem renderizada"""
        self.level_imagem = self.font.render(str(self.stats.level), True,
                        self.text_color, self.ai_settings.bg_color)
        # Posiciona o nível abaixo da pontuação
        self.level_rect = self.level_imagem.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_score(self):
        """Transforma a pontuação em uma imagem renderizada."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score}"
        # score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                        self.ai_settings.bg_color)
        # Exibe a pontuação na parte superior da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                        self.ai_settings.bg_color)
        # Centraliza a pontuação máxima na parte superior da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_imagem, self.level_rect)
        self.ships.draw(self.screen)


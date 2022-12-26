class Settings():
    def __init__(self) -> None:
        """Display config"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # spacecraft confg
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        # Bullets settings
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Aliens config
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 20
        self.fleet_direction = 1
        

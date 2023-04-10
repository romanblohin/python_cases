class Settings:
    """A class to store all settings for RocketGame"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = (0, 0, 0)
        # Bullet settings
        self.bullet_width = 15 
        self.bullet_height = 3 
        self.bullets_allowed = 10
        self.bullet_color = (230, 230, 230)
        #Ship settings
        self.ship_width = 15
        self.ship_height = 80
        self.ship_color = (230, 230, 230)

        # Темп ускорения игры
        self.speedup_scale = 1.1
        self.speedup_flag = False

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.rocket_speed = 1.5
        self.bullet_speed = 3.0
        self.ship_speed = 0.5
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.rocket_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
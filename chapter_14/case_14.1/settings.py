class Settings:
    """A class to store all settings for RocketGame"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = (0, 0, 0)
        # Настройки ракеты 
        self.rocket_speed = 2
        # Параметры снаряда 
        self.bullet_speed = 1
        self.bullet_width = 15 
        self.bullet_height = 3 
        self.bullets_allowed = 3
        self.bullet_color = (230, 230, 230)
        #Ship settings
        self.ship_width = 15
        self.ship_height = 80
        self.ship_speed = 0.2
        self.fleet_direction = -1
        self.ship_color = (230, 230, 230)
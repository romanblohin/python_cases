class Settings:
    """A class to store all settings for RocketGame."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = (230, 230, 230)
        # Настройки ракеты 
        self.rocket_speed = 2
        # Настройки космического корабля 
        self.spaceship_speed = 0.2
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево. 
        self.fleet_direction = 1
        # Параметры снаряда 
        self.bullet_speed = 1
        self.bullet_width = 15 
        self.bullet_height = 3 
        self.bullets_allowed = 10
        self.bullet_color = (0, 0, 0)
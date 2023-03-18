class Settings:
    """A class to store all settings for Alien Invasion."""

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
        self.bullets_allowed = 10
        self.bullet_color = (230, 230, 230)
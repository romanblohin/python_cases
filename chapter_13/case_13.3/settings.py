class Settings:
    """A class to store all settings for rain."""

    def __init__(self):
        """Initialize the settings."""
        # Screen settings
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = (230, 230, 230)
        # Настройки капли 
        self.drop_speed = 0.5
        
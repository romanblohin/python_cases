import pygame
from pygame.sprite import Sprite
 
class Spaceship(Sprite):
    """A class to represent a single spaceship in the fleet."""

    def __init__(self, ai_game):
        """Initialize the spaceship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the spaceship image and set its rect attribute.
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()

        # Start each new spaceship near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the spaceship's exact horizontal position.
        self.y = float(self.rect.y)

    def update(self): 
        """Перемещает космический корабль влево или вправо.""" 
        self.y += (self.settings.spaceship_speed * self.settings.fleet_direction)
        self.rect.y = self.y

    def check_edges(self): 
        """Возвращает True, если космический корабль находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0: 
            return True

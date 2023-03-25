import pygame
from pygame.sprite import Sprite
 
class Drop(Sprite):
    """A class to represent a single drop in the fleet."""

    def __init__(self, ai_game):
        """Initialize the drop and set its starting position."""
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        
        # Load the drop image and set its rect attribute.
        self.image = pygame.image.load('images/drop.bmp')
        self.rect = self.image.get_rect()

        # Start each new drop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the drop's exact horizontal position.
        self.y = float(self.rect.y)

    def update(self): 
        """Перемещает капли вниз""" 
        self.rect.y += self.settings.drop_speed
        #self.rect.y = self.y

    def check_edges(self): 
        """Возвращает True, если пришелец находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0: 
            return True

import pygame
from pygame.sprite import Sprite
 
class Ship(Sprite):
    """A class to represent a single spaceship in the fleet."""

    def __init__(self, ai_game):
        """Initialize the spaceship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.color = self.settings.ship_color

        self.rect = pygame.Rect(0, 0, self.settings.ship_width,
            self.settings.ship_height)
        
        #Start each new ship at the right center of the screen.
        self.rect.midright = self.screen_rect.midright

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self): 
        """Перемещает корабль вниз или вверх.""" 
        self.y += (self.settings.ship_speed * self.settings.fleet_direction)
        self.rect.y = self.y

    def check_edges(self): 
        """Возвращает True, если корабль находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0: 
            return True

    def draw_ship(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def center_ship(self):
        """Размещает корабль в центре правой стороны."""
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)

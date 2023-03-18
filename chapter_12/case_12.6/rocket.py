import pygame
 
class Rocket:
    """A class to manage the rocket."""
 
    def __init__(self, ai_game):
        """Initialize the rocket and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        # Start each new rocket at the bottom center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Флаг перемещения 
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.rocket_speed

    def blitme(self):
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
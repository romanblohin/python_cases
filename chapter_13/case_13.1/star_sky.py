import sys

import pygame

from star import Star


class StarSky:
    """Overall class to manage game assets and behavior.""" 

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        
        self.bg_color = (0, 0, 0)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Star Sky")

        self.stars = pygame.sprite.Group()

        self._create_stars()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)                
                            
    def _check_keydown_events(self, event): 
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_q:
            sys.exit()
        
    def _create_stars(self):
        """Create the fleet of stars."""
        # Create an star and find the number of stars in a row.
        # Spacing between each star is equal to one star width.
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)
        
        # Determine the number of rows of stars that fit on the screen.
        available_space_y = self.screen_height - (2 * star_height)
        number_rows = available_space_y // (2 * star_height)
        
        # Create the full fleet of stars.
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Create an star and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = StarSky()
    ai.run_game()

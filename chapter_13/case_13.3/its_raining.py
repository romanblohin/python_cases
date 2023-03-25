import sys

import pygame

from random import randint

from settings import Settings
from drop import Drop

class Raining:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        
        #self.screen = pygame.display.set_mode(
        #    (self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("It's raining")

        self.drops = pygame.sprite.Group()

        self._create_rain()

    def _number_drops_rows(self):
        # Создание капли и вычисление количества капель в ряду 
        # Интервал между соседними каплями равен ширине капли.
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size 
        available_space_x = self.settings.screen_width - (2 * drop_width)
        self.number_drops_x = available_space_x // (2 * drop_width)

        """Определяет количество рядов, помещающихся на экране."""
        available_space_y = (self.settings.screen_height - drop_height)
        self.number_rows = available_space_y // (2 * drop_height)

    def _create_rain(self): 
        """Создание дождя"""
        # Вычисляем количество капель в ряду и количество рядов       
        self._number_drops_rows()
        
        # Создание дождя. 
        for row_number in range(self.number_rows):
            for drop_number in range(self.number_drops_x):
                self._create_drop(drop_number, row_number)

    def _create_drop(self, drop_number, row_number): 
        """Создание капли и размещение её в ряду."""
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size
        drop.x = drop_width + 2 * drop_width * drop_number + randint(-10, 10)
        drop.drop_number = drop_number
        drop.rect.x = drop.x
        drop.rect.y = drop.rect.height + 2 * drop.rect.height * row_number + randint(-10, 10)
        self.drops.add(drop)

    def _check_fleet_edges(self): 
        """Реагирует на достижение пришельцем края экрана."""
        for drop in self.drops.sprites(): 
            if drop.check_edges():
                self._change_fleet_direction() 
                break

    def run_game(self):
        """Start the main loop for the game."""
        while True:

            self._check_events()
            self._update_drops()                        
            self._update_screen()
    
    def _update_drops(self): 
        """Обновляет позиции всех капель."""
        #self._check_fleet_edges() 
        self.drops.update()
        
        for drop in self.drops.copy():
            if drop.rect.bottom >= self.settings.screen_height: 
                self.drops.remove(drop)
                #for drop_number in range(self.number_drops_x):
                self._create_drop(drop.drop_number, 0)

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)                
                
    def _check_keydown_events(self, event): 
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_q:
            sys.exit()
        
    def _update_screen(self):
        # При каждом проходе цикла перерисовывается экран. 
        self.screen.fill(self.settings.bg_color)
        self.drops.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = Raining()
    ai.run_game()
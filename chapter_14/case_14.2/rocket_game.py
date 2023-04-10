import sys

import pygame

from rocket import Rocket
from game_stats import GameStats
from button import Button
from settings import Settings
from bullet import Bullet
from ship import Ship

class RocketGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Rocket Game")

        # Создание экземпляра для хранения игровой статистики.
        self.stats = GameStats(self)

        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.ships = pygame.sprite.Group()

        self._create_ship()
        
        # Создание кнопки Play.
        self.play_button = Button(self, "Play")

    def _create_ship(self): 
        """Создание корабля."""
        ship = Ship(self)
        self.ships.add(ship)

    def run_game(self):
        """Start the main loop for the game."""
        while True:

            self._check_events()

            if self.stats.game_active:
                self.rocket.update()
                self._update_bullets()
                self._update_ship()
            
            self._update_screen()

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиций снарядов.
        self.bullets.update()

        # Удаление снарядов, вышедших за край экрана. Считаем статистику снарядов ушедших за край экрана 
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)
                self.stats.missed_bullets += 1
                
        self._check_bullet_ship_collisions()

    def _check_bullet_ship_collisions(self):
        """Обработка коллизий снарядов с кораблем"""
        # Удаление снарядов, участвующих в коллизиях.

        # Проверка попаданий в корабль.
        # При обнаружении попадания удалить снаряд.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.ships, True, False)

        if self.stats.missed_bullets >= self.settings.bullets_allowed:
            self.stats.game_active = False
    
    def _update_ship(self): 
        """Обновляет позицию корабля, делает проверку достиг ли корабль края экрана
           При достижении края экрана корабль меняет направление движения"""
        for ship in self.ships:
            if ship.check_edges():
                self.settings.fleet_direction *= -1
            ship.update()

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.start_game()
            

    def start_game(self):
        # Сброс игровой статистики.
        self.stats.reset_stats()
        self.stats.game_active = True

        # Очистка списка снарядов.
        self.bullets.empty()

        # Создание размещение ракеты и корабля в центре.
        self.rocket.center_rocket()
        [ship.center_ship() for ship in self.ships]

        # Указатель мыши скрывается.
        pygame.mouse.set_visible(False)
                
    def _check_keydown_events(self, event): 
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_DOWN: 
            self.rocket.moving_down = True
        elif event.key == pygame.K_UP: 
            self.rocket.moving_up = True
        elif event.key == pygame.K_q: 
            sys.exit()
        elif event.key == pygame.K_p:
            if not self.stats.game_active:
                self.start_game()
        elif event.key == pygame.K_SPACE: 
            self._fire_bullet()

    def _check_keyup_events(self, event): 
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_DOWN: 
            self.rocket.moving_down = False
        elif event.key == pygame.K_UP: 
            self.rocket.moving_up = False

    def _fire_bullet(self): 
        """Создание нового снаряда и включение его в группу bullets."""
        new_bullet = Bullet(self) 
        self.bullets.add(new_bullet)

    def _update_screen(self):
        # При каждом проходе цикла перерисовывается экран. 
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites(): 
            bullet.draw_bullet()

        [ship.draw_ship() for ship in self.ships]

        # Кнопка Play отображается в том случае, если игра неактивна.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = RocketGame()
    ai.run_game()
import sys

import pygame

from rocket import Rocket
from settings import Settings
from bullet import Bullet
from spaceship import Spaceship

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

        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.spaceships = pygame.sprite.Group()

        self._create_fleet()

    def _create_fleet(self): 
        """Создание флота вторжения."""
        # Создание космического корабля и вычисление количества кораблей в ряду 
        # Интервал между соседними кораблями равен ширине корабля.

        spaceship = Spaceship(self)
        spaceship_width, spaceship_height = spaceship.rect.size
        rocket_width = self.rocket.rect.width
        available_space_x = (self.settings.screen_width - 
            (3 * spaceship_width) - rocket_width) 
        
        number_spaceships_x = available_space_x // (2 * spaceship_width)
        
        """Определяет количество рядов, помещающихся на экране."""
        available_space_y = self.settings.screen_height - spaceship_height
        number_rows = available_space_y // (2 * spaceship_height)
        
        # Создание флота вторжения. 
        for row_number in range(number_rows):
            for spaceship_number in range(number_spaceships_x):
                self._create_spaceship(spaceship_number, row_number, rocket_width)

    def _create_spaceship(self, spaceship_number, row_number, rocket_width): 
        """Создание пришельца и размещение его в ряду."""
        spaceship = Spaceship(self)
        spaceship_width, spaceship_height = spaceship.rect.size
        spaceship.rect.x = self.settings.screen_width - 2 * spaceship.rect.height * (spaceship_number + 1)
        
        spaceship.y = spaceship.rect.height + 2 * spaceship.rect.height * row_number
        spaceship.rect.y = spaceship.y
        self.spaceships.add(spaceship)

    def _check_fleet_edges(self): 
        """Реагирует на достижение космическим кораблем края экрана."""
        for spaceship in self.spaceships.sprites(): 
            if spaceship.check_edges():
                self._change_fleet_direction() 
                break

    def _change_fleet_direction(self): 
        """Опускает весь флот и меняет направление флота."""
        for spaceship in self.spaceships.sprites(): 
            spaceship.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def run_game(self):
        """Start the main loop for the game."""
        while True:

            self._check_events()
            self.rocket.update()
            self._update_bullets()
            self._update_spaceships()
            self._update_screen()

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиций снарядов.
        self.bullets.update()

        # Удаление снарядов, вышедших за край экрана. 
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)

        self._check_bullet_spaceship_collisions()

    def _check_bullet_spaceship_collisions(self):
        """Обработка коллизий снарядов с космическими кораблями."""
        # Удаление снарядов и кораблей, участвующих в коллизиях.

        # Проверка попаданий в корабли.
        # При обнаружении попадания удалить снаряд и корабль.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.spaceships, True, True)

        if not self.spaceships:
            # Уничтожение существующих снарядов и создание нового флота.
            self.bullets.empty()
            self._create_fleet()

    def _update_spaceships(self): 
        """Обновляет позиции всех пришельцев во флоте."""
        self._check_fleet_edges() 
        self.spaceships.update()
            
    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event): 
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_DOWN: 
            self.rocket.moving_down = True
        elif event.key == pygame.K_UP: 
            self.rocket.moving_up = True
        elif event.key == pygame.K_q: 
            sys.exit()
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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self) 
            self.bullets.add(new_bullet)

    def _update_screen(self):
        # При каждом проходе цикла перерисовывается экран. 
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites(): 
            bullet.draw_bullet()

        self.spaceships.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = RocketGame()
    ai.run_game()
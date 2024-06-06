import sys
import pygame
from settings import Settings
from ship import Ship
from hero import Hero

class Game:
    def __init__(self):
        # Initialize game and create game resources
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.hero = Hero(self)
    
    def run_game(self):
        while True:
            self.check_events()
            self.ship.update()
            self.update_screen()
            self.clock.tick(60)

    def check_events(self):
        # Keyboard and mouse inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.keyup_events(event)
                        
    def keydown_events(self, event):
        # Start moving the ship
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def keyup_events(self, event):
        # Stop moving the ship
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.hero.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game
    ai = Game()
    ai.run_game()

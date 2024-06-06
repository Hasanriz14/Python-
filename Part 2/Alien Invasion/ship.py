import pygame
import sys

class Ship:
    def __init__(self, ai_game):
        # Initialize the Ship and set its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the Ship image and get its rect
        try:
            self.image = pygame.image.load('images/ship.bmp')
        except pygame.error as e:
            print(f"Unable to load image: {e}")
            sys.exit()

        self.rect = self.image.get_rect()
        # Start each Ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update the ship's position based on movement flags
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)

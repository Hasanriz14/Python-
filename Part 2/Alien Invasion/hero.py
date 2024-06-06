import pygame
class Hero:
    def __init__(self,ai_game):
        # Initialize the hero and set its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Load the Hero image and get its rect
        self.image = pygame.image.load('images/hero.bmp')
        self.rect = self.image.get_rect()

        # Start each Hero at the Center of the Screen
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        # Draw the hero at its current location
        self.screen.blit(self.image,self.rect)
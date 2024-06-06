import pygame 
class Main_character:
    def __init__(self, art):
        self.screen = art.screen
        self.screen_rect = art.screen.get_rect()
        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect = midleft
        self.x =float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x
    
    def draw(self):
        self.screen.blit(self.image,self.rect)
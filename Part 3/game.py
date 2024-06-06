import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Rocket')
clock = pygame.time.Clock()
get_surf = pygame.image.load("graphics\Sky.png")
get_bot = pygame.image.load("graphics/ground.png")
get_snail = pygame.image.load('graphics/snail/snail1.png')
get_display_rect = screen.get_rect()
get_img_rect = get_bot.get_rect()
create_text = pygame.font.Font(pygame.font.get_default_font(),22)
send_text = create_text.render('Binky',True,(60,60,60))
get_img_rect.bottom = get_display_rect.bottom
snail_x_pos = 550
snail_y_pos = 600



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            exit()
    screen.blit(get_surf,(0,0))
    screen.blit(get_bot,get_img_rect)
    screen.blit(send_text,(100,100))
    snail_x_pos -= 3
    screen.blit(get_snail,(snail_x_pos,600))
    pygame.display.update
    pygame.display.update()
    clock.tick(60)
import pygame ,sys 
from screen import Screen
from main_char import Main_character

pygame.init()
scr = Screen()
screen = pygame.display.set_mode((scr.screen_width,scr.screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

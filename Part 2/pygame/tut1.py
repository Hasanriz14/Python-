import pygame, sys
# Moving an Image on a screen
def get_pos():
    player_pos = 1
    scr = [1,2,4,5,7,3,1]
    print(scr)
    scr[4] = 1
    print(scr)
    scr[player_pos] =12
    print(scr)

def set_pos():
    background = [1,2,2,2,1,1,2]
    screen = [0]*7
    for i in range(7):
        screen[i] = background[i]
    print(f"screen: {screen}")
    player_pos = 3
    screen[player_pos] = 14
    print(f"screen: {screen}")
    screen[player_pos] = background[player_pos]
    player_pos = player_pos -1 
    screen[player_pos] = 9
    print(f"screen: {screen}")
    print(f"background: {background}")

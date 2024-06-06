import pygame

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
running = True
dt = 0 

player_pos  = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    screen.fill("blue")


  # Define a simple triangle around the player position
    points = [
        (player_pos.x, player_pos.y - 20),   # Top point
        (player_pos.x - 20, player_pos.y + 20), # Bottom left point
        (player_pos.x + 20, player_pos.y + 20)  # Bottom right point
    ]
    
    pygame.draw.polygon(screen, "white", points)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) /1000
pygame.quit()
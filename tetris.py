import pygame

pygame.init()
screen = pygame.display.set_mode((500, 800))
clock = pygame.time.Clock()
running = True
rect_pos = [screen.get_width()/2, screen.get_height()/2]
rect_size = 20
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    screen.fill("purple")
    pygame.draw.rect(screen, "white", (rect_pos[0]-rect_size, rect_pos[1]-rect_size, rect_size, rect_size))
    key = pygame.key.get_pressed()
    
    if(key[pygame.K_w] or key[pygame.K_UP]):
        rect_pos[1] -= 100 * dt
    elif (key[pygame.K_s] or key[pygame.K_DOWN]):
        rect_pos[1] += 100 * dt
    elif (key[pygame.K_a] or key[pygame.K_LEFT]):
        rect_pos[0] -= 100 * dt
    elif (key[pygame.K_d] or key[pygame.K_RIGHT]):
        rect_pos[0] += 100 * dt

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

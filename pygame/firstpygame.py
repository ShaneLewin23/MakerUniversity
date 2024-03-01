import pygame

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.Rect((300,250, 20, 20))
thing = pygame.Rect((123, 700, 20, 20))

run = True

def movePlayer(player, key, velocity=None):

    if velocity is None: 
        increment = .5
    else: 
        increment = velocity

    # move left 
    if key[pygame.K_a] == True and player.left > 0:
        player.move_ip(-velocity,0)
    
    # move right 
    elif key[pygame.K_d] == True and player.right < SCREEN_WIDTH:
        player.move_ip(velocity,0)
    
    # move up 
    elif key[pygame.K_w] == True and player.top > 0:
        player.move_ip(0,-velocity)

    # move right 
    elif key[pygame.K_s] == True and player.bottom < SCREEN_HEIGHT:
        player.move_ip(0,velocity)

def scr_fill(switch=False):
    if not switch: 
        scrf = (0,0,0)
    else:
        scrf = (255,255,255)
    return scrf

while run: 
    switch = False
    screen.fill(scr_fill(switch))
    pygame.draw.rect(screen, (255,123,0), player)
    pygame.draw.rect(screen, (255,255,255), thing)

    key = pygame.key.get_pressed()
    movePlayer(player=player, key=key, velocity=2)
    if player.colliderect(thing):
        switch = not switch
        scr_fill = scr_fill(switch)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False;

    pygame.display.update()




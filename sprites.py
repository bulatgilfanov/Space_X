import pygame

pygame.init()
win = pygame.display.set_mode((1000, 900))


player = pygame.image.load("sprites/ship.png")
background = pygame.image.load("fon/space.jpg")

x = 350
y = 500
speed = 10

clock = pygame.time.Clock()
run = True
while (run):
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed

    win.blit(background, (0, 0))
    win.blit(player, (x, y))
    pygame.display.update()

pygame.quit()
import pygame

win = pygame.display.set_mode((600, 400))

x = 100
y = 50

a =50
b =10

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    b = b + 1
    if b > 500:
        b = 0

    win.fill((220, 255, 100))
    pygame.draw.rect(win, (10, 25, 234), (x, y, 100, 150))
    pygame.draw.circle(win, (0, 57, 169), (a, b), 50)
    pygame.display.update()

    pygame.time.delay(10)



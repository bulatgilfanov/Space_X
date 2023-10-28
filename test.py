background = pygame.image.load("fon/space.jpg")
background_rect = background.get_rect()
player_img = pygame.image.load("sprites/ship.jpg")
meteor_img = pygame.image.load("sprites/meteorBrown.png")
bullet_img = pygame.image.load("sprites/laserRed.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()

        self.image = pygame.transform.scale(player_img, (50, 38))


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


win, color, random.randint(0, 1000), 50
color = random.choices(range(256), k=3)



lastMove = "up"

class Laser():
    def __init__(self, x, y, radius, facing):
        self.facing = facing
        self.x = x
        self.y = y
        self.radius = radius
        self.vel = 8 * facing

    def draw(self):
        self.win.blit(laser, (self.x, self.y), self.radius)

    def drawWindow(self):
        for bullet in bullets:
            bullet.draw(win)

        pygame.display.update()

        win.blit(background, (0, 0))

        for bullet in bullets:
            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

                if gameplay:
                else:

                    if gameplay:
                        mouse = pygame.mouse.get_pos()
                    if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:

                        def start_game():

                            run = True
                            while (run):
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        run = False

                                        def start_game():

                                            run = True
                                            while (run):
                                                for event in pygame.event.get():
                                                    if event.type == pygame.QUIT:
                                                        run = False

